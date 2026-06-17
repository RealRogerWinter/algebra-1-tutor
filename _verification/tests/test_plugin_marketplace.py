"""The Claude Code plugin marketplace manifests stay valid and never leak into the consumer .zip.

`.claude-plugin/marketplace.json` lets a Claude Code user run
    /plugin marketplace add RealRogerWinter/algebra-1-tutor
    /plugin install algebra-1-tutor@algebra-1-tutor
The skill itself (SKILL.md + references/ + figures/) is the plugin source; these tests guard that
the manifests are well-formed and that the Claude-Code-only metadata is excluded from build_skill's
uploadable package.
"""
import json, os, zipfile
import build_skill as bs

MARKETPLACE = os.path.join(bs.REPO_ROOT, ".claude-plugin", "marketplace.json")
PLUGIN = os.path.join(bs.REPO_ROOT, "algebra-1-tutor", ".claude-plugin", "plugin.json")


def _load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def test_marketplace_manifest_valid():
    m = _load(MARKETPLACE)
    assert m.get("name"), "marketplace needs a name (the id users type after @)"
    assert m.get("owner", {}).get("name"), "marketplace needs owner.name"
    plugins = m.get("plugins")
    assert isinstance(plugins, list) and plugins, "marketplace must list at least one plugin"
    p = plugins[0]
    assert p.get("name") and p.get("description")
    src = os.path.normpath(os.path.join(bs.REPO_ROOT, p["source"]))
    assert os.path.isdir(src), f"plugin source missing: {p['source']}"
    # single-skill plugin: SKILL.md sits at the plugin source root
    assert os.path.isfile(os.path.join(src, "SKILL.md")), "plugin source needs SKILL.md at its root"


def test_plugin_manifest_matches_marketplace():
    m = _load(MARKETPLACE)
    pj = _load(PLUGIN)
    assert pj.get("name") == m["plugins"][0]["name"] == "algebra-1-tutor"


def _walk_rel(skill_dir, exclude):
    """Files under skill_dir as posix-relative paths, pruning any directory named in `exclude`.
    Unlike glob('**/*'), os.walk descends into dot-prefixed dirs — so this exercises whether EXCLUDE
    (not just glob's dot-dir skip) is what keeps the manifest out."""
    out = []
    for root, dirs, files in os.walk(skill_dir):
        dirs[:] = [d for d in dirs if d not in exclude]
        for f in files:
            out.append(os.path.relpath(os.path.join(root, f), skill_dir).replace("\\", "/"))
    return out


def test_claude_plugin_never_ships_in_consumer_zip():
    # Non-vacuous: the manifest really exists in the source tree...
    assert os.path.isfile(PLUGIN), "expected algebra-1-tutor/.claude-plugin/plugin.json to exist"
    # ...yet it is absent from both the package set and the committed consumer .zip.
    packaged = [rel for rel, _ in bs._files()]
    assert packaged, "build_skill found no files"
    assert not any(".claude-plugin" in rel for rel in packaged), ".claude-plugin leaked into the package set"
    names = zipfile.ZipFile(bs.ZIP_FILE).namelist()
    assert not any(".claude-plugin" in n for n in names), ".claude-plugin leaked into the committed .zip"
    # Guard the EXCLUDE edit itself: glob('**/*') already skips dot-dirs, so EXCLUDE is the
    # defense-in-depth that stays load-bearing if the collector ever moves to os.walk.
    assert ".claude-plugin" in bs.EXCLUDE
    assert any(".claude-plugin/plugin.json" in p for p in _walk_rel(bs.SKILL_DIR, ())), "walk should see the manifest"
    assert not any(".claude-plugin" in p for p in _walk_rel(bs.SKILL_DIR, bs.EXCLUDE)), "EXCLUDE must drop it under os.walk"
