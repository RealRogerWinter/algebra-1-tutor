# Image assets

This folder holds the raster artwork for the generated website — per-lesson
hero images and inline concept illustrations — plus a few shared site images.

## Provenance and license

The hero and illustration JPEGs (`hero-*.jpg`, `illus-*.jpg`, and the small set
of named concept images) were generated with Google's Gemini image model
("nano-banana", `gemini-2.5-flash-image`) for this project. Because purely
AI-generated images generally are not subject to copyright, they are released as
**CC0 1.0** (public domain dedication): <https://creativecommons.org/publicdomain/zero/1.0/>.
No rights are asserted over them.

These images are decorative. Every *mathematical* figure in the course (graphs,
number lines, parabolas, scatter plots) is a separate, computed, sympy-checked
SVG under `algebra-1-tutor/figures/` — not a raster image here.

## Third-party rendering libraries (not stored here)

The site loads these from public CDNs; they are not redistributed in this repo:

- **KaTeX** (MIT) — math rendering
- **Google Fonts**: Fraunces, Source Serif 4, IBM Plex Mono (SIL Open Font License)
