# gpiozeroを使って、adコンバーターの値を読み取るサンプルを実装する
from gpiozero import MCP3002

adc = MCP3002(channel=0)


def main():
    while True:
        adc_value = adc.value
        print(adc_value)


if __name__ == "__main__":
    main()
