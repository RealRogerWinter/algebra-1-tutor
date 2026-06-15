"""SSOT for the viz (HTML/SVG/interactive) figures embedded in the textbook (build tooling, CI gate).

Each viz figure gets a reference code (<lesson>.fN, appended after any deterministic figures.py
figure in that lesson; <unit>.0.fN for a unit-overview figure). The build (build_textbook._viz_code)
reads this registry to number each embedded viz as "Figure <code>" with a deep-link id, exactly like
the deterministic figures. Any math a viz asserts is recorded here as `facts` (lhs == rhs string
pairs) and VETTED WITH SYMPY by check(); check() also confirms each code is unique + well-formed,
each module#index sample exists, and the registry is in 1:1 correspondence with the
<!--viz:module#index--> markers actually placed in textbook-src/.

  python _verification/viz_figures.py            # report the registry
  python _verification/viz_figures.py --check    # vet codes + sympy facts + marker correspondence
"""
import argparse, glob, importlib.util, os, re, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
VIZ_DIR = os.path.join(HERE, "viz")
TEXTBOOK_SRC = os.path.join(REPO_ROOT, "textbook-src")
CODE_RE = re.compile(r"^(?:[1-9]|1[0-2]|A)\.\d+\.f\d+[a-z]?$")   # e.g. 2.3.f1, 5.4.f2, 5.0.f1
MARKER_RE = re.compile(r"<!--\s*viz:([a-z0-9_]+)#(\d+)\s*-->")

# code, module, index, facts (each fact a (lhs, rhs) pair verified expand-equal under sympy).
# facts == [] for figures with no asserted math (process flowcharts, the concept map, reference
# cards, the live interactive explorers, and the labelled fraction diagram).
VIZ_FIGURES = [
    {"code": "1.1.f1", "module": "interactive_equation", "index": 0, "facts": [("4+3", "7")]},
    {"code": "1.3.f1", "module": "flowcharts", "index": 0, "facts": [("8-2*3+4", "6")]},
    {"code": "1.5.f1", "module": "interactive_equation", "index": 1, "facts": [("3*4+2", "14")]},
    {"code": "2.1.f1", "module": "interactive_equation", "index": 2, "facts": [("4*5", "20")]},
    {"code": "2.2.f1", "module": "bar_models", "index": 2, "facts": [("2*4+3", "11")]},
    {"code": "2.2.f2", "module": "annotated_examples", "index": 0, "facts": [("2*4+3", "11")]},
    {"code": "2.3.f1", "module": "area_models", "index": 3, "facts": [("3*x+2*x", "5*x")]},
    {"code": "2.3.f2", "module": "area_models", "index": 0, "facts": [("2*(x+4)", "2*x+8")]},
    {"code": "2.4.f1", "module": "flowcharts", "index": 1, "facts": [("3*(2-2)+4", "2*(2+1)-2")]},
    {"code": "2.5.f1", "module": "anatomy", "index": 1, "facts": []},
    {"code": "2.6.f1", "module": "annotated_examples", "index": 2, "facts": [("6/2+6/3", "5")]},
    {"code": "3.1.f1", "module": "double_number_lines", "index": 0, "facts": [("60/1", "120/2"), ("120/2", "180/3")]},
    {"code": "3.2.f1", "module": "double_number_lines", "index": 1, "facts": [("4/3", "8/6"), ("8/6", "12/9")]},
    {"code": "3.3.f1", "module": "double_number_lines", "index": 2, "facts": [("10/40", "Rational(1,4)"), ("20/40", "Rational(1,2)")]},
    {"code": "5.0.f1", "module": "concept_map", "index": 1, "facts": []},
    {"code": "5.0.f2", "module": "reference_cards", "index": 0, "facts": []},
    {"code": "5.2.f2", "module": "interactive_graph", "index": 1, "facts": [("2*3-1", "5")]},
    {"code": "5.3.f2", "module": "example_graphs", "index": 0, "facts": [("2*1-1", "1"), ("2*0-1", "-1")]},
    {"code": "5.4.f2", "module": "anatomy", "index": 0, "facts": [("2*1+1", "3")]},
    {"code": "5.4.f3", "module": "interactive_graph", "index": 0, "facts": []},
    {"code": "5.6.f2", "module": "anatomy", "index": 3, "facts": [("2*3+3*0", "6"), ("2*0+3*2", "6")]},
    {"code": "6.2.f1", "module": "bar_models", "index": 3, "facts": [("12+15", "27"), ("15-12", "3")]},
    {"code": "6.2.f2", "module": "bar_models", "index": 0, "facts": [("7+11", "18")]},
    {"code": "10.1.f1", "module": "anatomy", "index": 2, "facts": [("2**4", "16")]},
    {"code": "10.4.f1", "module": "area_models", "index": 1, "facts": [("(x+2)*(x+3)", "x**2+5*x+6")]},
    {"code": "11.2.f1", "module": "area_models", "index": 2, "facts": [("x**2+5*x+6", "(x+2)*(x+3)")]},
    {"code": "12.0.f1", "module": "reference_cards", "index": 1, "facts": []},
    {"code": "12.3.f2", "module": "example_graphs", "index": 1, "facts": [("2**2-5*2+6", "0"), ("3**2-5*3+6", "0")]},
    {"code": "12.4.f1", "module": "area_models", "index": 4, "facts": [("x**2+6*x+9", "(x+3)**2")]},
    {"code": "12.5.f2", "module": "flowcharts", "index": 2, "facts": []},
    {"code": "12.6.f2", "module": "interactive_graph", "index": 2, "facts": []},
    {"code": "A.1.f1", "module": "stats_charts", "index": 1, "facts": []},
    {"code": "A.1.f2", "module": "stats_charts", "index": 0, "facts": []},
    {"code": "A.3.f1", "module": "stats_charts", "index": 2, "facts": [("6/20", "Rational(3,10)"), ("24/30", "Rational(4,5)")]},
]


