"""Generate a single warm illustration via the Gemini REST image API (build tooling, NOT shipped,
NOT a CI gate). The image PNGs/JPGs it writes are committed as static assets; this script is never
run by CI, so its non-determinism is fine.

Auth: query-param `?key=` (the working method for the provided key). The key is resolved from, in
order: --api-key, $GEMINI_API_KEY, then the gitignored file _imgwork/gemini.key. Never hard-code or
commit the key.

Usage (prompt as an arg OR, preferred for long prompts, from a file to dodge shell quoting):
  python _verification/gen_illustration.py --out docs/assets/u1-1-hero.jpg --prompt "..."
  python _verification/gen_illustration.py --out docs/assets/u1-1-hero.jpg --prompt-file p.txt

Exit 0 on success (prints saved path + size). Non-zero on any error (prints the API diagnostic:
a safety block, an empty/text-only response, or an HTTP error).
"""
import argparse, base64, json, os, sys, time, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
KEY_FILE = os.path.join(REPO_ROOT, "_imgwork", "gemini.key")
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
DEFAULT_MODEL = "gemini-2.5-flash-image"


def _resolve_key(cli_key):
    # The deliberately-placed key file wins over $GEMINI_API_KEY, which on this machine holds a
    # stale/invalid AIza key. Order: --api-key, then _imgwork/gemini.key, then the env var.
    if cli_key:
        return cli_key.strip()
    if os.path.exists(KEY_FILE):
        k = open(KEY_FILE, encoding="utf-8").read().strip()
        if k:
            return k
    env = os.environ.get("GEMINI_API_KEY")
    if env and env.strip():
        return env.strip()
    return None


def _post(model, key, prompt, aspect=None, timeout=180):
    gen = {"responseModalities": ["IMAGE"]}
    if aspect:
        gen["imageConfig"] = {"aspectRatio": aspect}
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": gen,
    }).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT.format(model=model, key=key),
        data=body, headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def _extract_image(resp):
    for cand in resp.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                return base64.b64decode(inline["data"])
    return None


def _save(raw, out):
    """Write raw bytes, or re-encode to a lean JPEG when out is .jpg/.jpeg and Pillow is available
    (matches the existing docs/assets/*.jpg heroes; keeps the repo + site light)."""
    if out.lower().endswith((".jpg", ".jpeg")):
        try:
            import io
            from PIL import Image
            im = Image.open(io.BytesIO(raw)).convert("RGB")
            if im.width > 1200:
                im = im.resize((1200, round(im.height * 1200 / im.width)), Image.LANCZOS)
            im.save(out, "JPEG", quality=82, optimize=True, progressive=True)
            return
        except Exception as e:
            sys.stderr.write(f"(Pillow re-encode failed: {e}; writing raw bytes)\n")
    with open(out, "wb") as f:
        f.write(raw)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--prompt")
    ap.add_argument("--prompt-file")
    ap.add_argument("--api-key")
    ap.add_argument("--aspect", help='e.g. "16:9" (heroes), "4:3"/"1:1" (inline). Omit for default.')
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--retries", type=int, default=3)
    a = ap.parse_args(argv)

    key = _resolve_key(a.api_key)
    if not key:
        print("ERROR: no API key (--api-key, $GEMINI_API_KEY, or _imgwork/gemini.key)", file=sys.stderr)
        return 2
    prompt = open(a.prompt_file, encoding="utf-8").read() if a.prompt_file else a.prompt
    if not prompt or not prompt.strip():
        print("ERROR: empty prompt", file=sys.stderr); return 2

    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    last = ""
    for attempt in range(1, a.retries + 1):
        try:
            resp = _post(a.model, key, prompt, aspect=a.aspect)
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:400]}"
        except Exception as e:
            last = f"{type(e).__name__}: {e}"
        else:
            img = _extract_image(resp)
            if img:
                _save(img, a.out)
                print(f"OK {a.out} ({len(img)} raw bytes -> {os.path.getsize(a.out)} on disk)")
                return 0
            last = "no inlineData in response: " + json.dumps(resp)[:400]
        if attempt < a.retries:
            time.sleep(2 * attempt)
    print(f"ERROR after {a.retries} attempt(s): {last}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
