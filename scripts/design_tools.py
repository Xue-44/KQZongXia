#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
设计工具脚本 - 为市场虾 Agent 提供设计自动化能力
支持四品牌的物料批量生成、尺寸调整、品牌色彩应用等功能
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Union
from dataclasses import dataclass
from enum import Enum

# 尝试导入图像处理库
try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

try:
    import cv2
    import numpy as np
    HAS_OPENCV = True
except ImportError:
    HAS_OPENCV = False


class Brand(Enum):
    TRUMPCHI = "trumpchi"
    AUDI = "audi"
    HYPER = "hyper"
    AION = "aion"


# 四品牌配色方案
BRAND_PALETTES = {
    Brand.TRUMPCHI: {
        "name": "广汽传祺",
        "primary": (0, 102, 204), "secondary": (192, 192, 192),
        "bg": (255, 255, 255), "dark_bg": (245, 245, 245),
        "text": (51, 51, 51), "light_text": (255, 255, 255),
        "hex_primary": "#0066CC", "hex_secondary": "#C0C0C0",
    },
    Brand.AUDI: {
        "name": "上汽奥迪",
        "primary": (0, 0, 0), "secondary": (212, 175, 55),
        "bg": (26, 26, 26), "dark_bg": (0, 0, 0),
        "text": (255, 255, 255), "light_text": (212, 175, 55),
        "hex_primary": "#000000", "hex_secondary": "#D4AF37",
    },
    Brand.HYPER: {
        "name": "广汽昊铂",
        "primary": (138, 43, 226), "secondary": (255, 215, 0),
        "bg": (26, 10, 46), "dark_bg": (10, 0, 20),
        "text": (255, 255, 255), "light_text": (255, 215, 0),
        "hex_primary": "#8A2BE2", "hex_secondary": "#FFD700",
    },
    Brand.AION: {
        "name": "广汽埃安",
        "primary": (0, 176, 80), "secondary": (255, 255, 255),
        "bg": (255, 255, 255), "dark_bg": (232, 245, 233),
        "text": (51, 51, 51), "light_text": (255, 255, 255),
        "hex_primary": "#00B050", "hex_secondary": "#FFFFFF",
    },
}

# 物料尺寸规范
MATERIAL_SIZES = {
    "banner_1920x600": (1920, 600),
    "social_cover": (800, 800),
    "feed_ad_1080x1920": (1080, 1920),
    "video_cover": (1920, 1080),
    "standee_80x180": (800, 1800),
    "brochure_a4": (2480, 3508),
    "invitation_a5": (1748, 2480),
    "badge_85x54": (1004, 638),
    "h5_page": (750, 1334),
}


