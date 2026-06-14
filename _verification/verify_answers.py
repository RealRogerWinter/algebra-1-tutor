"""
Central answer-key verifier for the algebra-1-tutor skill (build tooling, not shipped).

Loads every _verification/unit-*.json + appendix.json and independently re-checks
each computational problem with sympy. 'manual' problems are skipped (reported as a count).

Kinds:
  solve        : eq "lhs=rhs", var, answer (comma-separated for multiple roots)
  eval         : expr (pure number), answer
  simplify     : expr, answer  (algebraic equality)
  expand       : expr, answer  (algebraic equality)
  factor_check : expr, answer  (expand(answer) == expand(expr))
  manual       : skipped
"""
import json
import glob
import os
import sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))


def P(s):
    """Parse a string to a sympy expression with rationalized numbers and real symbols.

    Uses sympify(rational=True) so float literals like 1.1 become exact Rationals
    (11/10), avoiding floating-point comparison artifacts. Expressions use explicit
    '*' for multiplication (per the author guide), so implicit-multiplication parsing
    is unnecessary.
    """
    e = sp.sympify(str(s), rational=True)
    # make all free symbols real (helps Abs / inequalities / radicals)
    reps = {sym: sp.Symbol(sym.name, real=True) for sym in e.free_symbols}
    return e.xreplace(reps)


def zero(expr):
    return sp.simplify(sp.expand(expr)) == 0


def check_solve(prob):
    lhs, rhs = prob["eq"].split("=")
    var = sp.Symbol(prob["var"], real=True)
    eq = sp.Eq(P(lhs), P(rhs))
    got = sp.solve(eq, var)
    got = [sp.simplify(g) for g in got]
    expected = [P(a) for a in str(prob["answer"]).split(",")]
    # set equality (ignoring multiplicity/order)
    def match(e):
        return any(zero(e - g) for g in got)
    def back(g):
        return any(zero(g - e) for e in expected)
    ok = all(match(e) for e in expected) and all(back(g) for g in got)
    return ok, f"solve {prob['eq']} -> got {got}, expected {expected}"


def check_eval(prob):
    ok = zero(P(prob["expr"]) - P(prob["answer"]))
    return ok, f"eval {prob['expr']} =? {prob['answer']}"


def check_equal(prob):  # simplify / expand
    ok = zero(P(prob["expr"]) - P(prob["answer"]))
    return ok, f"{prob['kind']} {prob['expr']} =? {prob['answer']}"


def check_factor(prob):
    ok = zero(sp.expand(P(prob["answer"])) - sp.expand(P(prob["expr"])))
    return ok, f"factor_check {prob['expr']} <- {prob['answer']}"


CHECKERS = {
    "solve": check_solve,
    "eval": check_eval,
    "simplify": check_equal,
    "expand": check_equal,
    "factor_check": check_factor,
}


def main():
    files = sorted(glob.glob(os.path.join(HERE, "unit-*.json"))) + \
            sorted(glob.glob(os.path.join(HERE, "appendix*.json")))
    total = auto = manual = failed = 0
    seen_ids = {}
    failures = []
    dup_ids = []

    for fp in files:
        with open(fp, encoding="utf-8") as f:
            data = json.load(f)
        for prob in data["problems"]:
            total += 1
            pid = prob.get("id", "<no-id>")
            key = (os.path.basename(fp), pid)
            if pid in seen_ids and seen_ids[pid] != os.path.basename(fp):
                pass  # ids only need to be unique within a file; cross-file reuse is fine
            kind = prob["kind"]
            if kind == "manual":
                manual += 1
                continue
            auto += 1
            checker = CHECKERS.get(kind)
            if checker is None:
                failed += 1
                failures.append((os.path.basename(fp), pid, f"unknown kind '{kind}'"))
                continue
            try:
                ok, desc = checker(prob)
                if not ok:
                    failed += 1
                    failures.append((os.path.basename(fp), pid, desc))
            except Exception as e:  # noqa
                failed += 1
                failures.append((os.path.basename(fp), pid, f"ERROR {type(e).__name__}: {e}"))

    print(f"Files checked: {len(files)}")
    print(f"Total problems: {total}  |  auto-checked: {auto}  |  manual (skipped): {manual}")
    print(f"Failures: {failed}")
    if failures:
        print("\n--- FAILURES ---")
        for fn, pid, desc in failures:
            print(f"  [{fn}] {pid}: {desc}")
        sys.exit(1)
    print("\nAll auto-checkable answers verified correct. [OK]")


if __name__ == "__main__":
    main()
