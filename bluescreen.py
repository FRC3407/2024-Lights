import pixelstrip
import board
from colors import *



class BlueScreen(pixelstrip.Animation):
    def __init__(self):
        pixelstrip.Animation.__init__(self)

    def reset(self, matrix):
        self.timeout = 0.0
    
    def fill(self, r, g, b):
        for i in range(matrix.width):
            for o in range(matrix.height):
                matrix[i, o] = (r, g, b, 0)

    def draw(self, matrix, delta_time):
        if self.is_timed_out():
            self.fill(0, 0, 255)
            matrix.show()

matrix = pixelstrip.PixelStrip(board.D12, width=8, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_TOP, pixelstrip.MATRIX_LEFT, pixelstrip.MATRIX_ZIGZAG, pixelstrip.MATRIX_COLUMN_MAJOR})
matrix.animation = BlueScreen()
while True:
    matrix.draw()
