import os
import sys
import displaytest as main_display
displaylib = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'display')
if os.path.exists(displaylib):
    sys.path.append(displaylib)

print (displaylib)

main_display.threadtest()