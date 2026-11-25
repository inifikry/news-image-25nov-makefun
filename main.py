#!/usr/bin/env python3
"""Entry for news-image-20261125: copy the front page to /output/entry.png.

The image (frontpage.png, drawn by draw_frontpage.py from news first
reported on Wednesday 25 November 2026) ships in this repository, so the
program needs no network: it just copies the file to the output directory.
Standard library only.
"""
import hashlib
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "frontpage.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    with open(dst, "rb") as fh:
        data = fh.read()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise SystemExit("entry.png is not a PNG file")
    print("wrote", dst, len(data), "bytes",
          "sha256", hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    sys.exit(main())
