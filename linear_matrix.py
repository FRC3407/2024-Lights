import pixelstrip
import board 
from colors import *
import math
import random

class Coder(pixelstrip.Animation):
    def line(self, strip, y, length):
        for i in range(length):
                if y-i >= 0 and y-i <= strip.n:
                    if i == 0:
                        strip[y-i] = (0, 0, 0, 0)                   
                    if i < length/2 and not i == 0:
                        strip[y-i] = (0, int(abs(0.5*5*math.cos(math.pi*i/(length*0.1)))), 0, 0)
                    if i == length/2:
                        strip[y-i] = (0, 15, 0, 0)
                    if i > length/2:
                        strip[y-i] = (int(abs(0.5*math.cos(math.pi*i/(length*0.1)))), 15, int(abs(0.5*5*math.cos(math.pi*i/(length*0.1)))), 0)
 
    def __init__(self):
        self.yPos = [3,2,4,5]
        self.length = []
        self.timeout = 0.0
        self.length.append(random.randrange(0, 1))
        self.length.append(random.randrange(0, 1))
        self.length.append(random.randrange(0, 1))
        self.length.append(random.randrange(0, 1))
        
    def reset(self, strip):
        self.timeout = 0.0

    def draw(self, strip, delta_time):
        if self.is_timed_out():
            stuff = 0
            while stuff<len(self.yPos):
                if self.yPos[stuff] >= 0 and self.yPos[stuff] < strip.n:
                    self.line(strip, self.yPos[stuff], self.length[stuff])
                    self.yPos[stuff] = self.yPos[stuff] - 1
                elif stuff in self.yPos:
                    self.yPos.append(random.randrange(0, strip.n))
                    self.length.append(random.randrange(1, strip.n))
                    self.length.pop(stuff)
                    self.yPos.pop(stuff)
                    stuff -= 1
                stuff += 1
            self.timeout = 0.1
            strip.show()


if __name__ == "__main__":
    strip = pixelstrip.PixelStrip(board.D12, 24, bpp=4, pixel_order=pixelstrip.GRB)
    strip.timeout = 0.7

    strip.animation = Coder()

    while True:
        strip.draw()
