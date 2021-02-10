from tinker_rpi.timer import Timer
from gpiozero import LED, Buzzer, LightSensor, Button, MotionSensor
# , PWMLED, Button, Buzzer, MotionSensor, LightSensor, MCP3008
# from signal import pause
from time import sleep


led_pin_outs = [21, 20, 16, 12]
pir = MotionSensor(19)
pir_timer = Timer()

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
            pir_timer.start()
            return 2
    return 1


def surveillance(motion_count):
    print('Surveillance Active')
    for led in leds:
        led.on()
        sleep(0.2)
        led.off()
        sleep(0.2)
    if pir.motion_detected:
        print("Time ellapsed", pir_timer.get_ellapsed_time())
        return increment(motion_count)
    return motion_count


def alarm():
    print("Alarm Mode")
    buzzer.on()
    sleep(0.2)
    buzzer.off()
    sleep(0.2)
    for led in leds:
        led.on()
    sleep(0.2)

    for led in leds:
        led.off()
    sleep(0.2)
    if button.is_pressed:
        return 1
    return 3


def increment(count):
    count = count + 1
    return count


def main():
    current_state = 1
    motion_count = 0
    while True:
        if(current_state == 1):
            next_state = start()
            current_state = next_state
        if(current_state == 2):
            motion_count = surveillance(motion_count)
            if pir_timer.get_ellapsed_time() <= 15 and motion_count >=2:
                next_state = 3
                current_state = next_state
            elif pir_timer.get_ellapsed_time() > 15 and motion_count < 2:
                pir_timer.restart()
        if(current_state == 3):
            next_state = alarm()
            current_state = next_state
