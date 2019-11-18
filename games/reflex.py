# Simple reflex testing game for micro:bit
# Copyright (c) Alexis Brandner 2019 - http://github.com/Alexinfos/microbitscripts/
# Created on nov. 14th, 2019
from microbit import *
from random import randint
from time import ticks_ms

while True:
    display.set_pixel(2,2,9)
    sleep(randint(1000,4000))
    
    # If the button is pressed before the LED goes off, it probably means that the player is trying to cheat
    cheated = button_a.is_pressed()
    display.set_pixel(2,2,0)
    
    # Counts time between the moment the LED goes off and the moment the player presses the button
    timer_start = ticks_ms()
    while not (button_a.is_pressed() or button_b.is_pressed()):
        continue
    timer_end = ticks_ms()
    
    # If the player cheated, it displays a blinking x and a message. If not, it shows the time elapsed in milliseconds
    if not cheated:
        for i in range(0,2):
            display.scroll(str(timer_end - timer_start) + "ms", wait=True)
    else:
        for i in range(0,10):
            display.show(Image.NO)
            sleep(100)
            display.clear()
            sleep(100)
        display.scroll("You cheated!")

    display.show(Image.ARROW_E)
    # Resets screeen and waits for the button b to be pressed before starting a new game
    while not button_b.is_pressed():
        continue
    display.clear()
    sleep(1000)
