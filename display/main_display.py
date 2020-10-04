#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image, ImageDraw, ImageFont

fonts={
    'c1':'MFTheGoldenEra_Noncommercial-Light.ttf',
    'c2':'MFKeSong_Noncommercial-Regular.ttf',
    'c3':'MFChunHei_Noncommercial-Regular.ttf'
}

font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
cfont6 = ImageFont.truetype(os.path.join(picdir, fonts['c2']), 6)
cfont8 = ImageFont.truetype(os.path.join(picdir, fonts['c2']), 8)
cfont10 = ImageFont.truetype(os.path.join(picdir, fonts['c2']), 10)
cfont12 = ImageFont.truetype(os.path.join(picdir, fonts['c2']), 12)
cfont16 = ImageFont.truetype(os.path.join(picdir, fonts['c2']), 16)
jfont6 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 6)
jfont8 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 8)
jfont10 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 10)
jfont12 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 12)
jfont16 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 16)







epd = epd2in13_V2.EPD()
current_image = Image.new('1', (epd.height, epd.width), 255)
current_draw = ImageDraw.Draw(current_image)
pre_image = Image.new('1', (epd.height, epd.width), 255)
pre_draw = ImageDraw.Draw(pre_image)


def initdis():
    print('init')
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

def initMainFrame(image_arg):
    print('inir baseframe')
    epd.displayPartBaseImage(epd.getbuffer(image_arg))
    epd.init(epd.PART_UPDATE)

def exitdis():
    print('exit')
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    print('sleep')
    epd.sleep()
    epd.Dev_exit()

def displaypro():
    try:
        initdis()
        current_draw.text((0, 92), u'测试文本', font=cfont16, fill=0)
        initMainFrame(current_image)
        pre_draw.rectangle((0, 0, 125, 61), fill=255)
        pre_draw.rectangle((126, 62, 250, 122), fill=255)
        pre_draw.text((0, 0),u'文本测试', font=cfont12, fill=0)
        pre_draw.text((10, 13), u'新世紀エヴァンゲリオン', font = jfont16, fill = 0)
        epd.displayPartial(epd.getbuffer(pre_image))
        time.sleep(10)
        exitdis()
    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd2in13_V2.epdconfig.module_exit()
        exit()



displaypro()
