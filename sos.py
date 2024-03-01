import pixelstrip
import board
from colors import *

class State:
    def __init__(self, s, light_on, next_state, timeout):
        self.s = s
        self.light_on = light_on
        self.next_state = next_state
        self.timeout = timeout


class StripeAnimation(pixelstrip.Animation):
    def __init__(self):
        pixelstrip.Animation.__init__(self)
        self.s = 0
        self.states = {0: State(0, False, 1, 0.5), 
                       1: State(1, True, 2, 0.132), 
                       2: State(2, False, 3, 0.132), 
                       3: State(3, True, 4, 0.132), 
                       4: State(1, False, 5, 0.132), 
                       5: State(1, True, 6, 0.132), 
                       6: State(1, False, 7, 0.2), 
                       7: State(1, True, 8, 0.396), 
                       8: State(1, False, 9, 0.132), 
                       9: State(1, True, 10, 0.396), 
                       10: State(1, False, 11, 0.132), 
                       11: State(1, True, 12, 0.396), 
                       12: State(1, False, 13, 0.132), 
                       13: State(1, True, 14, 0.132), 
                       14: State(1, False, 15, 0.132), 
                       15: State(1, True, 16, 0.132), 
                       16: State(1, False, 17, 0.132), 
                       17: State(1, True, 18, 0.132), 
                       18: State(1, False, 0, 0.132), 
                       }

    def reset(self, matrix):
        self.timeout = 0.0

    def draw(self, matrix, delta_time):
        if self.is_timed_out():
            state = self.states[self.s]

            if state.light_on:
                matrix.fill(WHITE)
            else:
                matrix.clear()
            matrix.show()
            self.s = state.next_state
            self.timeout = state.timeout

matrix = pixelstrip.PixelStrip(board.GP15, width=8, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_TOP, pixelstrip.MATRIX_LEFT, pixelstrip.MATRIX_ZIGZAG, pixelstrip.MATRIX_COLUMN_MAJOR})
matrix.animation = StripeAnimation()
while True:
    matrix.draw()