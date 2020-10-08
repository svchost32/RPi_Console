from socket import *
import socket as soc
from threading import Thread
import os
import wrcon
sockets = []


def info_main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(soc.SOL_SOCKET,soc.SO_REUSEADDR,1)
    server_socket.bind(('', 8200))
    server_socket.listen()
    # print('开始监听')

    while True:
        client_socket, client_info = server_socket.accept()
        sockets.append(client_socket)
        t = Thread(target=readMSG, args=(client_socket,))
        t.start()


def readMSG(client_socket):
    while True:
        try:
            recv_data = client_socket.recv(1024)
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
                recv_msg = recv_data.decode('utf-8').split(',')
                wrcon.write_config(recv_msg[0],recv_msg[1])
                # socket.send(('已收到:'+recv_data.decode('utf-8')).encode('utf-8'))


