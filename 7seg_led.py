from time import sleep

from gpiozero import LEDCharDisplay

char_display = LEDCharDisplay(16, 12, 25, 8, 7, 20, 21)

while True:
    for c in "987654321 ":
        char_display.value = c
        sleep(0.5)
