#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
from threading import Thread

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
    'c3':'MFChunHei_Noncommercial-Regular.ttf',
    'e1':'manteka.ttf'
}

panels={
    'left':(0,0,180,118),
    'right':(184,0,246,118),
    'righttop':(185,5,245,58),
    'rightbottom':(185,62,245,117)
}

font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
cfont6 = ImageFont.truetype(os.path.join(picdir, fonts['c3']), 6)
cfont8 = ImageFont.truetype(os.path.join(picdir, fonts['c3']), 8)
cfont10 = ImageFont.truetype(os.path.join(picdir, fonts['c3']), 10)
cfont12 = ImageFont.truetype(os.path.join(picdir, fonts['c1']), 12)
cfont16 = ImageFont.truetype(os.path.join(picdir, fonts['c3']), 16)
jfont6 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 6)
jfont8 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 8)
jfont10 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 10)
jfont12 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 12)
jfont16 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 16)
efont6 = ImageFont.truetype(os.path.join(picdir, fonts['e1']), 6)
efont8 = ImageFont.truetype(os.path.join(picdir, fonts['e1']), 8)
efont10 = ImageFont.truetype(os.path.join(picdir, fonts['e1']), 10)
efont12 = ImageFont.truetype(os.path.join(picdir, fonts['e1']), 12)
efont16 = ImageFont.truetype(os.path.join(picdir, fonts['e1']), 16)


epd = epd2in13_V2.EPD()
current_image = Image.new('1', (epd.height, epd.width), 255)
current_draw = ImageDraw.Draw(current_image)
pre_image = Image.new('1', (epd.height, epd.width), 255)
pre_draw = ImageDraw.Draw(pre_image)
mainFrame_image = Image.new('1', (epd.height, epd.width), 255)
mainFrame_draw = ImageDraw.Draw(mainFrame_image)
exitflag = True#各线程终止


class left:#左面板
    # def __init__(self):
    #     pass

    def leftpannel_draw(self,draw):
        draw.rectangle(panels['left'],fill=255)
        print('左已绘制')
        # return draw

class right:#右面版
    startflag = False
    def __init__(self):
        startflag = True
    def rightpannel_draw(self,draw):
        draw.rectangle(panels['right'])
        print('右已绘制')
        # return draw

def righttop_draw():
    # righttop_frame = Image.new('1', (epd.height, epd.width), 255)
    # righttop_frame_draw = ImageDraw.Draw(righttop_frame)

    while exitflag:
        mainFrame_draw.rectangle(panels['righttop'], fill=255)
        mainFrame_draw.text((186,5), time.strftime('%H:%M:%S'), font=efont10, fill=0)
        time.sleep(1)
        # epd.displayPartial(epd.getbuffer(mainFrame_draw))

def rightbottom_draw():
    # rightbottom_frame = Image.new('1', (epd.height, epd.width), 255)
    # rightbottom_frame_draw = ImageDraw.Draw(rightbottom_frame)

    while exitflag:
        mainFrame_draw.rectangle(panels['rightbottom'], fill=255)
        mainFrame_draw.text((186,63), time.strftime('%H:%M:%S'), font=efont12, fill=0)
        time.sleep(5)
        # epd.displayPartial(epd.getbuffer(rightbottom_frame))


def initdis():
    print('init')
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

def initMainFrame(image_arg):
    print('inir baseframe')
    #初始化左右面板
    left.leftpannel_draw(0,mainFrame_draw)
    right.rightpannel_draw(0,mainFrame_draw)#绘制左右区域
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
    num = 0
    global exitflag
    try:
        initdis()
        # current_draw.text((1, 92), u'看不见我', font=cfont16, fill=0)
        initMainFrame(mainFrame_image)
        print('开始画图')
        trt = Thread(target=righttop_draw)
        trb = Thread(target=rightbottom_draw)
        trt.start()
        trb.start()
        while True:
            mainFrame_draw.rectangle((5, 5, 175, 30), fill=255)
            # mainFrame_draw.rectangle((186, 5, 245, 117), fill=255)
            mainFrame_draw.text((5, 5),str(num)+u'次 左侧文本测试长长长', font=cfont12, fill=0)
            mainFrame_draw.text((10, 17), u'XXX，晚上好', font = cfont16, fill = 0)
            # mainFrame_draw.text((186, 105), time.strftime('%H:%M:%S'), font=jfont10, fill=0)\
            epd.displayPartial(epd.getbuffer(mainFrame_image))
            num=num+1
            time.sleep(1)
            if(num == 10):
                exitflag = False
                break
        exitdis()
    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd2in13_V2.epdconfig.module_exit()
        exit()



displaypro()
