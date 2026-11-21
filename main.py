import os
import struct
import zlib


def chunk(kind, data):
    body = struct.pack(">I", len(data)) + kind + data
    return body + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "assets", "poster.rgb.z"), "rb") as f:
        raw = zlib.decompress(f.read())
    width = 1024
    height = 1024
    stride = width * 3
    rows = bytearray()
    for y in range(height):
        rows.append(0)
        rows += raw[y * stride:(y + 1) * stride]
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", ihdr)
    comp = zlib.compressobj(9)
    idat = comp.compress(bytes(rows)) + comp.flush()
    for i in range(0, len(idat), 65536):
        png += chunk(b"IDAT", idat[i:i + 65536])
    png += chunk(b"IEND", b"")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.png"), "wb") as f:
        f.write(png)


if __name__ == "__main__":
    main()
