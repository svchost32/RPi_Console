#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

# import keyboard
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image, ImageDraw, ImageFont

from threading import Thread


def displaymain():

    try:
        logging.info("epd2in13_V2 Demo")

        epd = epd2in13_V2.EPD()
        logging.info("init and Clear")
        epd.init(epd.FULL_UPDATE)
        epd.Clear(0xFF)

        # Drawing on the image
        font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
        font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
        font16 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 16)
        font12 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 12)

        time_image = Image.new('1', (epd.height, epd.width), 255)
        time_draw = ImageDraw.Draw(time_image)

        image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
        draw = ImageDraw.Draw(image)

        epd.init(epd.FULL_UPDATE)

        num = 0

        time_draw.text((0, 107), str(num) + 'Bottom font15', font=font12, fill=0)
        draw.text((0, 107), str(num) + 'Bottom font15', font=font12, fill=0)

        epd.displayPartBaseImage(epd.getbuffer(image))

        epd.init(epd.PART_UPDATE)

        # draw.text((0, 107), 'Bottom font15', font = font15, fill = 0)

        currtemttime = 0
        while (True):
            # while(s.recvfrom(1024)[0].decode('gb2312')!='exit'):
            time_draw.rectangle((0, 0, 125, 61), fill=255)
            time_draw.rectangle((126, 62, 250, 122), fill=255)
            time_draw.text((0, 0), str(num) + u'次 time draw', font=font12, fill=0)
            # time_draw.text((10, 13), u'新世紀エヴァンゲリオン', font = font16, fill = 0)
            # time_draw.text((10, 13), recv_msg, font=font16, fill=0)
            # print(recv_msg+' Thread 2')
            # logging.info(recv_msg)
            # time_draw.text((0, 40), '', font = font12, fill = 0)
            time_draw.text((126, 62), time.strftime('%H:%M:%S'), font=font16, fill=0)
            # edp.displayPartial
            # logging.info(str(time.time()))
            draw.rectangle((126, 62, 250, 122), fill=255)
            draw.text((0, 0), str(num) + u'次 draw', font=font12, fill=0)



            epd.displayPartial(epd.getbuffer(time_image))
            print('part1')
            time.sleep(2)



            epd.displayPartial(epd.getbuffer(image))
            print('part2')
            time.sleep(2)


            num = num + 1
            # print(recv_msg)
            if(num == 5):
                break
            # if (recv_msg.endswith('bye')):
            #     break



        logging.info("Clear...")
        epd.init(epd.FULL_UPDATE)
        epd.Clear(0xFF)

        logging.info("Goto Sleep...")
        epd.sleep()
        epd.Dev_exit()

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd2in13_V2.epdconfig.module_exit()
        exit()


displaymain()
