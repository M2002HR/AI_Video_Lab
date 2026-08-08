#!/usr/bin/env python3
"""Generate low-resolution Git-safe media proxies for AI Video Ad Lab.

Images require Pillow. Videos require ffmpeg in PATH.
The script never overwrites the source file.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def make_image(src: Path, dst: Path, max_edge: int = 1280, quality: int = 72) -> dict:
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise SystemExit("Pillow is required for image proxies: pip install pillow") from exc

    dst.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)
        if im.mode not in ("RGB", "RGBA"):
            im = im.convert("RGB")
        w, h = im.size
        scale = min(1.0, max_edge / max(w, h))
        if scale < 1.0:
            im = im.resize((max(1, round(w * scale)), max(1, round(h * scale))), Image.Resampling.LANCZOS)
        if im.mode == "RGBA":
            # Keep alpha only if source truly needs it; WebP supports alpha.
            save_im = im
        else:
            save_im = im.convert("RGB")
        save_im.save(dst, "WEBP", quality=quality, method=6, exif=b"")
        out_w, out_h = save_im.size

    return {
        "media_type": "image",
        "profile": f"IMG-PROXY-{max_edge}-WEBP-Q{quality}",
        "width": out_w,
        "height": out_h,
        "bytes": dst.stat().st_size,
        "source_sha256": sha256(src),
        "proxy_sha256": sha256(dst),
    }


def ffprobe_json(path: Path) -> dict:
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        return {}
    cmd = [
        ffprobe, "-v", "error", "-show_entries",
        "format=duration:stream=index,codec_type,width,height,r_frame_rate",
        "-of", "json", str(path),
    ]
    try:
        return json.loads(subprocess.check_output(cmd, text=True))
    except Exception:
        return {}


def make_video(src: Path, dst: Path, max_edge: int = 1280, crf: int = 30, fps: int = 24, audio_kbps: int = 96) -> dict:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise SystemExit("ffmpeg is required for video proxies and was not found in PATH")

    dst.parent.mkdir(parents=True, exist_ok=True)
    vf = (
        f"scale=w='min({max_edge},iw)':h='min({max_edge},ih)':"
        "force_original_aspect_ratio=decrease,"
        "scale=trunc(iw/2)*2:trunc(ih/2)*2,"
        f"fps={fps}"
    )
    cmd = [
        ffmpeg, "-y", "-i", str(src),
        "-map_metadata", "-1",
        "-vf", vf,
        "-c:v", "libx264", "-preset", "medium", "-crf", str(crf),
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", f"{audio_kbps}k",
        "-movflags", "+faststart",
        str(dst),
    ]
    subprocess.run(cmd, check=True)

    probe = ffprobe_json(dst)
    video_stream = next((s for s in probe.get("streams", []) if s.get("codec_type") == "video"), {})
    duration = None
    try:
        duration = float(probe.get("format", {}).get("duration"))
    except (TypeError, ValueError):
        pass

    return {
        "media_type": "video",
        "profile": f"VID-PROXY-H264-MAX{max_edge}-CRF{crf}-{fps}FPS",
        "width": video_stream.get("width"),
        "height": video_stream.get("height"),
        "duration_seconds": duration,
        "fps": fps,
        "bytes": dst.stat().st_size,
        "source_sha256": sha256(src),
        "proxy_sha256": sha256(dst),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate low-resolution media proxy")
    sub = ap.add_subparsers(dest="kind", required=True)

    img = sub.add_parser("image")
    img.add_argument("src", type=Path)
    img.add_argument("dst", type=Path)
    img.add_argument("--max-edge", type=int, default=1280)
    img.add_argument("--quality", type=int, default=72)

    vid = sub.add_parser("video")
    vid.add_argument("src", type=Path)
    vid.add_argument("dst", type=Path)
    vid.add_argument("--max-edge", type=int, default=1280)
    vid.add_argument("--crf", type=int, default=30)
    vid.add_argument("--fps", type=int, default=24)
    vid.add_argument("--audio-kbps", type=int, default=96)

    args = ap.parse_args()
    if not args.src.is_file():
        raise SystemExit(f"Source not found: {args.src}")
    if args.src.resolve() == args.dst.resolve():
        raise SystemExit("Destination must differ from source; originals are never overwritten")

    if args.kind == "image":
        meta = make_image(args.src, args.dst, args.max_edge, args.quality)
    else:
        meta = make_video(args.src, args.dst, args.max_edge, args.crf, args.fps, args.audio_kbps)

    meta.update({"source_path": str(args.src), "proxy_path": str(args.dst), "source_of_truth": False})
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
