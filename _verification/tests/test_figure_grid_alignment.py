# Regression guard for the figure-grid misalignment bug.
#
# Bug: figures sat on a CSS background grid (figure.fig {background-size:22px}) that was a
# separate, scaled coordinate system from the inline SVG, so a point at (3,2) rendered near
# (5,3) on the unrelated grid. CI never caught it because figures.py --check only validates the
# SVG's own coordinates, not its alignment with the CSS background.
#
# Fix: the grid is now drawn INSIDE the SVG with the same mapper as the axes/points, so a point
# always lands exactly on a grid crossing; the CSS background grid was removed.
import os, re

HERE = os.path.dirname(__file__)
FIG_DIR = os.path.join(HERE, "..", "..", "algebra-1-tutor", "figures")
GRID = "#e8e8e8"


def _svg(code):
    return open(os.path.join(FIG_DIR, code + ".svg"), encoding="utf-8").read()


def test_plotted_point_lands_on_a_grid_crossing():
    # 4.1.f2 plots (3, 2): the dot must sit on the intersection of a drawn vertical and
    # horizontal gridline (same pixel column/row), proving grid and point share one lattice.
    svg = _svg("4.1.f2")
    dot = re.search(r'<circle cx="([\d.]+)" cy="([\d.]+)"', svg)
    assert dot, "no plotted point in 4.1.f2"
    cx, cy = dot.group(1), dot.group(2)
    assert re.search(rf'<line x1="{re.escape(cx)}" y1="[\d.]+" x2="{re.escape(cx)}" y2="[\d.]+" stroke="{GRID}"', svg), \
        f"no vertical gridline at the point's column x={cx} (point is off the grid)"
    assert re.search(rf'<line x1="[\d.]+" y1="{re.escape(cy)}" x2="[\d.]+" y2="{re.escape(cy)}" stroke="{GRID}"', svg), \
        f"no horizontal gridline at the point's row y={cy} (point is off the grid)"


def test_plane_figures_draw_their_own_grid():
    for code in ("4.1.f1", "4.1.f3", "4.1.f5", "5.1.f1"):
        assert GRID in _svg(code), f"{code} has no in-SVG grid (relying on a CSS background grid again?)"


def test_number_line_figures_have_no_2d_grid():
    # 1D number lines must not gain a 2D grid.
    assert GRID not in _svg("1.2.f1")


def test_no_css_background_grid_in_built_pages():
    # The misaligned CSS background grid must stay removed from generated output.
    page = os.path.join(HERE, "..", "..", "docs", "textbook", "unit-04-1.html")
    html = open(page, encoding="utf-8").read()
    assert "background-size:22px" not in html, "the misaligned CSS background grid is back"
