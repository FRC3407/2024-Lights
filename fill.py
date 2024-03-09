import pixelstrip
import board 
from colors import *
import math
import random


class Fill(pixelstrip.Animation):
    def __init__(self, color):
        self.color = color
        
    def reset(self, strip):
        self.timeout = 0.0
        strip.fill(self.color)

    def draw(self, strip, delta_time):
        if self.is_timed_out():
            strip.show()
            strip.timeout = 1

if __name__ == "__main__":
    strip = pixelstrip.PixelStrip(board.D12, 8, bpp=4, pixel_order=pixelstrip.GRB)
    strip.timeout = 0.7

    strip.animation = Fill(color= (0, 255, 0))

    while True:
        strip.draw()
