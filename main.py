import digitalio
import board
from time import sleep
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
from orange_reverse_matrix import ReverseOrangeCoder
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
    CircleSpinner(), #2

    linear_matrix.Coder(), # 3
    linear_matrix.Coder(), # 4
    linear_matrix.Coder(), # 5
    # PulseAnimation([GREEN, BLACK, DARKSLATEGRAY]), # 3
    # PulseAnimation([GREEN, BLACK, DARKSLATEGRAY]), # 4
    # PulseAnimation([GREEN, BLACK, DARKSLATEGRAY]), # 5

    # PulseAnimation([ORANGE, BLACK, YELLOW]), #6
    green_matrix.Coder(), #6

    conways_game_of_life.Coder(), #7

    # PulseAnimation([ORANGE, BLACK, YELLOW]), #8
    # PulseAnimation([ORANGE, BLACK, YELLOW]), #9
    # PulseAnimation([ORANGE, BLACK, YELLOW]), #10
    # PulseAnimation([ORANGE, BLACK, YELLOW]), #11
     ReverseOrangeCoder(cycle_time=0.05), #8
     ReverseOrangeCoder(cycle_time=0.05), #9
     ReverseOrangeCoder(cycle_time=0.01), #10
     ReverseOrangeCoder(cycle_time=0.01), #11
    
    Flash(), #12

    Fill(color=RED), #13
    Fill(color=GREEN), #14
    Fill(color=WHITE), #15

    PulseAnimation([GREEN, DARKSLATEGRAY]), #16

    # green_matrix.Coder() #17
    # linear_matrix.Coder(), #18
    # ReverseOrangeCoder(cycle_time=0.1), #19
    # LinearOrangeCoder(cycle_time=0.1) #20

    Pointing() #17
    # # Add way more animations here
]

# List of PixelStrips
strip = [
    PixelStrip(board.NEOPIXEL0, 144, bpp=4, offset=1, pixel_order="GRB", brightness=BRIGHTNESS),
    PixelStrip(board.NEOPIXEL1, width=32, offset=1, height=8, bpp=4, pixel_order="GRB", brightness=BRIGHTNESS, options={pixelstrip.MATRIX_TOP, pixelstrip.MATRIX_LEFT, pixelstrip.MATRIX_COLUMN_MAJOR, pixelstrip.MATRIX_ZIGZAG}),
    PixelStrip(board.NEOPIXEL2, width=8, offset=1, height=8, bpp=4, pixel_order="GRB", brightness=BRIGHTNESS),
    PixelStrip(board.NEOPIXEL3, 24, bpp=4, offset=1, pixel_order="GRB", brightness=BRIGHTNESS),
    PixelStrip(board.NEOPIXEL4, 24, bpp=4, offset=1, pixel_order="GRB", brightness=BRIGHTNESS)
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
        print(f"received {(strip_num, anim_num)}")
        return (strip_num, anim_num)
    else:
        return None

def main(): 
    global strip, led
    blink(3)
    print("HELLO")
    # strip[2].animation = animation[20]
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
            print(f"RECEIVE({strip_num}, {anim_num})\n")
        led.value = (current_time() < last_msg_time + 0.5)

def blink(n, color=BLUE, sleep_time=0.4): 
    """Blink lights to show that the program has loaded successfully"""
    global strip
    for s in strip:
        s.clear()
    for _ in range(n):
        for s in strip:
            s[0] = color
            s.show()
        sleep(sleep_time)
        for s in strip:
            s.clear()
            s.show()
        sleep(sleep_time)


if __name__ == "__main__":
    main()
