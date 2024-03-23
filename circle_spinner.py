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
        self.b = 1
        self.pos = 0
        self.t = 0.05
        self.timeout = 0.05
    def reset(self, strip):
        self.timeout = 0.0

    def draw(self, strip, delta_time):
        if self.is_timed_out():
            strip.fill(0)
            self.line(strip, self.pos, strip.n/27)
            self.pos = (self.pos+self.b) % strip.n
            if self.t != 0.0:
                if self.pos == 24:
                    self.t = self.t - 0.01
            elif self.pos == 24 and self.b < 7:
                self.b = self.b + 1
            # elif self.pos == 24 and self.b > 1:
            #     self.b = self.b - 1
            # elif self.b == 1 and self.pos == 0:
            #     self.t = self.t + 0.01
            #     self.timeout = self.t

            print(self.t)
            
            self.timeout = self.t

            strip.show()


if __name__ == "__main__":
    strip = pixelstrip.PixelStrip(board.D12, 8, bpp=4, pixel_order=pixelstrip.GRB)
    strip.timeout = 0.05

    strip.animation = CircleSpinner()

    while True:
        strip.draw()
