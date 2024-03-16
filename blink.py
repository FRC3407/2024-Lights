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
        self.states = {0: State(0, True, 1, 0.132), 
                       1: State(1, False, 2, 0.132), 
                       2: State(2, True, 3, 0.132), 
                       3: State(3, False, 4, 0.132), 
                       4: State(4, True, 5, 1000),
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

if __name__ == "__main__":
    matrix = pixelstrip.PixelStrip(board.GP15, width=8, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_TOP, pixelstrip.MATRIX_LEFT, pixelstrip.MATRIX_ZIGZAG, pixelstrip.MATRIX_COLUMN_MAJOR})
    matrix.animation = StripeAnimation()
    while True:
        matrix.draw()