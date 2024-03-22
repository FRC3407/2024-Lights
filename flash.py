"""
 _________________________________
/  __  __                         \
| |  \/  | ___   ___              |
| | |\/| |/ _ \ / _ \             |
| | |  | | (_) | (_) |            |
| |_|  |_|\___/ \___/             |
|                                 |
\ This code was written by CalSch /
 ---------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""
import pixelstrip
import board 
from colors import *
import math
import random
import time

FLASH_DURATION = 0.3
BLANK_DURATION = 0.2
BLINK_TIME = FLASH_DURATION + BLANK_DURATION
MAX_TIME = FLASH_DURATION*3 + BLANK_DURATION*3

COLORS = [
    (2,6,20,0),
    (2,6,20,0),
    (25,4,1,0),
]

class Flash(pixelstrip.Animation):
    def __init__(self):
        self.start_time = time.monotonic()
        self.timeout = 0.0
        pixelstrip.Animation.__init__(self)

    def reset(self, strip):
        self.timeout = 0.0

    def draw(self, matrix, delta_time):
        if self.is_timed_out():
            relative_time = time.monotonic() - self.start_time
            matrix.fill((0,0,0,0))
            
            t = relative_time%BLINK_TIME
            blink = int(relative_time/BLINK_TIME)
            # print(blink)
            if t > BLANK_DURATION and relative_time < MAX_TIME: # Flash on
                color = COLORS[blink]
                print(color)
                matrix.fill(color)
                # matrix[5]=(255,255,255,0)
                print("horray!")


            matrix.show()
            self.timeout = 0.05
            
                



if __name__ == "__main__":
    matrix = pixelstrip.PixelStrip(board.GP15, width=8, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_TOP, pixelstrip.MATRIX_LEFT, pixelstrip.MATRIX_ZIGZAG, pixelstrip.MATRIX_COLUMN_MAJOR})
    matrix.timeout = 0.7

    matrix.animation = Flash()

    print("i am alive!")

    while True:
        matrix.draw()
