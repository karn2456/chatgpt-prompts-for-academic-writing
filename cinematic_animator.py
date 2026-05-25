#!/usr/bin/env python3
"""
Cinematic aviation animation pipeline.
Applies 2026 color grade, Ken Burns pan, jet silhouette + neon gold trails.
"""

import math
import os
import subprocess
import tempfile

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageSequence

SRC = "/root/.claude/uploads/63820127-4dac-4a44-aeb2-31c26aef3527/cc3dac24-GIF_20260525_112620_077.gif"
OUT_GIF = "/home/user/chatgpt-prompts-for-academic-writing/cinematic_aviation.gif"
OUT_MP4 = "/home/user/chatgpt-prompts-for-academic-writing/cinematic_aviation.mp4"
FRAMES_DIR = tempfile.mkdtemp(prefix="cin_frames_")

# ── Output canvas ────────────────────────────────────────────────────────────
W, H = 1280, 720          # 16:9 cinematic output
FPS = 24
TOTAL_FRAMES = 144        # 6 seconds × 24 fps (slow-motion stretch of 58 src frames)

# ── Color palette ────────────────────────────────────────────────────────────
AV_BLUE   = np.array([10,  35,  75],  dtype=np.float32)   # deep aviation blue (shadows)
VIN_CREAM = np.array([245, 230, 195], dtype=np.float32)   # vintage cream (highlights)
GOLD      = np.array([255, 200,  50], dtype=np.float32)   # neon gold trails
SKY_MID   = np.array([25,  70, 130],  dtype=np.float32)   # mid-tone sky blue


# ════════════════════════════════════════════════════════════════════════════
# Frame extraction
# ════════════════════════════════════════════════════════════════════════════
def load_source_frames():
    img = Image.open(SRC)
    frames = []
    for f in ImageSequence.Iterator(img):
        frames.append(f.convert("RGB"))
    print(f"Loaded {len(frames)} source frames @ {img.size}")
    return frames


# ════════════════════════════════════════════════════════════════════════════
# Color grading
# ════════════════════════════════════════════════════════════════════════════
def grade(arr: np.ndarray) -> np.ndarray:
    """
    Cinematic 2026 grade:
      - Map luminance: shadows → aviation blue, highlights → vintage cream
      - Boost contrast via S-curve
      - Teal-orange style: push shadows blue, mids sky, highlights cream
    """
    f = arr.astype(np.float32) / 255.0

    # Luminance
    lum = 0.2126 * f[..., 0] + 0.7152 * f[..., 1] + 0.0722 * f[..., 2]

    # S-curve contrast
    lum_c = np.where(lum < 0.5,
                     2 * lum ** 2,
                     1 - 2 * (1 - lum) ** 2)

    # Tri-tone colour blend: shadow/mid/highlight
    shadow_w    = np.clip(1.0 - lum_c * 2.5, 0, 1)[..., np.newaxis]
    highlight_w = np.clip((lum_c - 0.55) * 2.5, 0, 1)[..., np.newaxis]
    mid_w       = np.clip(1.0 - shadow_w[..., 0] - highlight_w[..., 0], 0, 1)[..., np.newaxis]

    colour = (
        shadow_w    * (AV_BLUE   / 255.0) +
        mid_w       * (SKY_MID   / 255.0) +
        highlight_w * (VIN_CREAM / 255.0)
    )

    # Blend original with grade (80% grade influence to preserve faces/details)
    blended = f * 0.38 + colour * 0.62

    # Saturation boost on original channels (keep skin detail readable)
    mean = blended.mean(axis=2, keepdims=True)
    blended = mean + (blended - mean) * 1.35

    return np.clip(blended * 255, 0, 255).astype(np.uint8)


# ════════════════════════════════════════════════════════════════════════════
# Ken Burns slow pan + zoom
# ════════════════════════════════════════════════════════════════════════════
def ken_burns(src_img: Image.Image, t: float) -> Image.Image:
    """
    t ∈ [0,1]: slow diagonal pan left→right with gentle zoom-in.
    Source is scaled to fill canvas then cropped with sliding window.
    """
    sw, sh = src_img.size
    # Scale to fill output height with 15% extra room for panning
    scale = (H / sh) * 1.18
    nw = int(sw * scale)
    nh = int(sh * scale)
    resized = src_img.resize((nw, nh), Image.LANCZOS)

    # Zoom: 1.0 → 1.08 over the clip
    zoom = 1.0 + 0.08 * t
    zw = int(nw * zoom)
    zh = int(nh * zoom)
    zoomed = resized.resize((zw, zh), Image.LANCZOS)

    # Pan: move left-to-right diagonally
    max_dx = zw - W
    max_dy = zh - H
    x = int(max_dx * t * 0.6)         # 60% of available horizontal travel
    y = int(max_dy * (0.5 - t * 0.25))  # slight vertical drift
    x = max(0, min(x, max(0, max_dx)))
    y = max(0, min(y, max(0, max_dy)))

    return zoomed.crop((x, y, x + W, y + H))


