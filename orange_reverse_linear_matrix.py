import pixelstrip
import board 
from colors import *
import math
import random


class Coder(pixelstrip.Animation):
    def line(self, y, length):
        for i in range(length):
                if y-i >= 0 and y-i < strip.n:
                    print(f"y={y}\ni={i}\n")
                    if i == 0:
                        strip[y-i] = (0, 0, 0, 0)
                    else: 
                        strip[y-i] = (255, 30, 0 ,0)
    def __init__(self):
        self.yPos = []
        self.length = []
        self.timeout = 0.0
        self.yPos.append(random.randrange(0, strip.n+7))
        self.length.append(random.randrange(0, 7))
    def reset(self, strip):
        self.timeout = 0.0

    def draw(self, strip, delta_time):
        if self.is_timed_out():
            for i in range(strip.n/20):
                self.yPos.append(random.randrange(0, strip.n))
                self.length.append(random.randrange(1, strip.n))
            for stuff in range(len(self.yPos)):
                if self.yPos[stuff] >= 0:
                    self.line(self.yPos[stuff], self.length[stuff])
                    self.yPos[stuff] = self.yPos[stuff] + 1
            self.timeout = 0.01
            strip.show()


if __name__ == "__main__":
    strip = pixelstrip.PixelStrip(board.D12, 8, bpp=4, pixel_order=pixelstrip.GRB)
    strip.timeout = 0.7

    strip.animation = Coder()

    while True:
        strip.draw()
