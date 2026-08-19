#!/usr/bin/env python3
"""Inject embedded fonts and base64 images into a kit HTML in place.

Usage:
  python3 embed.py <file.html> [--fonts fonts.css] [--img "{{PLACEHOLDER}}=/path/to/image"] ...

- --fonts   : contents replace the first `/*FONTS*/` marker in the HTML.
- --img     : each PLACEHOLDER (e.g. {{IMG_HERO}}) is replaced everywhere with a data: URI
              for the given image file (jpg/png/webp/svg detected by extension).

Edits the file in place. Fails loudly if a placeholder or the /*FONTS*/ marker is missing,
so you never ship a kit with an unresolved {{...}} or a broken font block.
"""
import sys, base64, mimetypes, os

def data_uri(path):
    ext = os.path.splitext(path)[1].lower().lstrip(".")
    mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png",
            "webp": "image/webp", "gif": "image/gif", "svg": "image/svg+xml"}.get(
                ext, mimetypes.guess_type(path)[0] or "application/octet-stream")
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    html = sys.argv[1]
    fonts = None
    imgs = []
    a = sys.argv[2:]
    i = 0
    while i < len(a):
        if a[i] == "--fonts":
            fonts = a[i + 1]; i += 2
        elif a[i] == "--img":
            key, _, path = a[i + 1].partition("=")
            imgs.append((key, path)); i += 2
        else:
            print(f"unknown arg: {a[i]}", file=sys.stderr); sys.exit(1)

    s = open(html).read()

    if fonts:
        assert "/*FONTS*/" in s, "no /*FONTS*/ marker in HTML"
        s = s.replace("/*FONTS*/", open(fonts).read(), 1)
        print("  injected fonts", file=sys.stderr)

    for key, path in imgs:
        assert key in s, f"placeholder not found in HTML: {key}"
        s = s.replace(key, data_uri(path))
        print(f"  {key} <- {os.path.basename(path)}", file=sys.stderr)

    leftover = [k for k in ("{{IMG", "/*FONTS*/") if k in s]
    if leftover:
        print(f"WARNING: unresolved markers still present: {leftover}", file=sys.stderr)

    open(html, "w").write(s)
    print(f"wrote {html}: {len(s)//1024}KB", file=sys.stderr)

if __name__ == "__main__":
    main()
