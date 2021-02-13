from time import sleep
from tinker_rpi.timer import Timer
from tinker_rpi.utils import linear_eq
from tinker_rpi.led_util import LEDUtil
from gpiozero import Buzzer, LightSensor, Button, MotionSensor, MCP3008
from tinker_rpi.constants import states, LED_PIN_OUTS, MOTION_SENSOR_PIN, BUZZER_PIN, LIGHT_SENSOR_PIN, DEFAULT_BTN_HOLD_TIME, BUTTON_PIN

pir_timer = Timer()
pot = MCP3008(channel=0)
pir = MotionSensor(MOTION_SENSOR_PIN)

def map_pot_value_to_seconds(pot_value):
    if not pot_value:
        return DEFAULT_BTN_HOLD_TIME
    time = round(linear_eq(-1.8, pot_value, 2), 1)
    return time

def turn_buzzer(buzzer):
    buzzer.on()
    sleep(0.2)
    buzzer.off()
    sleep(0.2)


def main():
    motion_count = 0
    buzzer = Buzzer(BUZZER_PIN)
    ledUtil = LEDUtil(LED_PIN_OUTS)
    current_state = states["READY"]
    light_sensor = LightSensor(LIGHT_SENSOR_PIN)
    button_press_lenght = DEFAULT_BTN_HOLD_TIME
    button = Button(BUTTON_PIN, hold_time=DEFAULT_BTN_HOLD_TIME)

    def alarm():
        print("Alarm Mode")
        turn_buzzer(buzzer)
        ledUtil.led_alarm_sequence()
        if button.is_pressed:
            return states["READY"]
        return states["ALARM"]

    def surveillance():
        print('Surveillance Active')
        ledUtil.led_surveillance_sequence()
        if pir.motion_detected:
            print("Time ellapsed", pir_timer.get_ellapsed_time())
            motion_count = motion_count + 1
        if pir_timer.get_ellapsed_time() <= 15 and motion_count >= 2:
            motion_count = 0
            pir_timer.stop()
            return states["ALARM"]
        elif pir_timer.get_ellapsed_time() > 15 and motion_count < 2:
            pir_timer.restart()
            motion_count = 0
        return states["SURVEILLANCE"]

    def ready():
        buzzer.off()
        if(light_sensor.light_detected):
            print("Dial potentiometer to select interval of button")
            button_press_lenght = map_pot_value_to_seconds(pot.value)
            button.hold_time = button_press_lenght
            ledUtil.led_ready_light_sequence()
        else:
            ledUtil.led_ready_dark_sequence()
            print("Press and Hold {} sec for to enter Surveillance Mode".format(
                button_press_lenght))
            if(button.is_held):
                pir_timer.start()
                return states["SURVEILLANCE"]
        return states["READY"]

    while True:
        if(current_state == states["READY"]):
            next_state = ready()
            current_state = next_state
        if(current_state == states["SURVEILLANCE"]):
            next_state = surveillance(motion_count)
            current_state = next_state
        if(current_state == states["ALARM"]):
            next_state = alarm()
            current_state = next_state
