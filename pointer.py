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
            x = self.xth
            self.yth = matrix.height/2 + i*math.cos(direction)
            if self.yth % 2 == 0:
                self.xth = (matrix.width - 1) - self.xth
            if self.xth < matrix.width and self.xth > 0 and self.yth < matrix.height and self.yth > 0:
                # matrix[int(self.xth), int(self.yth)] = (255, 30, 0 ,0)
                matrix[int(self.xth), int(self.yth)] = (255, 30, 0 ,0)
                continue
                for o in range(1, i):
                    if self.xth+o < matrix.width and self.xth + o > 0 and self.yth < matrix.height and self.yth > 0:
                        matrix[int(self.xth+o), int(self.yth)] = (255, 30, 0 ,0)
                    if self.xth < matrix.width and self.xth > 0 and self.yth + o < matrix.height and self.yth + o > 0:
                        matrix[int(self.xth), int(self.yth + o)] = (255, 30, 0 ,0)






# matrix = pixelstrip.PixelStrip(board.D12, width=8, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_TOP, pixelstrip.MATRIX_LEFT, pixelstrip.MATRIX_ZIGZAG, pixelstrip.MATRIX_COLUMN_MAJOR})
# matrix.animation = Pointing()
# while True:
#     matrix.draw()