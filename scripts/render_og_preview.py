"""Generate the social-preview image using the site's exact approved logo artwork.

The wordmark is taken as pixels from assets/img/brand/logo.webp, not
recreated with different fonts or spacing.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import shutil

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "img/brand/logo.webp"
OUTPUT = ASSETS / "og-preview-v2.png"
PREVIOUS = ASSETS / "og-preview.png"
W, H = 1200, 630
BG = (5, 5, 5)
FG = (248, 248, 248)

def sans(size):
    for filename in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ):
        if Path(filename).exists():
            return ImageFont.truetype(filename, size)
    raise FileNotFoundError("Sans-serif font unavailable on build runner")

def render():
    if not SOURCE.exists():
        raise FileNotFoundError("Approved brand file not found: " + str(SOURCE))
    canvas = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(canvas)
    regular = sans(20)

    # Corner inscriptions: same non-italic, modern sans font and size.
    draw.text((60, 59), "Security Study Archive", font=regular, fill=FG, anchor="lt")

    source = Image.open(SOURCE).convert("RGBA")
    # The original brand image has the wordmark above a secondary subtitle.
    # Crop the subtitle out, preserving the original mixed-face wordmark.
    top = source.crop((0, 0, source.width, round(source.height * 0.76)))
    alpha = top.getchannel("A")
    if alpha.getextrema()[0] == 0:
        mask = alpha
    else:
        mask = ImageOps.invert(ImageOps.grayscale(top.convert("RGB")))
    mask = mask.point(lambda value: max(0, value - 16) * 255 // 239)
    bbox = mask.point(lambda value: 255 if value > 23 else 0).getbbox()
    if not bbox:
        raise ValueError("Unable to locate approved wordmark pixels")
    mask = mask.crop(bbox)

    wordmark_width = 570
    logo_height = round(wordmark_width * mask.height / mask.width)
    mask = mask.resize((wordmark_width, logo_height), Image.Resampling.LANCZOS)
    canvas.paste(FG, ((W - wordmark_width) // 2, 260), mask)

    draw.text((W // 2, 351), "bysumcookies.github.io", font=sans(19), fill=FG, anchor="mt")
    draw.text((1140, 498), "Byte by byte,", font=regular, fill=FG, anchor="rt")
    draw.text((1140, 531), "building security.", font=regular, fill=FG, anchor="rt")

    canvas.save(OUTPUT, format="PNG", optimize=True)
    with Image.open(OUTPUT) as check:
        check.verify()
    with Image.open(OUTPUT) as check:
        assert check.size == (1200, 630) and check.format == "PNG"
    # Repair the formerly damaged old path as well, for existing clients.
    shutil.copyfile(OUTPUT, PREVIOUS)
    print("OG preview validated:", OUTPUT, OUTPUT.stat().st_size, "bytes")
if __name__ == "__main__":
    render()
