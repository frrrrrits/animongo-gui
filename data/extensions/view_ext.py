# credit: https://github.com/AyraHikari/PyAnimeIndo/blob/GUI/utils/utils.py

import os
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from PyQt5.QtCore import QFile
from PyQt5.QtGui import QImage, QPixmap

def get_res_path(icon_name):
    app_path = os.path.abspath(os.getcwd())
    folder = "res/"
    path = os.path.join(app_path, folder)
    icon = os.path.normpath(os.path.join(path, icon_name))
    return icon

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

def make_rounded(pic, eps=None):
    im = Image.open(BytesIO(pic))
    if eps:
       im = write_eps_cover(im, eps)
    im = add_corners(im, 18)
    return pil2pixmap(im)

def make_rounded_res(pic, is_bytes=False):
    if not is_bytes:
        im = Image.open(pic)
    else:
        im = Image.open(BytesIO(pic))
    im = add_corners(im, int(im.size[0]/3))
    return pil2pixmap(im)


def write_eps_cover(img, eps):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    font = ImageFont.truetype(get_res_path("fonts.ttf"), 45)
    text_w, text_h = draw.textsize(eps, font)
    draw.rounded_rectangle((20, h/text_h*4, text_w+45, text_h + 55), 17, fill="#e6c7ee")
    draw.text((33, h/text_h*5), eps, "black", font=font)
    return img

def pil2pixmap(image):
    bytes_img = BytesIO()
    image.save(bytes_img, format='png')
    qimg = QImage()
    qimg.loadFromData(bytes_img.getvalue())
    return QPixmap.fromImage(qimg)



