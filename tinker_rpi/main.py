from gpiozero import LED, Button, Buzzer
from signal import pause

led = LED(17)
button = Button(2)
buzzer = Buzzer(26)

def button_pressed():
    led.on()
    buzzer.on()


def button_released():
    led.off()
    buzzer.off()

button.when_pressed = button_pressed
button.when_released = button_released

pause()