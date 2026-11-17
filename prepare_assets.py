#!/usr/bin/env python3
"""Zet de bronbestanden (bron/, van Instagram @dehaasstyling) om naar
web-geoptimaliseerde beelden en video's in assets/. Opnieuw draaien mag altijd.

Gebruik:  python3 prepare_assets.py
Vereist:  ffmpeg + Pillow
"""
import subprocess
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
SRC_IG, SRC_REEL = ROOT / "bron/instagram", ROOT / "bron/reels"
IMG, VID = ROOT / "assets/img", ROOT / "assets/video"
IMG.mkdir(parents=True, exist_ok=True)
VID.mkdir(parents=True, exist_ok=True)


def run(*args):
    subprocess.run(args, check=True, capture_output=True)


def save_img(src: Path, name: str, size=(1200, 1500), crop=True):
    im = Image.open(src).convert("RGB")
    im = ImageOps.fit(im, size, Image.LANCZOS, centering=(0.5, 0.45)) if crop else im
    im.save(IMG / f"{name}.webp", "WEBP", quality=82, method=6)
    im.save(IMG / f"{name}.jpg", "JPEG", quality=84, optimize=True, progressive=True)


def frame(reel: str, t: float, name: str, size=(1080, 1350)):
    tmp = IMG / f"_{name}.png"
    run("ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", str(SRC_REEL / reel), "-frames:v", "1", str(tmp))
    save_img(tmp, name, size)
    tmp.unlink()


def clip(reel: str, start: float, dur: float, name: str, width=720):
    out = VID / f"{name}.mp4"
    run("ffmpeg", "-v", "error", "-y", "-ss", str(start), "-t", str(dur), "-i", str(SRC_REEL / reel),
        "-an", "-vf", f"scale={width}:-2,fps=30", "-c:v", "libx264", "-preset", "slow", "-crf", "25",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out))
    run("ffmpeg", "-v", "error", "-y", "-ss", "0.1", "-i", str(out), "-frames:v", "1", "-q:v", "3",
        str(IMG / f"{name}-poster.jpg"))


# Foto's uit posts
save_img(SRC_IG / "bibi-portret.jpg", "bibi-portret", (1000, 1250))
save_img(SRC_IG / "biab-nagels.jpg", "biab-nagels", (1000, 1250))
save_img(SRC_IG / "multizuurpeeling.jpg", "peeling", (1000, 1000))
save_img(SRC_IG / "maria-akerberg-huidadvies.jpg", "maria-akerberg", (900, 900))

# Stills uit reels
frame("reel_10_2.mp4", 0.6, "salon-ruimte")
frame("reel_08_1.mp4", 3.0, "lichttherapie")
frame("reel_09_1.mp4", 12.0, "gezichtsmassage")
frame("reel_09_1.mp4", 1.0, "inika-olie")
frame("reel_11_2.mp4", 14.0, "bibi-behandeling")
frame("reel_11_2.mp4", 2.5, "led-masker")
frame("reel_07_2.mp4", 15.8, "inika-spf", (1080, 1350))
frame("reel_06_0.mp4", 3.5, "logo-kaartjes", (1080, 1350))

# Uit de Instagram-highlights (bron/highlights, 1080x1919 stories)
HL = ROOT / "bron/highlights"


def story_crop(src: Path, name: str, box, size=(1000, 1250)):
    im = Image.open(src).convert("RGB").crop(box)
    tmp = IMG / f"_{name}.png"
    im.save(tmp)
    save_img(tmp, name, size)
    tmp.unlink()


story_crop(HL / "transformatie/01.jpg", "nagels-resultaat-1", (0, 380, 1080, 1730))
story_crop(HL / "transformatie/03.jpg", "nagels-resultaat-2", (0, 240, 1080, 1590))
story_crop(HL / "nagels-trainingsdag.jpg", "nagels-glitter", (0, 120, 1080, 1470))
story_crop(HL / "superlash/03.jpg", "superlash-voor-na", (0, 500, 1080, 1430), (1000, 861))
story_crop(HL / "superlash/00.jpg", "superlash-product", (90, 560, 1050, 1760), (1000, 1250))

# Korte, stille loops
clip("reel_11_2.mp4", 4.0, 12.0, "hero-behandeling")
clip("reel_10_2.mp4", 0.0, 8.6, "salon-tour")
clip("reel_08_1.mp4", 0.0, 6.0, "lichttherapie")
clip("reel_09_1.mp4", 6.0, 10.0, "deep-tissue")

print("Klaar:", sorted(p.name for p in (IMG.iterdir())), sorted(p.name for p in VID.iterdir()))
