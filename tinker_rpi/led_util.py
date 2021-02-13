from gpiozero import LED
from time import sleep


class LEDUtil:
    def __init__(self, led_pins):
        self.led_pins = led_pins
        self.leds = []
        self.initialize_leds()

    def initialize_leds(self):
        for led_pin in self.led_pins:
            self.leds.append(LED(led_pin))

    def led_ready_dark_sequence(self):
        for led in self.leds:
            led.on()

    def led_alarm_sequence(self):
        for led in self.leds:
            led.on()
        sleep(0.2)
        for led in self.leds:
            led.off()
        sleep(0.2)

    def led_ready_light_sequence(self):
        self.leds[0].on()
        self.leds[1].off()
        self.leds[2].off()
        self.leds[3].on()

    def led_dark_sequence(self):
        for led in self.leds:
            led.on()

    def led_surveillance_sequence(self):
        for led in self.leds:
            led.on()
            sleep(0.2)
            led.off()
            sleep(0.2)
