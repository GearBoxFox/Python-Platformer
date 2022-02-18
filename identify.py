from PIL import Image
import os.path
import sys

if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    sys.exit('Syntax: identify.py [filename]')

pic = sys.argv[1]
img = Image.open(pic)
x = img.size[0]
y = img.size[1]

print(x, y)