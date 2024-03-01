import pixelstrip
import board 
from colors import *
import math
import random





class ReverseOrangeCoder(pixelstrip.Animation):
    def line(self, x, y, length):
        for i in range(length):
            if x <= matrix.width and x >= 0:
                if y-i >= 0 and y-i <= matrix.height:
                    if i == 0:
                        matrix[x, y-i] = (0, 0, 0, 0)
                    else:
                        matrix[x, y-i] = (255, 30, 0, 0)
    def __init__(self):
        self.xPos = []
        self.yPos = []
        self.length = []
        self.timeout = 0.0
        self.xPos.append(random.randrange(0, matrix.width-1))
        self.yPos.append(random.randrange(0, matrix.height+7))
        self.length.append(random.randrange(0, 7))
    def reset(self, matrix):
        self.timeout = 0.0

    def draw(self, matrix, delta_time):
        if self.is_timed_out():
            matrix.fill(0)
            for i in range(matrix.width/3):
                self.xPos.append(random.randrange(0, matrix.width))
                self.yPos.append(random.randrange(-7, matrix.height+1))
                self.length.append(random.randrange(0, 7))
            for stuff in range(len(self.xPos)):
                if self.yPos[stuff] >= 0:
                    self.line(self.xPos[stuff], self.yPos[stuff], self.length[stuff])
                    self.yPos[stuff] = self.yPos[stuff] + 1
            self.timeout = 0.1
            matrix.show()

matrix = pixelstrip.PixelStrip(board.D12, width=32, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_TOP, pixelstrip.MATRIX_LEFT, pixelstrip.MATRIX_COLUMN_MAJOR, pixelstrip.MATRIX_ZIGZAG})
matrix.timeout = 0.7

matrix.animation = ReverseOrangeCoder()

while True:
    matrix.draw()
