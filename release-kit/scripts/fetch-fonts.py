#!/usr/bin/env python3
"""Fetch Google Fonts as base64-embedded @font-face rules (latin subset only).

Usage:
  python3 fetch-fonts.py <out.css> "<Family>:wght@<w>;<w>" ["<Family2>:wght@..." ...]

Example:
  python3 fetch-fonts.py fonts.css "Inter:wght@400;500;600" "Inter Tight:wght@500;600;700"

Writes @font-face rules using data: URIs so the resulting HTML/PDF is fully self-contained
and renders identically offline. Only the latin block (U+0000-00FF) is embedded per weight,
so each face is ~45KB rather than the full multi-subset file.

Paste the output at the top of your <style> (or use embed.py to inject it into a /*FONTS*/ marker).
"""
import sys, re, base64, urllib.request, urllib.parse

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    out = sys.argv[1]
    families = sys.argv[2:]
    q = "&".join("family=" + urllib.parse.quote(f, safe=":;@") for f in families)
    css_url = f"https://fonts.googleapis.com/css2?{q}&display=swap"
    req = urllib.request.Request(css_url, headers={"User-Agent": UA})
    css = urllib.request.urlopen(req).read().decode()

    blocks = re.findall(r'@font-face\s*\{(.*?)\}', css, re.S)
    want = {}  # (family, weight) -> url, latin only
    for b in blocks:
        fam = re.search(r"font-family:\s*'([^']+)'", b)
        wt  = re.search(r"font-weight:\s*(\d+)", b)
        ur  = re.search(r"unicode-range:\s*([^;]+);", b)
        url = re.search(r"src:\s*url\(([^)]+)\)", b)
        if fam and wt and ur and url and "U+0000-00FF" in ur.group(1):
            want[(fam.group(1), wt.group(1))] = url.group(1)

    if not want:
        print("ERROR: no latin @font-face blocks found — check family/weight spec", file=sys.stderr)
        sys.exit(2)

    faces = []
    for (fam, wt), url in sorted(want.items()):
        data = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA})).read()
        b64 = base64.b64encode(data).decode()
        faces.append(
            f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{wt};"
            f"font-display:swap;src:url(data:font/woff2;base64,{b64}) format('woff2');}}")
        print(f"  embedded {fam} {wt}  ({len(data)//1024}KB)", file=sys.stderr)

    with open(out, "w") as f:
        f.write("\n".join(faces))
    print(f"wrote {out}: {len(faces)} faces, {sum(len(x) for x in faces)//1024}KB", file=sys.stderr)

if __name__ == "__main__":
    main()
