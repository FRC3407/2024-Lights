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
from noise import noise

# This is run for every pixel and returns a color, the t value is the time in seconds since the animation started
# The x and y values go from 0 to 1
def pix(x,y,t) -> Tuple:
    r = noise(x*2+t+10000,y*2)*255
    g = noise(x*2+t+20000,y*2)*255
    b = noise(x*2+t+30000,y*2)*255
    return (r,g,b)

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
            for y in range(matrix.height):
                for x in range(matrix.width):
                    matrix[x,y]=pix(x/matrix.width,y/matrix.height,relative_time)


            matrix.show()
            self.timeout = 0.0
            
                



if __name__ == "__main__":
    matrix = pixelstrip.PixelStrip(board.GP15, width=8, height=11, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_TOP, pixelstrip.MATRIX_LEFT, pixelstrip.MATRIX_ZIGZAG, pixelstrip.MATRIX_COLUMN_MAJOR}, brightness=0.4)
    matrix.timeout = 0.7

    matrix.animation = Flash()

    print("i am alive!")

    while True:
        matrix.draw()
