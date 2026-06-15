# Security Policy

This project is a static educational website (served via GitHub Pages) plus
Python build-and-verification tooling. It has no server, no database, no user
accounts, and collects no data at runtime.

## Reporting a vulnerability or concern

Please report security issues privately rather than opening a public issue:

- Preferred: open a private report through GitHub's **Security → Advisories →
  "Report a vulnerability"** flow:
  https://github.com/RealRogerWinter/algebra-1-tutor/security/advisories/new
- For anything else sensitive, contact the maintainer through GitHub
  (@RealRogerWinter).

We aim to acknowledge a report within about a week.

## Scope notes

- The image-generation helper (`_verification/gen_illustration.py`) reads a
  Google Gemini API key only from a local, git-ignored location: the
  `--api-key` flag, the file `_imgwork/gemini.key`, or the `GEMINI_API_KEY`
  environment variable. No key is committed, and `*.key` and `_imgwork/` are
  git-ignored.
- The generated site loads KaTeX and web fonts from public CDNs (jsDelivr,
  Google Fonts). It includes no analytics and no trackers.

## Supported versions

Only the current `main` branch — and the live site built from it — is supported.
