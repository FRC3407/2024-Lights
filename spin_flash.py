import pixelstrip
import board 
from colors import *
import math
import random


class SpinFlash(pixelstrip.Animation):
    def line(self, y, length):
        for i in range(length):
                if y+i >= 0 and y+i < strip.n:
                    strip[y+i] = (255, 30, 0 ,0)
    def __init__(self):
        self.pos = 0
        self.time = 0
    def reset(self, strip):
        self.timeout = 0.0

    def draw(self, strip, delta_time):
        if self.is_timed_out():
            self.time = self.time + 1
            if self.time <= 20 or self.time > 30:
                strip.fill(0)
                self.line(self.pos, strip.n/3)
                self.pos = (self.pos+1) % strip.n 
                self.timeout = 0.1
                strip.show()
            else:
                strip.fill((255, 255, 255))
                strip.show()
                



if __name__ == "__main__":
    strip = pixelstrip.PixelStrip(board.D12, 8, bpp=4, pixel_order=pixelstrip.GRB)
    strip.timeout = 0.7

    strip.animation = SpinFlash()

    while True:
        strip.draw()
