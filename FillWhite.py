import pixelstrip
import board 
from colors import *


class FillWhite(pixelstrip.Animation):
    def __init__(self):
        pass
    def reset(self, strip):
        self.timeout = 0.0
        strip.fill(WHITE)


    def draw(self, strip, delta_time):
        if self.is_timed_out():
            strip.show()

if __name__ == "__main__":
    strip = pixelstrip.PixelStrip(board.D12, 8, bpp=4, pixel_order=pixelstrip.GRB)
    strip.timeout = 0.7

    strip.animation = FillWhite()

    while True:
        strip.draw()
