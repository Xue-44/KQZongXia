#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
市场推广图片处理工具
用于 KaiQiJiTuan Agent 的市场推广图片处理能力
支持广告识别、活动物料识别、竞品分析、图片仿作
"""

import os, json, logging
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

logger = logging.getLogger(__name__)

class MarketingImageRecognition:
    """市场推广图片识别工具"""

    AD_ELEMENTS = {
        "logo": ["logo","品牌标识","商标","标志"],
        "cta": ["立即购买","点击了解","限时优惠","扫码关注","咨询热线"],
        "price": ["￥","元","价格","特价","优惠价"],
        "promotion": ["促销","活动","折扣","满减","赠品","抽奖"],
        "contact": ["电话","微信","二维码","地址","官网","客服"]
    }

    @staticmethod
    def detect_ad_elements(image_path):
        img = cv2.imread(image_path)
        if img is None: return {'error': '无法读取图片'}
        h, w = img.shape[:2]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mser = cv2.MSER_create()
        regions, _ = mser.detectRegions(gray)
        text_regions = []
        for region in regions:
            x, y, bw, bh = cv2.boundingRect(region)
            if bw * bh > 100 and 0.1 < bw / max(bh, 1) < 10:
                text_regions.append({'x':int(x),'y':int(y),'width':int(bw),'height':int(bh)})
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pixels = img_rgb.reshape(-1, 3)
        from collections import Counter
        unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)
        top_colors = unique_colors[np.argsort(-counts)[:5]]
        return {
            'image_size': f'{w}x{h}',
            'text_region_count': len(text_regions),
            'text_coverage': round(len(text_regions)*100/(w*h/1000),2),
            'dominant_colors': [list(map(int,c)) for c in top_colors],
            'is_likely_ad': len(text_regions) > 5
        }

    @staticmethod
    def analyze_competitor_material(image_path):
        img = cv2.imread(image_path)
        if img is None: return {'error': '无法读取图片'}
        h, w = img.shape[:2]
        brand_colors = {
            '传祺': [(0,100,200),(200,50,50)],
            '奥迪': [(0,0,0),(255,255,255),(200,0,0)],
            '昊铂': [(0,200,255),(0,50,100)],
            '埃安': [(0,180,100),(0,80,50)],
            '特斯拉': [(200,50,50),(50,50,50)],
            '比亚迪': [(255,200,0),(0,100,200)],
            '宝马': [(0,100,200),(200,200,200)],
            '奔驰': [(0,0,0),(200,200,200)]
        }
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pixels = img_rgb.reshape(-1, 3)
        brand_scores = {}
        for brand, colors in brand_colors.items():
            score = 0
            for color in colors:
                distances = np.linalg.norm(pixels.astype(float)-np.array(color),axis=1)
                score += np.sum(distances<80)/len(pixels)
            brand_scores[brand] = round(score/len(colors),4)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        edge_density = np.sum(edges>0)/(w*h)
        contrast = np.std(gray)
        design_score = round((1-edge_density)*0.3+min(contrast/100,1)*0.4+(1-abs(0.5-np.mean(gray)/255))*0.3, 2)
        return {
            'brand_match_scores': brand_scores,
            'likely_brand': max(brand_scores,key=brand_scores.get),
            'design_quality': design_score,
            'edge_density': round(edge_density,4),
            'contrast': round(float(contrast),1),
            'brightness': round(float(np.mean(gray)),1)
        }

    @staticmethod
    def detect_event_material(image_path):
        img = cv2.imread(image_path)
        if img is None: return {'error': '无法读取图片'}
        h, w = img.shape[:2]
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        saturation = img_hsv[:,:,1]
        high_sat_pct = np.sum(saturation>150)/(w*h)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),1.1,4)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mser = cv2.MSER_create()
        regions, _ = mser.detectRegions(gray)
        text_count = len([r for r in regions if cv2.contourArea(r)>100])
        return {
            'is_event_material': high_sat_pct>0.1 or len(faces)>0,
            'face_count': len(faces),
            'text_region_count': text_count,
            'saturation_level': round(float(np.mean(saturation)),1),
            'high_saturation_pct': round(high_sat_pct*100,1),
            'event_type': '产品发布会' if len(faces)>0 else '广告物料'
        }

    @staticmethod
    def evaluate_design_quality(image_path):
        img = cv2.imread(image_path)
        if img is None: return {'error': '无法读取图片'}
        h, w = img.shape[:2]
        center_region = img[h//4:3*h//4, w//4:3*w//4]
        edge_regions = [img[0:h//4,0:w//4], img[0:h//4,3*w//4:w], img[3*h//4:h,0:w//4], img[3*h//4:h,3*w//4:w]]
        cb = np.mean(cv2.cvtColor(center_region, cv2.COLOR_BGR2GRAY))
        eb = np.mean([np.mean(cv2.cvtColor(r, cv2.COLOR_BGR2GRAY)) for r in edge_regions])
        vb = 1 - abs(cb-eb)/255
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pixels = img_rgb.reshape(-1, 3)
        ch = 1 - np.mean(np.std(pixels, axis=0))/255
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        lapl = cv2.Laplacian(gray, cv2.CV_64F)
        sharp = np.var(lapl)
        overall = round(vb*0.3+ch*0.3+min(sharp/1000,1)*0.4, 2)
        return {
            'overall_score': overall,
            'visual_balance': round(vb,2),
            'color_harmony': round(ch,2),
            'sharpness': round(float(sharp),1),
            'composition': 'balanced' if vb>0.7 else 'unbalanced',
            'color_scheme': 'harmonious' if ch>0.7 else 'contrasting'
        }

class MarketingImageImitation:
    """市场推广图片仿作工具"""

    @staticmethod
    def create_ad_banner(brand, size=(1920,600), headline='', subhead='', cta_text='立即咨询', output_path=None):
        w, h = size
        palettes = {
            '传祺': {'primary':(0,100,200),'secondary':(200,50,50),'bg':(245,245,250),'text':(30,30,30)},
            '奥迪': {'primary':(20,20,20),'secondary':(200,0,0),'bg':(240,240,240),'text':(30,30,30)},
            '昊铂': {'primary':(0,160,230),'secondary':(0,60,120),'bg':(235,245,255),'text':(30,30,30)},
            '埃安': {'primary':(0,170,90),'secondary':(0,90,60),'bg':(240,255,245),'text':(30,30,30)}
        }
        colors = palettes.get(brand, palettes['传祺'])
        canvas = Image.new('RGB', (w,h), colors['bg'])
        draw = ImageDraw.Draw(canvas)
        for y in range(h):
            r = int(colors['primary'][0]*(1-y/h)+colors['secondary'][0]*y/h)
            g = int(colors['primary'][1]*(1-y/h)+colors['secondary'][1]*y/h)
            b = int(colors['primary'][2]*(1-y/h)+colors['secondary'][2]*y/h)
            draw.line([(0,y),(w,y)], fill=(r,g,b))
        draw.rectangle([0,0,w,50], fill=colors['primary'])
        cta_h = 80
        draw.rectangle([0,h-cta_h,w,h], fill=colors['secondary'])
        m = 40
        draw.rectangle([m,80,w-m,h-cta_h-20], outline=colors['primary'], width=2)
        try:
            font_l = ImageFont.truetype('simhei.ttf', 48)
            font_m = ImageFont.truetype('simhei.ttf', 32)
            font_s = ImageFont.truetype('simhei.ttf', 24)
        except:
            font_l = font_m = font_s = ImageFont.load_default()
        if headline:
            draw.text((m+30, 100), headline, fill=colors['text'], font=font_l)
        if subhead:
            draw.text((m+30, 170), subhead, fill=colors['text'], font=font_m)
        cta_x = (w-300)//2
        draw.text((cta_x, h-cta_h+20), cta_text, fill=(255,255,255), font=font_m)
        if output_path is None:
            output_path = str(Path.home()/f'Documents/ad_banner_{brand}_{datetime.now().strftime(chr(37)+'Y'+chr(37)+'m'+chr(37)+'d_'+chr(37)+'H'+chr(37)+'M')}.png')
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        canvas.save(output_path)
        return output_path

    @staticmethod
    def create_social_media_image(brand, content_text, platform='小红书', colors=None, output_path=None):
        size = (1080, 1080)
        w, h = size
        palettes = {
            '传祺': {'primary':(0,100,200),'secondary':(200,50,50),'bg':(245,245,250),'accent':(255,200,0)},
            '奥迪': {'primary':(20,20,20),'secondary':(200,0,0),'bg':(240,240,240),'accent':(180,180,180)},
            '昊铂': {'primary':(0,160,230),'secondary':(0,60,120),'bg':(235,245,255),'accent':(0,200,255)},
            '埃安': {'primary':(0,170,90),'secondary':(0,90,60),'bg':(240,255,245),'accent':(255,200,0)}
        }
        c = colors or palettes.get(brand, palettes['传祺'])
        canvas = Image.new('RGB', (w,h), c['bg'])
        draw = ImageDraw.Draw(canvas)
        # Banner at top
        draw.rectangle([0,0,w,120], fill=c['primary'])
        # Bottom bar
        draw.rectangle([0,h-60,w,h], fill=c['secondary'])
        # Decorative elements
        for i in range(5):
            x = i*220+30
            draw.rounded_rectangle([x,130,x+180,180], radius=10, fill=c['accent'], outline=c['primary'])
        # Content area
        try:
            font_title = ImageFont.truetype('simhei.ttf', 44)
            font_body = ImageFont.truetype('simhei.ttf', 28)
            font_footer = ImageFont.truetype('simhei.ttf', 20)
        except:
            font_title = ImageFont.load_default()
            font_body = ImageFont.load_default()
            font_footer = ImageFont.load_default()
        draw.text((60, 220), f'【{brand}】{platform}推广', fill=c['text'], font=font_title)
        paragraphs = content_text.split(chr(10))
        y_pos = 300
        for para in paragraphs[:15]:
            draw.text((60, y_pos), para, fill=c['text'], font=font_body)
            y_pos += 40
        from datetime import datetime
        draw.text((w-300, h-50), f'{brand} | {datetime.now().strftime(chr(37)+'Y.'+chr(37)+'m.'+chr(37)+'d')}', fill=(255,255,255), font=font_footer)
        if output_path is None:
            output_path = str(Path.home()/f'Documents/social_{brand}_{platform}_{datetime.now().strftime(chr(37)+'Y'+chr(37)+'m'+chr(37)+'d')}.png')
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        canvas.save(output_path)
        return output_path

    @staticmethod
    def add_watermark(image_path, watermark_text, position='bottom-right', opacity=0.3, output_path=None):
        img = Image.open(image_path).convert('RGBA')
        w, h = img.size
        overlay = Image.new('RGBA', img.size, (255,255,255,0))
        draw = ImageDraw.Draw(overlay)
        try: font = ImageFont.truetype('simhei.ttf', max(16, min(w,h)//20))
        except: font = ImageFont.load_default()
        bbox = draw.textbbox((0,0), watermark_text, font=font)
        tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
        positions = {
            'bottom-right': (w-tw-20, h-th-20),
            'bottom-left': (20, h-th-20),
            'top-right': (w-tw-20, 20),
            'top-left': (20, 20),
            'center': ((w-tw)//2, (h-th)//2)
        }
        pos = positions.get(position, positions['bottom-right'])
        alpha = int(255 * opacity)
        draw.text(pos, watermark_text, fill=(255,255,255,alpha), font=font)
        result = Image.alpha_composite(img, overlay)
        if output_path is None:
            p = Path(image_path)
            output_path = str(p.parent / f'{p.stem}_watermarked{p.suffix}')
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        result.convert('RGB').save(output_path)
        return output_path

class MarketingBatchProcessor:
    """市场推广图片批量处理器"""

    @staticmethod
    def batch_analyze(image_paths):
        results = []
        rec = MarketingImageRecognition()
        for p in image_paths:
            try:
                ad_info = rec.detect_ad_elements(p)
                competitor_info = rec.analyze_competitor_material(p)
                event_info = rec.detect_event_material(p)
                design_info = rec.evaluate_design_quality(p)
                results.append({
                    'path': p,
                    'ad_analysis': ad_info,
                    'competitor_analysis': competitor_info,
                    'event_analysis': event_info,
                    'design_analysis': design_info
                })
            except Exception as e:
                results.append({'path': p, 'error': str(e)})
        return results

class MarketingReportGenerator:
    """市场推广报告生成器"""

    @staticmethod
    def generate_analysis_report(results, output_path):
        from datetime import datetime
        md = ['# 市场推广图片分析报告', '', f'生成时间: {datetime.now().isoformat()}', '', '---', '']
        md.append('| 文件 | 是否广告 | 疑似品牌 | 设计评分 | 活动物料 |')
        md.append('|------|---------|---------|---------|---------|')
        for r in results:
            if 'error' in r:
                md.append(f'| {Path(r["path"]).name} | - | - | - | 错误: {r["error"]} |')
                continue
            ad = r.get('ad_analysis',{})
            comp = r.get('competitor_analysis',{})
            dsn = r.get('design_analysis',{})
            evt = r.get('event_analysis',{})
            md.append(f'| {Path(r["path"]).name} | {ad.get("is_likely_ad","?")} | {comp.get("likely_brand","?")} | {dsn.get("overall_score","?")} | {evt.get("is_event_material","?")} |')
        md.extend(['', '---', '', '## 各图片详细分析', ''])
        for i, r in enumerate(results, 1):
            md.append(f'### {i}. {Path(r["path"]).name}')
            md.append(f'```json')
            md.append(json.dumps(r, indent=2, ensure_ascii=False, default=str))
            md.append(f'```')
            md.append('')
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        Path(output_path).write_text(chr(10).join(md), encoding='utf-8')
        return output_path

if __name__ == '__main__':
    from datetime import datetime
    rec = MarketingImageRecognition()
    imt = MarketingImageImitation()
    print('=== 市场推广图片处理工具就绪 ===')
    print('MarketingImageRecognition: detect_ad_elements, analyze_competitor_material, detect_event_material, evaluate_design_quality')
    print('MarketingImageImitation: create_ad_banner, create_social_media_image, add_watermark')
    print('MarketingBatchProcessor: batch_analyze')
    print('MarketingReportGenerator: generate_analysis_report')