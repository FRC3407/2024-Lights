import pixelstrip
import board 
from colors import *
import math
import random


class Fill(pixelstrip.Animation):
    def __init__(self, color):
        pass
    def reset(self, strip, color, delta_time):
        strip.fill(color)

    def draw(self, strip, delta_time):
        if self.is_timed_out():
            strip.show()

if __name__ == "__main__":
    strip = pixelstrip.PixelStrip(board.D12, 8, bpp=4, pixel_order=pixelstrip.GRB)
    strip.timeout = 0.7

    strip.animation = Fill(color= (0, 255, 0))

    while True:
        strip.draw()
