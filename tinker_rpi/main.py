from gpiozero import LED, Button
from time import sleep


led = LED(17)
button = Button(18)

def main():
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)