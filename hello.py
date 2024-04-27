import pixelstrip
import board 
from colors import *
import math
import random


class HelloWorld(pixelstrip.Animation):
    def __init__(self):
        pass

    def reset(self, strip):
        strip.timeout = 2.0
        strip.load_font("fonts/proggy_tiny_12pt.bdf")
        strip.clear()


    def draw(self, strip, delta_time):
        if self.is_timed_out():
            strip.draw_text("Hello")
            strip.clear()
            strip.draw_text("World")
            strip.clear()

if __name__ == "__main__":
    strip = pixelstrip.PixelStrip(board.D12, 8, bpp=4, pixel_order=pixelstrip.GRB)
    strip.timeout = 0.7

    strip.animation = HelloWorld()

    while True:
        strip.draw()
