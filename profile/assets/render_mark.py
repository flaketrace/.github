"""Render the flaketrace mark to PNG with real alpha.

qlmanage bakes an opaque white background into its SVG previews, which reads as
"transparent" on GitHub's light theme and as a white box on dark. Drawing the
geometry directly is the only way to get a genuine alpha channel here, and it
keeps the PNG byte-identical in intent to profile/assets/mark.svg.

Geometry is in the same 64-unit space as the SVG:
  slate polyline  (4,46) (12,43) (20,47) (28,44) (34,15) (40,46) (48,42) (56,46) (60,44)
  green overdraw  (28,44) (34,15) (40,46)
  stroke 3.6, round caps and joins
"""

import sys
from PIL import Image, ImageDraw

SLATE = (92, 104, 115, 255)  # #5c6873
GREEN = (63, 185, 80, 255)  # #3fb950

BASE = [(4, 46), (12, 43), (20, 47), (28, 44), (34, 15), (40, 46), (48, 42), (56, 46), (60, 44)]
SPIKE = [(28, 44), (34, 15), (40, 46)]
STROKE = 3.6

SS = 12  # supersample factor; downscaled with LANCZOS for antialiasing


def draw_polyline(d, pts, colour, width):
    """Thick polyline with round caps and joins — PIL has no stroke-linejoin."""
    w = width * SS
    scaled = [(x * SS, y * SS) for x, y in pts]
    d.line(scaled, fill=colour, width=int(round(w)))
    r = w / 2.0
    for x, y in scaled:  # discs at every vertex give the round join/cap
        d.ellipse((x - r, y - r, x + r, y + r), fill=colour)


def main(out_path, target_width):
    size = 64 * SS
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    draw_polyline(d, BASE, SLATE, STROKE)
    draw_polyline(d, SPIKE, GREEN, STROKE)

    bbox = im.getbbox()
    if bbox is None:
        raise SystemExit("nothing drawn")
    pad = int(2 * SS)
    l, t, r, b = bbox
    im = im.crop(
        (max(0, l - pad), max(0, t - pad), min(im.width, r + pad), min(im.height, b + pad))
    )

    h = round(target_width * im.height / im.width)
    im = im.resize((target_width, h), Image.LANCZOS)
    im.save(out_path)
    print(f"{out_path}  {im.width}x{im.height}  aspect {im.width / im.height:.2f}")

    corner = im.getpixel((0, 0))
    print("corner pixel (must be alpha 0):", corner)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
