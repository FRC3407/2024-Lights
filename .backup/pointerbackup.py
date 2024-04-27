import pixelstrip
import board
from colors import *
import math



class Pointing(pixelstrip.Animation):
    def __init__(self):
        pixelstrip.Animation.__init__(self)
        self.a = 0
        self.xth = 0
        self.yth = 0

    def reset(self, matrix):
        self.timeout = 0.0

    def draw(self, matrix, delta_time):
        if self.is_timed_out():
            matrix.fill(0)
            self.pointer(self.a, matrix)
            self.a = self.a + 0.1
            matrix.show()
            self.timeout = 0.0


    
    def pointer(self, direction, matrix):
        # for y in range(matrix.height):
        #     for x in range(matrix.width):
        #         a=x
        #         if y%2==0:
        #             x = 7 - x
        #         matrix[x,y]=(a/8*50,y/8*50,0,0)
        for i in range(matrix.height/2+1):
            self.xth = i*math.sin(direction)+matrix.width/2
            self.yth = matrix.height/2 + i*math.cos(direction)
            if (int(self.xth) % 2) == 0:
                y = (matrix.height - 1) - self.yth
            else:
                y=self.yth
            if self.xth < matrix.width and self.xth > 0 and self.yth < matrix.height and self.yth > 0:
                matrix[int(y), int(self.xth)] = (255, 30, 0 ,0)
                continue
                for o in range(1, i):
                    if (int(self.xth+o)%2) == 0:
                        y = (matrix.height - 1) - self.yth
                        a = 0-o
                    else:
                        y = self.yth
                        a = o
                    if self.xth+o < matrix.width and self.xth + o > 0 and y < matrix.height and y > 0:
                        matrix[int(self.xth+o), int(y)] = (255, 30, 0 ,0)
                    if self.xth < matrix.width and self.xth > 0 and y + a < matrix.height and y + a > 0:
                        matrix[int(self.xth), int(y + a)] = (255, 30, 0 ,0)






# matrix = pixelstrip.PixelStrip(board.D12, width=8, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_TOP, pixelstrip.MATRIX_LEFT, pixelstrip.MATRIX_ZIGZAG, pixelstrip.MATRIX_COLUMN_MAJOR})
# matrix.animation = Pointing()
# while True:
#     matrix.draw()