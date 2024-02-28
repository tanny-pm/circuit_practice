from random import uniform
from signal import pause
from sys import exit
from time import sleep

from gpiozero import LED, Button

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input("Left player name is ")
right_name = input("Right player name is ")

led.on()
sleep(uniform(5, 10))
led.off()


def pressed(button):
    if button.pin.number == 14:
        print(f"{left_name} won the game!")
    else:
        print(f"{right_name} won the game!")
    exit()


right_button.when_pressed = pressed
left_button.when_pressed = pressed

pause()
