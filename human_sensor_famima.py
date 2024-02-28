from time import sleep

from gpiozero import MotionSensor, TonalBuzzer
from gpiozero.tones import Tone

BPM = 80

motion_senser = MotionSensor(4)
b = TonalBuzzer(17)


def play_sound(devide: int, tone: str | None = None):
    if tone is not None:
        b.play(Tone(tone))
    else:
        b.stop()
    sleep((60 / BPM) / (devide / 4))


def play_famima_sound():
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
    play_sound(4)


def main():
    i = 0

    while True:
        i = i + 1

        if not motion_senser.motion_detected:
            play_famima_sound()

        print(f"motion! {motion_senser.motion_detected}")

        sleep(0.5)
    """

    motion_senser.when_motion = play_famima_sound
    motion_senser.when_no_motion = play_famima_sound
    pause()
    """

    """
    play_famima_sound()
    motion_senser.wait_for_motion()
    print("Motion!")
    motion_senser.when_motion = play_famima_sound
    pause()
    """


if __name__ == "__main__":
    main()

    b = 1
