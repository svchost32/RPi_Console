import os
import sys
import displaytest as md1
import main_conn as mc1
import wrcon

def init():
    wrcon.write_config('main','Waiting For DATA UPDate')


from threading import Thread


displaylib = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'display')
if os.path.exists(displaylib):
    sys.path.append(displaylib)

# print('测试成功了么')
init()
t1 = Thread(target=mc1.info_main)
t2 = Thread(target=md1.displaymain)

t2.start()
t1.start()


