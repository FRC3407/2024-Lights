import pixelstrip
import board 
from colors import *
import math
import random


class CircleSpinner(pixelstrip.Animation):
    def line(self,strip, y, length):
        for i in range(length):
                if y+i >= 0 and y+i < strip.n:
                    strip[y+i] = (255, 30, 0 ,0)
    def __init__(self):
        self.pos = 0
    def reset(self, strip):
        self.timeout = 0.0

    def draw(self, strip, delta_time):
        if self.is_timed_out():
            strip.fill(0)
            self.line(strip, self.pos, strip.n/3)
            self.pos = (self.pos+1) % strip.n 
            self.timeout = 0.1
            strip.show()


if __name__ == "__main__":
    strip = pixelstrip.PixelStrip(board.D12, 8, bpp=4, pixel_order=pixelstrip.GRB)
    strip.timeout = 0.7

    strip.animation = CircleSpinner()

    while True:
        strip.draw()
