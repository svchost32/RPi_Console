#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
from threading import Thread
import wrcon

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
    'e1':'manteka.ttf',
    'e2':'SourceCodePro-Regular.otf'

}

panels={
    'left':(0,0,180,121),
    'right':(184,0,246,121),
    'lefttitle':(5,5,179,21), #title16号字体
    'leftsubtitle':(5,22,179,35), #小标题12号,
    'lefttitleline':[(5, 37), (160, 37)],
    'leftcontent':(5,40,179,120),
    'rightime':(185,1,249,10),#右上时钟
    'righttop':(185,13,245,80),
    'rightbottom':(185,81,245,120),
    'rightbottomline':[(185,92), (240, 92)]
}
font7 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 7)
font8 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 8)
font9 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 9)
font10 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 10)
font12 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 12)
font14 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 14)
font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
cfont6 = ImageFont.truetype(os.path.join(picdir, fonts['c3']), 6)
cfont8 = ImageFont.truetype(os.path.join(picdir, fonts['c2']), 8)
cfont9 = ImageFont.truetype(os.path.join(picdir, fonts['c2']), 9)
cfont10 = ImageFont.truetype(os.path.join(picdir, fonts['c3']), 10)
cfont12 = ImageFont.truetype(os.path.join(picdir, fonts['c1']), 12)
cfont16 = ImageFont.truetype(os.path.join(picdir, fonts['c3']), 16)
cfont24 = ImageFont.truetype(os.path.join(picdir, fonts['c1']), 24)

jfont6 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 6)
jfont8 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 8)
jfont10 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 10)
jfont12 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 12)
jfont16 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 16)
efont6 = ImageFont.truetype(os.path.join(picdir, fonts['e1']), 6)
efont7 = ImageFont.truetype(os.path.join(picdir, fonts['e1']), 7)
efont8 = ImageFont.truetype(os.path.join(picdir, fonts['e1']), 8)
efont9 = ImageFont.truetype(os.path.join(picdir, fonts['e1']), 9)
efont10 = ImageFont.truetype(os.path.join(picdir, fonts['e1']), 10)
efont12 = ImageFont.truetype(os.path.join(picdir, fonts['e2']), 12)
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
        draw.rectangle(panels['left'],fill=255)#框线 255没有，0有
        print('左已绘制')
        # return draw

class right:#右面版
    startflag = False
    def __init__(self):
        startflag = True
    def rightpannel_draw(self,draw):
        draw.rectangle(panels['right'],fill=255)
        print('右已绘制')




def lefttitle_draw():
    while exitflag:
        mainFrame_draw.rectangle(panels['lefttitle'], fill=255)#填充色
        mainFrame_draw.text((panels['lefttitle'][0], panels['lefttitle'][1]),u'标题文本测试', font=cfont16, fill=0)
        time.sleep(1)

def leftsubtitle_draw():
    while exitflag:
        mainFrame_draw.rectangle(panels['leftsubtitle'], fill=255)
        mainFrame_draw.text((panels['leftsubtitle'][0]+2, panels['leftsubtitle'][1]),u'副标题测试', font=font12, fill=0)
        time.sleep(2)

def leftcontent_draw():
    while exitflag:
        mainFrame_draw.rectangle(panels['leftcontent'], fill=255)#填充色
        mainFrame_draw.rectangle(panels['leftcontent'])  # 填充色
        mainFrame_draw.text((panels['leftcontent'][0]+5, panels['leftcontent'][1]+5),u'换个内容:', font=cfont24, fill=0)
        mainFrame_draw.text((panels['leftcontent'][0] + 5, panels['leftcontent'][1] + 31),wrcon.read_config('content'), font=cfont24, fill=0)
        time.sleep(1)


def rightTime():
    while exitflag:
        mainFrame_draw.rectangle(panels['rightime'], fill=255)
        mainFrame_draw.text((panels['rightime'][0]+15,panels['rightime'][1]), time.strftime('%H:%M:%S'), font=efont9, fill=0)
        mainFrame_draw.line(
            [(panels['righttop'][0]+12, panels['righttop'][1]-1), (panels['righttop'][2]-2, panels['righttop'][1]-1)],
            fill=0, width=1)
        time.sleep(1)



