import os
import sys
import display.main_display as md1
import net.main_conn as mc1
import wrcon
import time
import init as initial

def init():
    wrcon.write_config('main','枯荣大佬')
    wrcon.write_config('ip', initial.get_host_ip())


from threading import Thread


displaylib = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'display')
if os.path.exists(displaylib):
    sys.path.append(displaylib)
# time.sleep(10)
# print('测试成功了么')
init()
t1 = Thread(target=mc1.info_main)
t2 = Thread(target=md1.displaypro)

t2.start()
t1.start()


