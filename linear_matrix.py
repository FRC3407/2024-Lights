import pixelstrip
import board 
from colors import *
import math
import random

class Rainbow(pixelstrip.Animation):
    def fill(self, red, green, blue):
        for x in range(8):
            for y in range(8):
                strip[x,y] = (red, green, blue, 0)
    def __init__(self):
        strip.increment = 0
        pixelstrip.Animation.__init__(self)
        # self.color = GREEN
        self.timeout = 0.0
        self.row = 0
    def reset(self, strip):
        self.timeout = 0.0
    def draw(self, strip, delta_time):
        if self.is_timed_out():
            strip.increment = (strip.increment + .1) % (math.pi*3/2)
            if strip.increment <= math.pi/2:
                strip.color = strip.increment % (math.pi/2)
                self.fill(int(abs(math.cos(strip.color)*10)), 0, int(abs(math.sin(strip.color)*10)))
            elif strip.increment <= math.pi:
                strip.color = strip.increment%(math.pi/2)
                self.fill(0, int(abs(math.sin(strip.color)*10)), int(abs(math.cos(strip.color)*10)))
            else:
                strip.color = strip.increment% (math.pi/2)
                self.fill(int(abs(math.sin(strip.color)*10)), int(abs(math.cos(strip.color)*10)), 0)
            self.timeout = 0.001
            strip.show()



class Coder(pixelstrip.Animation):
    def line(self, y, length):
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
                    self.yPos[stuff] = self.yPos[stuff] - 1
            self.timeout = 0.1
            strip.show()


if __name__ == "__main__":
    strip = pixelstrip.PixelStrip(board.D12, 24, bpp=4, pixel_order=pixelstrip.GRB)
    strip.timeout = 0.7

    strip.animation = Coder()

    while True:
        strip.draw()