def righttop_draw():
    # righttop_frame = Image.new('1', (epd.height, epd.width), 255)
    # righttop_frame_draw = ImageDraw.Draw(righttop_frame)

    while exitflag:
        mainFrame_draw.rectangle(panels['righttop'], fill=255)
        mainFrame_draw.rectangle((panels['righttop'][0],panels['righttop'][1],panels['righttop'][2],panels['righttop'][1]+21),fill=255)##框1
        # mainFrame_draw.line(
        #     [(panels['righttop'][0], panels['righttop'][1] ), (panels['righttop'][2], panels['righttop'][1])],
        #     fill=0, width=1)
        mainFrame_draw.line(
            [(panels['righttop'][0], panels['righttop'][1] + 1), (panels['righttop'][0], panels['righttop'][1] + 20)],
            fill=0, width=2)
        # mainFrame_draw.line(
        #     [(panels['righttop'][2], panels['righttop'][1] + 1), (panels['righttop'][2], panels['righttop'][1] + 20)],
        #     fill=0, width=1)
        mainFrame_draw.text((panels['righttop'][0]+3,panels['righttop'][1]+1), u'测试文本行1', font=font9, fill=0)##框1行1文本
        mainFrame_draw.text((panels['righttop'][0]+3, panels['righttop'][1]+11), u'测试文本行2', font=font9, fill=0)

        mainFrame_draw.rectangle((panels['righttop'][0], panels['righttop'][1]+23, panels['righttop'][2], panels['righttop'][1] +44),fill=255)
        # mainFrame_draw.line(##上边
        #     [(panels['righttop'][0], panels['righttop'][1]+23), (panels['righttop'][2], panels['righttop'][1]+23)],
        #     fill=0, width=1)
        mainFrame_draw.line(
            [(panels['righttop'][0], panels['righttop'][1]+24), (panels['righttop'][0], panels['righttop'][1] + 43)],
            fill=0, width=2)
        # mainFrame_draw.line(
        #     [(panels['righttop'][2], panels['righttop'][1] + 24), (panels['righttop'][2], panels['righttop'][1] + 43)],
        #     fill=0, width=1)
        mainFrame_draw.text((panels['righttop'][0] + 3, panels['righttop'][1] + 24), u'填充内容2-1', font=font9,fill=0)  ##框1行1文本
        mainFrame_draw.text((panels['righttop'][0] + 3, panels['righttop'][1] + 34), u'填充内容2-2', font=font9, fill=0)

        mainFrame_draw.rectangle(
            (panels['righttop'][0], panels['righttop'][1] + 46, panels['righttop'][2], panels['righttop'][1] + 67),
            fill=255)
        # mainFrame_draw.line(
        #     [(panels['righttop'][0], panels['righttop'][1]+46), (panels['righttop'][2], panels['righttop'][1]+46)],
        #     fill=0, width=1)
        mainFrame_draw.line(
            [(panels['righttop'][0], panels['righttop'][1]+47), (panels['righttop'][0], panels['righttop'][1] + 66)],
            fill=0, width=2)
        # mainFrame_draw.line(#下边
        #     [(panels['righttop'][2], panels['righttop'][1] + 47), (panels['righttop'][2], panels['righttop'][1] + 66)],
        #     fill=0, width=1)
        mainFrame_draw.text((panels['righttop'][0] + 3, panels['righttop'][1] + 47), u'填充内容3-1', font=font9,fill=0)  ##框1行1文本
        mainFrame_draw.text((panels['righttop'][0] + 3, panels['righttop'][1] + 57), u'填充内容3-2', font=font9, fill=0)
        time.sleep(1)
        # epd.displayPartial(epd.getbuffer(mainFrame_draw))

def rightbottom_draw():
    # rightbottom_frame = Image.new('1', (epd.height, epd.width), 255)
    # rightbottom_frame_draw = ImageDraw.Draw(rightbottom_frame)

    while exitflag:
        mainFrame_draw.rectangle(panels['rightbottom'], fill=255)
        mainFrame_draw.text((panels['rightbottom'][0], panels['rightbottom'][1]), 'Conn Status', font=efont8,fill=0)
        mainFrame_draw.line(panels['rightbottomline'], fill=0, width=1)
        mainFrame_draw.text((panels['rightbottom'][0],panels['rightbottom'][1]+13), 'WebSer ..Good   ', font=font8, fill=0)
        mainFrame_draw.rectangle((panels['rightbottom'][0], panels['rightbottom'][1] + 22,panels['rightbottom'][2] -2,panels['rightbottom'][1] + 30), fill=0)
        mainFrame_draw.text((panels['rightbottom'][0], panels['rightbottom'][1] + 22), 'TcPSer ..Good   ', font=font8,fill=255)
        mainFrame_draw.text((panels['rightbottom'][0], panels['rightbottom'][1] + 31), 'Host:'+wrcon.read_config('ip'), font=font8,fill=0)
        time.sleep(2)
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
    mainFrame_draw.line(panels['lefttitleline'], fill=0, width=1)
    # mainFrame_draw.text((5, 100), wrcon.read_config('ip'), font=font10, fill=0)
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
        tlt= Thread(target=lefttitle_draw)
        tlst= Thread(target=leftsubtitle_draw)
        tlc = Thread(target=leftcontent_draw)
        rt=Thread(target=rightTime)
        trt.start()
        trb.start()
        tlt.start()
        tlst.start()
        tlc.start()
        rt.start()
        while True:
            # mainFrame_draw.rectangle((5, 5, 175, 90), fill=255)
            # mainFrame_draw.rectangle((186, 5, 245, 117), fill=255)
            # mainFrame_draw.text((5, 5),str(num)+u'次 左侧文本测试长长长', font=cfont12, fill=0)
            # mainFrame_draw.text((5, 17), wrcon.read_config('main'), font = cfont16, fill = 0)
            # mainFrame_draw.text((186, 105), time.strftime('%H:%M:%S'), font=jfont10, fill=0)\
            epd.displayPartial(epd.getbuffer(mainFrame_image))
            num=num+1
            time.sleep(1)
            if(num == 15):
                exitflag = False
                break
            # if (wrcon.read_config('status').endswith('bye')):
            #     print('显示结束')
            #     exitflag = False
            #     break
        exitdis()
    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd2in13_V2.epdconfig.module_exit()
        exit()



