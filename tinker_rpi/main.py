from gpiozero import LED, Buzzer, LightSensor, Button
# , PWMLED, Button, Buzzer, MotionSensor, LightSensor, MCP3008
# from signal import pause
from time import sleep

led_pin_outs = [21, 20, 16, 12]


def initialize_leds():
    leds = []
    for led_pin in led_pin_outs:
        leds.append(LED(led_pin))
    return leds


leds = initialize_leds()
buzzer = Buzzer(26)
light_sensor = LightSensor(13)
button = Button(2, hold_time=2)


def led_dark_condition():
    for led in leds:
        led.on()


def led_light_condition():
    leds[0].on()
    leds[1].off()
    leds[2].off()
    leds[3].on()


def start():
    buzzer.off()
    if(button.is_held):
        return True
    light_sensor.wait_for_light()
    led_light_condition()
    light_sensor.wait_for_dark()
    led_dark_condition()
    print("Press and Hold 2sec for to enter Surveillance Mode")
    return False


def ready():
    return True


def surveillance():
    return True


def alarm():
    return True


def main():
    while True:
        state_1 = start()
        print('Entering state 2')
        # if not state_1:
        #

        # led = LED(17)
        # pwm_led = PWMLED(21)
        # button = Button(2)
        # buzzer = Buzzer(26)
        # pir = MotionSensor(19)
        # lightSensor = LightSensor(13)
        # pot = MCP3008(channel=0)

        # def button_pressed():
        #     led.on()
        #     buzzer.on()

        # def button_released():
        #     led.off()
        #     buzzer.off()

        # def when_motion():
        #     print('Motion detected')

        # def when_no_motion():
        #     print('No motion available')

        # def button_motion_handling():
        #     pwm_led.source = lightSensor
        #     print('Light Sensor value', lightSensor.value)
        #     print('Pot Value', pot.value)
        #     button.when_pressed = button_pressed
        #     button.when_released = button_released
        #     pir.when_motion = when_motion
        #     pir.when_no_motion = when_no_motion
        #     pause()

        # def main_loop():
        #     current_pot_value = pot.value
        #     while True:
        #         if(current_pot_value != pot.value):
        #             print('Pot value changed', pot.value)
        #             current_pot_value = pot.value
        #             sleep(.5)

        # t1 = Thread(target=button_motion_handling)
        # threads = [t1]
        # t2 = Thread(target=main_loop)
        # threads += [t2]

        # t1.start()
        # t2.start()

        # for tloop in threads:
        #     tloop.join()

        # button_motion_handling()
