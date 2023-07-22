'''
Variables
'''

import os


worldx = 960
worldy = 720

fps = 40  # frame rate
ani = 4  # animation cycles

main = True

ALPHA = (0, 255, 0)

gloc = []
tx = 64
ty = 64

forwardsx = 600
backwardsx = 230
# put variables here


font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         "fonts", "fantasquebold.ttf")
font_size = tx

# Level data
box_platforms = [
    []
]