def _import_viz(name):
    fp = os.path.join(VIZ_DIR, name + ".py")
    if not os.path.exists(fp):
        return None
    spec = importlib.util.spec_from_file_location("vizfig_" + name, fp)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _fact_ok(lhs, rhs):
    x, y = sp.symbols("x y")
    ns = {"x": x, "y": y, "Rational": sp.Rational, "sqrt": sp.sqrt, "pi": sp.pi}
    try:
        return sp.simplify(sp.expand(sp.sympify(lhs, locals=ns)) - sp.expand(sp.sympify(rhs, locals=ns))) == 0
    except Exception:
        return False


def _markers_in_source():
    """{(module, index)} for every <!--viz:..#..--> marker placed across textbook-src/*.md."""
    found = set()
    for fp in glob.glob(os.path.join(TEXTBOOK_SRC, "*.md")):
        for m in MARKER_RE.finditer(open(fp, encoding="utf-8").read()):
            found.add((m.group(1), int(m.group(2))))
    return found


def check():
    issues, codes, pairs = [], set(), set()
    cache = {}
    det_codes = set()
    try:
        sys.path.insert(0, HERE)
        import figures as _det
        det_codes = {s["code"] for s in _det.FIGURES}
    except Exception:
        pass
    for vf in VIZ_FIGURES:
        code, mod_name, idx = vf["code"], vf["module"], vf["index"]
        if code in codes:
            issues.append(f"duplicate viz figure code {code}")
        codes.add(code)
        if not CODE_RE.match(code):
            issues.append(f"viz figure code {code} violates the figure-code grammar")
        if code in det_codes:
            issues.append(f"viz figure code {code} collides with a deterministic figures.py code")
        pairs.add((mod_name, idx))
        if mod_name not in cache:
            try:
                cache[mod_name] = _import_viz(mod_name)
            except Exception as e:  # noqa: BLE001
                cache[mod_name] = None
                issues.append(f"{code}: viz module {mod_name} failed to import: {e}")
        mod = cache[mod_name]
        if mod is not None:
            try:
                mod.samples()[idx]
            except Exception:
                issues.append(f"{code}: {mod_name}#{idx} sample does not exist")
        for (lhs, rhs) in vf.get("facts", []):
            if not _fact_ok(lhs, rhs):
                issues.append(f"{code}: sympy fact failed: {lhs} == {rhs}")
    # density: per lesson, viz f-indices must not collide and should be contiguous from where
    # deterministic figures leave off (we only enforce no-duplicate + no-gap among viz themselves
    # together with the deterministic ones is checked by figure_lint's grammar; here keep it simple).
    # bidirectional registry <-> placed markers
    placed = _markers_in_source()
    for (m, i) in sorted(placed - pairs):
        issues.append(f"marker <!--viz:{m}#{i}--> placed in source but has no viz_figures entry")
    for (m, i) in sorted(pairs - placed):
        issues.append(f"viz figure {m}#{i} registered but no <!--viz:{m}#{i}--> marker in source")
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        iss = check()
        if iss:
            print("FAIL:\n  " + "\n  ".join(iss)); return 1
        nf = sum(len(v["facts"]) for v in VIZ_FIGURES)
        print(f"viz_figures: {len(VIZ_FIGURES)} figures coded; {nf} sympy facts verified; "
              f"registry <-> markers in sync."); return 0
    for vf in VIZ_FIGURES:
        print(vf["code"], "<-", vf["module"], "#", vf["index"], "facts:", len(vf["facts"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
