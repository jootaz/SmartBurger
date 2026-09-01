#!/usr/bin/env python3
"""Gera a versao de arquivo unico, com as imagens embutidas em base64.

    python build/inline.py

Escreve dist/index-arquivo-unico.html. Serve para enviar a previa por e-mail
ou WhatsApp, onde uma pasta img/ separada se perderia.
"""
import base64
import mimetypes
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "index.html"
DEST = ROOT / "dist" / "index-arquivo-unico.html"


def main() -> int:
    if not SRC.exists():
        print("nao encontrei", SRC, file=sys.stderr)
        return 1

    html = SRC.read_text(encoding="utf-8")
    faltando = []

    def embed(match: re.Match) -> str:
        rel = match.group("path")
        img = ROOT / rel
        if not img.exists():
            faltando.append(rel)
            return match.group(0)
        mime = mimetypes.guess_type(img.name)[0] or "image/jpeg"
        b64 = base64.b64encode(img.read_bytes()).decode("ascii")
        return f'{match.group("pre")}data:{mime};base64,{b64}"'

    out = re.sub(
        r'(?P<pre>src=")(?P<path>img/[^"]+)"',
        embed,
        html,
    )

    if faltando:
        print("imagens faltando:", ", ".join(faltando), file=sys.stderr)
        return 1

    DEST.parent.mkdir(exist_ok=True)
    DEST.write_text(out, encoding="utf-8")
    print(f"{DEST.relative_to(ROOT)} — {DEST.stat().st_size / 1_048_576:.1f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
