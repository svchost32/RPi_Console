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
from PIL import Image,ImageDraw,ImageFont
import traceback
from socket import *
from threading import Thread
from suds.client import Client

sockets=[]

logging.basicConfig(level=logging.DEBUG)

# s = socket(AF_INET,SOCK_DGRAM)
# s.bind(('',2800))
# pre_msg = ''
recv_msg=''

# rec_data=s.recvfrom(1024)
# print(rec_data[0])


# def recv_data():
#     while (s.recvfrom(1024)[0].decode('gb2312')!='exit'):
#         recv_data = s.recvfrom(1024)
#         recv_msg = recv_data[0].decode('gb2312')
#         print(recv_msg+' Thread1')

#         # recv_msg =s.recvfrom(1024)[0].decode('gb2312')
#         # logging.info("收到信息"+recv_msg)

def info_main():
    server_socket = socket(AF_INET,SOCK_STREAM)
    server_socket.bind(('',8200))
    server_socket.listen()

    while True:
        client_socket,client_info=server_socket.accept()
        sockets.append(client_socket)
        t = Thread(target=readMSG,args=(client_socket,))
        t.start()

def readMSG(client_socket):
    global recv_msg
    while True:
        try:
            recv_data=client_socket.recv(1024)
        except:
            sockets.remove(client_socket)
            client_socket.close()
            print('失去连接')
            break
        # recv_data.decode('utf-8')
        if recv_data.decode('utf-8').endswith('exit'):
            sockets.remove(client_socket)
            client_socket.close()
            print('结束服务')
            os._exit(0)
        if len(recv_data) > 0:
            for socket in sockets:
                # print('发送消息来自'+str(socket))
                print(recv_data.decode('utf-8'))
                recv_msg = recv_data.decode('utf-8')
                # socket.send(recv_data)

        
# def get_ws_data():
#     client = Client('http://192.168.1.243:8000/?wsdl', cache=None)
#     result = client.service.say_hello('jason',1)
#     res = ''.join(result[0])
#     print('WS service work: '+res)
#     return res


def displaymain():
    global recv_msg
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
        # logging.info("1.Test TEXT...")
        # image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
        # draw = ImageDraw.Draw(image)

        # # draw.rectangle([(0,0),(50,50)],outline = 0)
        # # draw.rectangle([(55,0),(100,50)],fill = 0)
        # # draw.line([(0,0),(50,50)], fill = 0,width = 1)
        # # draw.line([(0,50),(50,0)], fill = 0,width = 1)
        # # draw.chord((10, 60, 50, 100), 0, 360, fill = 0)
        # # draw.ellipse((55, 60, 95, 100), outline = 0)
        # # draw.pieslice((55, 60, 95, 100), 90, 180, outline = 0)
        # # draw.pieslice((55, 60, 95, 100), 270, 360, fill = 0)
        # # draw.polygon([(110,0),(110,50),(150,25)],outline = 0)
        # # draw.polygon([(190,0),(190,50),(150,25)],fill = 0)
        # rec_data=s.recvfrom(1024)
        # logging.info(rec_data,rec_data[1],rec_data[0].decode('gb2312'))
        # draw.text((0, 0), 'TOP font15', font = font16, fill = 0)
        # # draw.text((0, 107),rec_data[0].decode('gb2312'), font = font16, fill = 0)
        # # draw.text((120, 60), 'e-Paper demo', font = font16, fill = 0)
        # # draw.text((110, 90), u'微雪电子', font = font16, fill = 0)
        # epd.display(epd.getbuffer(image))
        # time.sleep(2)
        
        # # read bmp file 
        # logging.info("2.read bmp file...")
        # image = Image.open(os.path.join(picdir, '2in13.bmp'))
        # epd.display(epd.getbuffer(image))
        # time.sleep(2)
        
        # # read bmp file on window
        # logging.info("3.read bmp file on window...")
        # # epd.Clear(0xFF)
        # image1 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
        # bmp = Image.open(os.path.join(picdir, '100x100.bmp'))
        # image1.paste(bmp, (2,2))    
        # epd.display(epd.getbuffer(image1))
        # time.sleep(2)


        logging.info("2.Combine TEXT...")

        time_image = Image.new('1', (epd.height, epd.width), 255)
        time_draw = ImageDraw.Draw(time_image)

        image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
        draw = ImageDraw.Draw(image)

        
        epd.init(epd.FULL_UPDATE)

        num = 0


        time_draw.text((0, 107), str(num)+'Bottom font15', font = font12, fill = 0)

        epd.displayPartBaseImage(epd.getbuffer(time_image))

        
        epd.init(epd.PART_UPDATE)


        # draw.text((0, 107), 'Bottom font15', font = font15, fill = 0)

        currtemttime = 0
        
        while (True):
            # while(s.recvfrom(1024)[0].decode('gb2312')!='exit'):
            time_draw.rectangle((0, 0, 125, 61), fill = 255)
            time_draw.rectangle((126, 62, 250, 122), fill = 255)
            time_draw.text((0, 0), str(num)+u'次', font = font12, fill = 0)
            # time_draw.text((10, 13), u'新世紀エヴァンゲリオン', font = font16, fill = 0)
            time_draw.text((10, 13),recv_msg, font = font16, fill = 0)
            # print(recv_msg+' Thread 2')
            # logging.info(recv_msg)
            # time_draw.text((0, 40), '', font = font12, fill = 0)
            time_draw.text((126, 62), time.strftime('%H:%M:%S'), font = font16, fill = 0)
            # edp.displayPartial
            # logging.info(str(time.time()))

            epd.displayPartial(epd.getbuffer(time_image))
            time.sleep(2)
            num = num + 1
            # print(recv_msg)
            # if(num == 5):
            #     break
            if(recv_msg.endswith('bye')):
                break



        
        # # partial update
        # logging.info("4.show time...")
        # time_image = Image.new('1', (epd.height, epd.width), 255)
        # time_draw = ImageDraw.Draw(time_image)
        
        # epd.init(epd.FULL_UPDATE)
        # epd.displayPartBaseImage(epd.getbuffer(time_image))
        
        # epd.init(epd.PART_UPDATE)
        # num = 0
        # while (True):
        #     time_draw.rectangle((120, 8020, 80), time.strftime('%H:%M:%S'), font = font24, fill = 0)
        #     epd.displayPartial(epd.getbuffer(time_image)), 220, 105), fill = 255)
        #     time_draw.text((1
        #     num = num + 1
        #     if(num == 5):
        #         break
        
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


# t1 = Thread(target=recv_data)
t2 = Thread(target=displaymain)
# t3 = Thread(target=info_main)
# t1.start()
logging.info("监听已启动")
t2.start()
info_main()
# t3.start()
# t1.join()
# t2.join()

