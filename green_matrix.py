import pixelstrip
import board 
from colors import *
import math
import random

class Coder(pixelstrip.Animation):
    def line(self, x, y, length, matrix):
        for i in range(length):
            if x < matrix.width and x >= 0:
                if y-i >= 0 and y-i < matrix.height-1:
                    if i == 0:
                        matrix[x, y-i] = (0, 0, 0, 0)                   
                    if i < length/2 and not i == 0:
                        matrix[x, y-i] = (0, int(abs(0.5*5*math.cos(math.pi*i/(length*0.1)))), 0, 0)
                    if i == length/2:
                        matrix[x, y-i] = (0, 15, 0, 0)
                    if i > length/2:
                        matrix[x, y-i] = (int(abs(0.5*math.cos(math.pi*i/(length*0.1)))), 15, int(abs(0.5*5*math.cos(math.pi*i/(length*0.1)))), 0)
    def __init__(self):
        self.xPos = [2,5,7]
        self.yPos = [4,3,2]
        self.length = []
        self.timeout = 0.0
        self.length.append(random.randrange(0, 7))
        self.length.append(random.randrange(0, 7))
        self.length.append(random.randrange(0, 7))
    def reset(self, matrix):
        self.timeout = 0.0

    def draw(self, matrix, delta_time):
        if self.is_timed_out():
            stuff=0
            while stuff<len(self.yPos):
                print("-------")
                print(stuff)
                print(self.yPos)
                print(self.yPos[stuff])
                if self.yPos[stuff] >= 0 or self.yPos[stuff] < matrix.height:
                    self.line(self.xPos[stuff], self.yPos[stuff], self.length[stuff], matrix)
                    self.yPos[stuff] = self.yPos[stuff] - 1
                else:
                    self.yPos.pop(stuff)
                    self.xPos.pop(stuff)
                    self.length.pop(stuff)
                    stuff -= 1
                    self.xPos.append(random.randrange(0, matrix.width))
                    self.yPos.append(random.randrange(0, matrix.height+7))
                    self.length.append(random.randrange(1, 8))
                stuff += 1
            self.timeout = 0.1
            matrix.show()


if __name__ == "__main__":
    matrix = pixelstrip.PixelStrip(board.D12, width=32, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_TOP, pixelstrip.MATRIX_LEFT, pixelstrip.MATRIX_COLUMN_MAJOR, pixelstrip.MATRIX_ZIGZAG})
    matrix.timeout = 0.7

    matrix.animation = Coder()

    while True:
        matrix.draw()
