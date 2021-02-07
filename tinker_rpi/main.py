from gpiozero import LED, PWMLED, Button, Buzzer, MotionSensor, LightSensor
from signal import pause

led = LED(17)
pwm_led = PWMLED(21)
button = Button(2)
buzzer = Buzzer(26)
pir = MotionSensor(19)
lightSensor = LightSensor(13)

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

print('Light Sensor value', lightSensor.value);

led.source = lightSensor

button.when_pressed = button_pressed
button.when_released = button_released
pir.when_motion = when_motion
pir.when_no_motion = when_no_motion

pause()