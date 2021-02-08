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
    if(light_sensor.light_detected):
        led_light_condition()
    else:
        led_dark_condition()
        print("Press and Hold 2sec for to enter Surveillance Mode")
        if(button.is_held):
            return 2
    return 1


def ready():
    for led in leds:
        led.on()
        sleep(0.2)
        led.off()
        sleep(0.2)
    return 2


def surveillance():
    return True


def alarm():
    return True

current_state = 1

def main():
    while True:
        current_state = 1;
        if(current_state == 1):
            next_state = start()
            current_state = next_state
        if(current_state == 2):
            next_state = surveillance()
            current_state = next_state
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