# ════════════════════════════════════════════════════════════════════════════
# Jet silhouette drawing
# ════════════════════════════════════════════════════════════════════════════
def build_jet_mask(w: int, h: int, cx: float, cy: float, scale: float) -> Image.Image:
    """Draw a sleek modern commercial jet silhouette (pure black alpha mask)."""
    mask = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(mask)
    s = scale

    # Fuselage – elongated teardrop tilted ~-20°
    def pt(rx, ry):
        ang = math.radians(-20)
        x = rx * math.cos(ang) - ry * math.sin(ang)
        y = rx * math.sin(ang) + ry * math.cos(ang)
        return (int(cx + x * s), int(cy + y * s))

    fuse = [
        pt(-160,  0), pt(-140,-10), pt(-100,-14), pt(-40,-16),
        pt(  0, -16), pt( 80,-12), pt(140, -6), pt(160,  0),
        pt(140,   6), pt( 80,  12), pt(  0,  16), pt(-40,  16),
        pt(-100,  14), pt(-140, 10),
    ]
    d.polygon(fuse, fill=(20, 20, 20, 255))

    # Main wing sweep
    wing = [
        pt(-20, -16), pt( 60,-16), pt(130,-80), pt(145,-85),
        pt(130,-60),  pt( 50,  0), pt( 60, 16), pt(-20,  16),
    ]
    d.polygon(wing, fill=(15, 15, 15, 245))

    # Left wing (mirror)
    lwing = [
        pt(-20, -16), pt(-20, 16), pt(-50, 70), pt(-60, 78),
        pt(-48,  55), pt(-25, 20), pt(-25,-20),
    ]
    d.polygon(lwing, fill=(15, 15, 15, 245))

    # Tail fin (vertical)
    vtail = [
        pt(120,  -6), pt(130, -6), pt(160,-55), pt(155,-55), pt(120,-10),
    ]
    d.polygon(vtail, fill=(18, 18, 18, 240))

    # Horizontal stabilizer
    htail_r = [pt(125,-6), pt(140,-6), pt(158,-32), pt(150,-32), pt(128,-8)]
    htail_l = [pt(125, 6), pt(140, 6), pt(158, 32), pt(150, 32), pt(128,  8)]
    d.polygon(htail_r, fill=(18, 18, 18, 240))
    d.polygon(htail_l, fill=(18, 18, 18, 240))

    # Engine pods (two, slung below main wing)
    for ex, ey in [( 10, 28), ( 60, 48)]:
        eng = [pt(ex-35, ey), pt(ex-30, ey-8), pt(ex+35, ey-8),
               pt(ex+35, ey+8), pt(ex-30, ey+8)]
        d.polygon(eng, fill=(30, 30, 30, 240))

    return mask


def draw_jet(canvas: Image.Image, t: float) -> None:
    """
    Composite the jet onto the canvas, animating it soaring upward.
    t ∈ [0,1]: jet enters from bottom-center and arcs upward.
    """
    # Entry arc: starts below frame, rises through center
    if t < 0.15:
        return   # brief title hold before jet appears
    t2 = (t - 0.15) / 0.85  # normalise to jet's own timeline

    # Position: bottom-center → upper-center-right
    base_x = W * 0.45
    base_y = H * 1.15 - t2 * H * 1.35   # rises from below
    scale = 0.8 + t2 * 0.35              # grows as it approaches camera

    mask = build_jet_mask(W, H, base_x, base_y, scale)
    canvas.alpha_composite(mask)