class DesignTools:
    """设计工具主类"""

    DEFAULT_ASSETS = Path("G:/openclaw/data/.openclaw/workspace/KaiQiJiTuan/assets")
    DEFAULT_OUTPUT = Path("G:/openclaw/data/.openclaw/workspace/KaiQiJiTuan/output")

    def __init__(self, assets_dir: Optional[Path] = None):
        self.assets_dir = Path(assets_dir) if assets_dir else self.DEFAULT_ASSETS
        self._ensure_dirs()

    def _ensure_dirs(self):
        for d in ["logos", "images", "backgrounds", "icons", "brand-assets"]:
            (self.assets_dir / d).mkdir(parents=True, exist_ok=True)
        self.DEFAULT_OUTPUT.mkdir(parents=True, exist_ok=True)

    def get_brand_palette(self, brand: Union[Brand, str]) -> Dict:
        if isinstance(brand, str):
            brand = Brand(brand.lower())
        if brand not in BRAND_PALETTES:
            raise ValueError(f"未知品牌: {brand}, 可选: {[b.value for b in Brand]}")
        return BRAND_PALETTES[brand]

    def list_brands(self) -> List[Dict]:
        result = []
        for b in Brand:
            p = BRAND_PALETTES[b]
            result.append({
                "key": b.value,
                "name": p["name"],
                "primary": p["hex_primary"],
                "secondary": p["hex_secondary"],
            })
        return result

    def create_brand_bg(self, brand: Brand, size: Tuple[int, int],
                         style: str = "gradient") -> Optional[object]:
        if not HAS_PIL:
            raise ImportError("需要安装 Pillow: pip install Pillow")
        palette = self.get_brand_palette(brand)
        w, h = size
        if style == "solid":
            return Image.new('RGB', (w, h), palette["primary"])
        elif style == "gradient":
            img = Image.new('RGB', (w, h), palette["bg"])
            draw = ImageDraw.Draw(img)
            for i in range(h):
                ratio = i / h
                r = int(palette["primary"][0] * (1 - ratio) + palette["bg"][0] * ratio)
                g = int(palette["primary"][1] * (1 - ratio) + palette["bg"][1] * ratio)
                b = int(palette["primary"][2] * (1 - ratio) + palette["bg"][2] * ratio)
                draw.line([(0, i), (w, i)], fill=(r, g, b))
            return img
        else:
            return Image.new('RGB', (w, h), palette["bg"])

    def apply_brand_overlay(self, image_path: Path, brand: Union[Brand, str],
                            opacity: float = 0.15,
                            output_path: Optional[Path] = None) -> Path:
        if not HAS_PIL:
            raise ImportError("需要安装 Pillow: pip install Pillow")
        if isinstance(brand, str):
            brand = Brand(brand.lower())
        palette = self.get_brand_palette(brand)
        original = Image.open(image_path).convert('RGB')
        overlay = Image.new('RGB', original.size, palette["primary"])
        blended = Image.blend(original, overlay, opacity)
        if output_path is None:
            output_path = (self.DEFAULT_OUTPUT /
                          f"{image_path.stem}_{brand.value}{image_path.suffix}")
        blended.save(output_path)
        print(f"已保存: {output_path}")
        return output_path

    def batch_resize(self, input_dir: Path, output_dir: Path,
                     target_size: Tuple[int, int],
                     keep_ratio: bool = True,
                     bg_color: Optional[Tuple[int, int, int]] = None) -> List[Path]:
        if not HAS_PIL:
            raise ImportError("需要安装 Pillow: pip install Pillow")
        output_dir.mkdir(parents=True, exist_ok=True)
        exts = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
        results = []
        for f in sorted(input_dir.iterdir()):
            if f.suffix.lower() not in exts:
                continue
            try:
                img = Image.open(f).convert('RGB')
                if keep_ratio:
                    img.thumbnail(target_size, Image.Resampling.LANCZOS)
                    canvas = Image.new('RGB', target_size, bg_color or (255, 255, 255))
                    px = (target_size[0] - img.width) // 2
                    py = (target_size[1] - img.height) // 2
                    canvas.paste(img, (px, py))
                    img = canvas
                else:
                    img = img.resize(target_size, Image.Resampling.LANCZOS)
                out = output_dir / f"{f.stem}_resized{f.suffix}"
                img.save(out)
                results.append(out)
                print(f"已调整: {f.name} -> {out.name}")
            except Exception as e:
                print(f"错误 ({f.name}): {e}")
        return results

    def batch_covers(self, brands: List[str], size: Tuple[int, int] = (800, 800),
                     campaign: str = "") -> Dict[str, Path]:
        if not HAS_PIL:
            raise ImportError("需要安装 Pillow: pip install Pillow")
        out_dir = self.DEFAULT_OUTPUT / "covers"
        out_dir.mkdir(parents=True, exist_ok=True)
        results = {}
        for b_name in brands:
            brand = Brand(b_name.lower())
            palette = self.get_brand_palette(brand)
            bg = self.create_brand_bg(brand, size, "gradient")
            draw = ImageDraw.Draw(bg)
            # 尝试加载字体
            try:
                title_font = ImageFont.truetype("C:/Windows/Fonts/msyhbd.ttc", 48)
                sub_font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 32)
            except Exception:
                title_font = ImageFont.load_default()
                sub_font = ImageFont.load_default()
            # 绘制文字
            title = palette["name"]
            bbox = draw.textbbox((0, 0), title, font=title_font)
            tw = bbox[2] - bbox[0]
            draw.text(((size[0] - tw) // 2, size[1] // 3), title,
                      fill=palette["light_text"], font=title_font)
            if campaign:
                bbox2 = draw.textbbox((0, 0), campaign, font=sub_font)
                cw = bbox2[2] - bbox2[0]
                draw.text(((size[0] - cw) // 2, size[1] // 2), campaign,
                          fill=palette["light_text"], font=sub_font)
            out_path = out_dir / f"{b_name}_cover_{campaign or 'default'}.png"
            bg.save(out_path)
            results[b_name] = out_path
            print(f"已生成: {out_path}")
        return results

    def quality_check(self, file_path: Path) -> Dict:
        """质量检查"""
        path = Path(file_path)
        result = {
            "file": str(path),
            "exists": path.exists(),
            "extension": path.suffix.lower(),
            "checks": [],
        }
        if not path.exists():
            result["checks"].append({"item": "文件存在", "status": "FAIL"})
            return result
        result["size_bytes"] = path.stat().st_size
        if path.suffix.lower() in {'.png', '.jpg', '.jpeg'} and HAS_PIL:
            with Image.open(path) as img:
                result["dimensions"] = f"{img.width}x{img.height}"
                result["mode"] = img.mode
                # 分辨率检查
                result["checks"].append({
                    "item": "分辨率",
                    "value": f"{img.width}x{img.height}",
                    "status": "OK" if img.width >= 800 else "LOW"
                })
                # 色彩模式检查
                result["checks"].append({
                    "item": "色彩模式",
                    "value": img.mode,
                    "status": "OK" if img.mode in ('RGB', 'CMYK', 'RGBA') else "WARN"
                })
        result["checks"].append({
            "item": "格式",
            "value": path.suffix,
            "status": "OK" if path.suffix.lower() in (
                '.png', '.jpg', '.jpeg', '.pdf', '.ai', '.psd') else "WARN"
        })
        return result


def main():
    parser = argparse.ArgumentParser(description="设计工具 - 市场虾 Agent")
    sub = parser.add_subparsers(dest="command")

    # brand-colors
    sp = sub.add_parser("brand-colors", help="查看品牌配色")
    sp.add_argument("--brand", default=None, help="品牌名 (trumpchi/audi/hyper/aion)")

    # resize
    sp = sub.add_parser("resize", help="批量调整图片尺寸")
    sp.add_argument("--input", required=True, help="输入目录")
    sp.add_argument("--output", required=True, help="输出目录")
    sp.add_argument("--size", default="800x800", help="目标尺寸 WxH")
    sp.add_argument("--no-ratio", action="store_true", help="不保持宽高比")

    # batch-covers
    sp = sub.add_parser("batch-covers", help="批量生成品牌封面")
    sp.add_argument("--brands", nargs="+", default=["trumpchi", "audi", "hyper", "aion"],
                    help="品牌列表")
    sp.add_argument("--campaign", default="", help="活动名称")
    sp.add_argument("--size", default="800x800", help="尺寸 WxH")

    # check
    sp = sub.add_parser("check", help="设计质量检查")
    sp.add_argument("--file", required=True, help="文件路径")

    args = parser.parse_args()
    tools = DesignTools()

    if args.command == "brand-colors":
        if args.brand:
            p = tools.get_brand_palette(args.brand)
            print(json.dumps({
                "name": p["name"],
                "primary": p["hex_primary"],
                "secondary": p["hex_secondary"]
            }, ensure_ascii=False))
        else:
            for b in tools.list_brands():
                print(f"{b['key']:12s} {b['name']:8s}  {b['primary']:8s}  {b['secondary']}")

    elif args.command == "resize":
        w, h = map(int, args.size.split("x"))
        tools.batch_resize(Path(args.input), Path(args.output), (w, h),
                          keep_ratio=not args.no_ratio)

    elif args.command == "batch-covers":
        w, h = map(int, args.size.split("x"))
        tools.batch_covers(args.brands, (w, h), args.campaign)

    elif args.command == "check":
        result = tools.quality_check(Path(args.file))
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()