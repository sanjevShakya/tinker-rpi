from gpiozero import LED, PWMLED, Button, Buzzer, MotionSensor, LightSensor, MCP3008
from signal import pause
import _thread

led = LED(17)
pwm_led = PWMLED(21)
button = Button(2)
buzzer = Buzzer(26)
pir = MotionSensor(19)
lightSensor = LightSensor(13)
pot = MCP3008(channel=0)


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


def button_motion_handling():
    pwm_led.source = lightSensor
    print('Light Sensor value', lightSensor.value)
    print('Pot Value', pot.value)
    button.when_pressed = button_pressed
    button.when_released = button_released
    pir.when_motion = when_motion
    pir.when_no_motion = when_no_motion
    pause()


def main_loop():
    current_pot_value = pot.value
    while True:
        if(current_pot_value != pot.value):
            print('Pot value changed', pot.value)
            current_pot_value = pot.value


try:
    _thread.start_new_thread(main_loop)
    _thread.start_new_thread(button_motion_handling)
except:
    print("Error: Unable to start thread")

while 1:
    pass
