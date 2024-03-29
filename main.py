import digitalio
import board
from i2ctarget import I2CTarget
from pixelstrip import PixelStrip, current_time

from animation_pulse import PulseAnimation
from circle_spinner import *
import green_matrix
from fill import *
import conways_game_of_life
import linear_matrix
from circle_spinner import *
from orange_reverse_linear_matrix import *
from orange_reverse_matrix import *
from spin_flash import *
from animation_bitmap import *
from pointer import *
from flash import *

I2C_ADDRESS = 0x41
BRIGHTNESS = 1.0

# List of Animations
animation = [
    CircleSpinner(),
    CircleSpinner(),
    CircleSpinner(),

    linear_matrix.Coder(),
    linear_matrix.Coder(),
    linear_matrix.Coder(),

    green_matrix.Coder(),

    conways_game_of_life.Coder(),

    ReverseOrangeCoder(cycle_time=0.1),
    ReverseOrangeCoder(cycle_time=0.1),
    ReverseOrangeCoder(cycle_time=0.05),
    ReverseOrangeCoder(cycle_time=0.05),
    
    Flash(),

    Fill(color=RED),
    Fill(color=GREEN),
    Fill(color=WHITE),

    PulseAnimation(),

    Pointing()
    # Add way more animations here
]

# List of PixelStrips
strip = [
    PixelStrip(board.NEOPIXEL0, 144, bpp=4, pixel_order="GRB", brightness=BRIGHTNESS),
    PixelStrip(board.NEOPIXEL1, width=32, height=8, bpp=4, pixel_order="GRB", brightness=BRIGHTNESS, options={pixelstrip.MATRIX_TOP, pixelstrip.MATRIX_LEFT, pixelstrip.MATRIX_COLUMN_MAJOR, pixelstrip.MATRIX_ZIGZAG}),
    PixelStrip(board.NEOPIXEL2, width=8, height=8, bpp=4, pixel_order="GRB", brightness=BRIGHTNESS),
    PixelStrip(board.NEOPIXEL3, 24, bpp=4, pixel_order="GRB", brightness=BRIGHTNESS),
    PixelStrip(board.NEOPIXEL4, 24, bpp=4, pixel_order="GRB", brightness=BRIGHTNESS)
]

# The built-in LED will turn on for half a second after every message
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

i2c = I2CTarget(scl=board.SCL, sda=board.SDA, addresses=[I2C_ADDRESS])

# Receive one byte through I2C, if available
def receive_message():
    global i2c
    message = i2c.request()
    if message:
        b = message.read(n=1)[0]
        strip_num = int((b & 0xE0) >> 5)
        anim_num = int(b & 0x1F)
        return (strip_num, anim_num)
    else:
        return None

def main():
    global strip, led
    for s in strip:
        s.clear()
    strip[1].animation = animation[3]
    last_msg_time = 0.0
    while True:
        for s in strip:
            s.draw()
        message = receive_message()
        if message:
            strip_num = message[0]
            anim_num = message[1]
            if strip_num < len(strip) and anim_num < len(animation):
                strip[strip_num].animation = animation[anim_num]
                print(f"RECEIVE({strip_num},{anim_num})\n")
            elif strip_num < len(strip):
                strip[strip_num].animation = None
            last_msg_time = current_time()
        led.value = (current_time() < last_msg_time + 0.5)

main()