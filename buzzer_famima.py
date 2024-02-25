from time import sleep

from gpiozero import TonalBuzzer
from gpiozero.tones import Tone

BPM = 80

b = TonalBuzzer(17)


def play_sound(devide: int, tone: str | None = None):
    if tone is not None:
        b.play(Tone(tone))
    else:
        b.stop()
    sleep((60 / BPM) / (devide / 4))


def main():
    play_sound(8, "F#5")  # ファ
    play_sound(8, "D5")  # レ
    play_sound(8, "A4")  # ラ
    play_sound(8, "D5")  # レ
    play_sound(8, "E5")  # ミ
    play_sound(8, "A5")  # ラ
    play_sound(8)
    play_sound(8, "E4")  # ミ
    play_sound(8, "E5")  # ミ
    play_sound(8, "F#5")  # ファ
    play_sound(8, "E5")  # ミ
    play_sound(8, "A4")  # ラ
    play_sound(4, "D5")  # レ


if __name__ == "__main__":
    main()
