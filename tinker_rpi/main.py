from gpiozero import LED, Button, Buzzer, MotionSensor
from signal import pause

led = LED(17)
button = Button(2)
buzzer = Buzzer(26)
pir = MotionSensor(19)

def button_pressed():
    led.on()
    buzzer.on()


def button_released():
    led.off()
    buzzer.off()

def when_motion():
    print('Motion detected')

def when_no_motion():
    print('No motion available')

button.when_pressed = button_pressed
button.when_released = button_released
pir.when_motion = when_motion
pir.when_no_motion = when_no_motion

pause()