# ════════════════════════════════════════════════════════════════════════════
# Neon gold light trails
# ════════════════════════════════════════════════════════════════════════════
def draw_trails(canvas: Image.Image, t: float) -> None:
    if t < 0.15:
        return
    t2 = (t - 0.15) / 0.85

    base_x = int(W * 0.45)
    base_y = int(H * 1.15 - t2 * H * 1.35)
    scale = 0.8 + t2 * 0.35

    trail_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    td = ImageDraw.Draw(trail_layer)

    ang = math.radians(-20)

    def jpt(rx, ry):
        x = rx * math.cos(ang) - ry * math.sin(ang)
        y = rx * math.sin(ang) + ry * math.cos(ang)
        return (int(base_x + x * scale), int(base_y + y * scale))

    # Multiple glowing trail stripes behind the engines
    trail_len = int(280 * scale * t2)
    for i, (ex, ey) in enumerate([(10, 28), (60, 48), (-10, -5)]):
        tip = jpt(ex - 40, ey)
        end = (tip[0] - trail_len, tip[1] + int(trail_len * 0.35))

        for width, alpha in [(18, 35), (10, 70), (5, 130), (2, 220)]:
            opacity = min(255, int(alpha * t2))
            td.line([tip, end], fill=(255, 195, 40, opacity), width=width)

        # Bright core
        td.line([tip, (tip[0] - trail_len // 2, tip[1] + trail_len // 6)],
                fill=(255, 240, 160, min(255, int(200 * t2))), width=2)

    # Gaussian glow
    blurred = trail_layer.filter(ImageFilter.GaussianBlur(radius=6))
    canvas.alpha_composite(blurred)
    canvas.alpha_composite(trail_layer)  # sharp core on top


# ════════════════════════════════════════════════════════════════════════════
# Vignette + film grain
# ════════════════════════════════════════════════════════════════════════════
def add_vignette(canvas: Image.Image, strength: float = 0.55) -> None:
    vig = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(vig)
    cx, cy = W // 2, H // 2
    steps = 60
    for i in range(steps, 0, -1):
        r = int(255 * strength * (1 - i / steps) ** 1.8)
        frac = i / steps
        bx = int(cx * (1 - frac))
        by = int(cy * (1 - frac))
        d.ellipse([bx, by, W - bx, H - by], fill=(0, 0, 0, r))
    vig_blur = vig.filter(ImageFilter.GaussianBlur(radius=W // 8))
    canvas.alpha_composite(vig_blur)


def add_grain(canvas: Image.Image, amount: float = 12.0) -> None:
    arr = np.array(canvas)
    noise = np.random.normal(0, amount, arr.shape[:2]).astype(np.int16)
    arr[..., :3] = np.clip(arr[..., :3].astype(np.int16) + noise[..., np.newaxis], 0, 255).astype(np.uint8)
    canvas.paste(Image.fromarray(arr))


# ════════════════════════════════════════════════════════════════════════════
# Letterbox bars
# ════════════════════════════════════════════════════════════════════════════
def add_letterbox(canvas: Image.Image, bar_h: int = 42) -> None:
    d = ImageDraw.Draw(canvas)
    d.rectangle([0, 0, W, bar_h], fill=(0, 0, 0))
    d.rectangle([0, H - bar_h, W, H], fill=(0, 0, 0))


# ════════════════════════════════════════════════════════════════════════════
# Title card overlay (first 18 frames = 0.75 s)
# ════════════════════════════════════════════════════════════════════════════
def add_title_card(canvas: Image.Image, t: float) -> None:
    if t > 0.14:
        return
    alpha = int(255 * (1.0 - t / 0.14))
    overlay = Image.new("RGBA", canvas.size, (8, 25, 58, alpha))
    canvas.alpha_composite(overlay)


# ════════════════════════════════════════════════════════════════════════════
# Main render loop
# ════════════════════════════════════════════════════════════════════════════
def render():
    print("Loading source frames …")
    src_frames = load_source_frames()
    n_src = len(src_frames)

    print(f"Rendering {TOTAL_FRAMES} output frames at {W}×{H} …")
    out_frames = []

    for i in range(TOTAL_FRAMES):
        t = i / (TOTAL_FRAMES - 1)

        # Map to source frame with slow-motion stretch
        src_idx = int(t * (n_src - 1))
        src_img = src_frames[src_idx]

        # ── 1. Ken Burns pan/zoom ──────────────────────────────────────────
        panned = ken_burns(src_img, t)

        # ── 2. Colour grade ───────────────────────────────────────────────
        arr = grade(np.array(panned))
        canvas = Image.fromarray(arr).convert("RGBA")

        # ── 3. Title card fade ────────────────────────────────────────────
        add_title_card(canvas, t)

        # ── 4. Light trails ───────────────────────────────────────────────
        draw_trails(canvas, t)

        # ── 5. Jet silhouette ─────────────────────────────────────────────
        draw_jet(canvas, t)

        # ── 6. Vignette ───────────────────────────────────────────────────
        add_vignette(canvas, 0.5)

        # ── 7. Letterbox ─────────────────────────────────────────────────
        add_letterbox(canvas, bar_h=44)

        # ── 8. Film grain ─────────────────────────────────────────────────
        add_grain(canvas, 9.0)

        frame_rgb = canvas.convert("RGB")

        # Save PNG for ffmpeg
        frame_path = os.path.join(FRAMES_DIR, f"frame_{i:05d}.png")
        frame_rgb.save(frame_path)

        out_frames.append(canvas.convert("P", palette=Image.ADAPTIVE, colors=256))

        if i % 24 == 0:
            print(f"  frame {i+1}/{TOTAL_FRAMES}  t={t:.3f}")

    # ── Export GIF ────────────────────────────────────────────────────────
    print("Saving GIF …")
    out_frames[0].save(
        OUT_GIF,
        save_all=True,
        append_images=out_frames[1:],
        loop=0,
        duration=int(1000 / FPS),
        optimize=False,
    )
    print(f"GIF saved → {OUT_GIF}  ({os.path.getsize(OUT_GIF)//1024} KB)")

    # ── Export MP4 via ffmpeg ─────────────────────────────────────────────
    print("Encoding MP4 …")
    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", os.path.join(FRAMES_DIR, "frame_%05d.png"),
        "-c:v", "libx264",
        "-preset", "slow",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-vf", "scale=1280:720",
        OUT_MP4,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"MP4 saved → {OUT_MP4}  ({os.path.getsize(OUT_MP4)//1024} KB)")
    else:
        print("ffmpeg error:", result.stderr[-500:])

    print("\nDone.")


if __name__ == "__main__":
    render()
