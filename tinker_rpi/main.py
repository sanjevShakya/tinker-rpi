from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

def led_on():
    led.on()

def led_off():
    led.off()

button.when_pressed = led_on
button.when_released = led_off

pause()