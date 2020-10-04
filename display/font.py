import os
import sys
from PIL import Image, ImageDraw, ImageFont

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
font16 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 16)
font12 = ImageFont.truetype(os.path.join(picdir, 'Font1.otf'), 12)
