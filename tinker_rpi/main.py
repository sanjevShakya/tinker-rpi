from time import sleep
from tinker_rpi.timer import Timer
from tinker_rpi.led_util import LEDUtil
from gpiozero import Buzzer, LightSensor, Button, MotionSensor, MCP3008
from tinker_rpi.utils import turn_buzzer, map_pot_value_to_seconds
from tinker_rpi.constants import ALARM, READY, SURVEILLANCE, states, LED_PIN_OUTS, MOTION_SENSOR_PIN, BUZZER_PIN, LIGHT_SENSOR_PIN, DEFAULT_BTN_HOLD_TIME, BUTTON_PIN

pir_timer = Timer()
pot = MCP3008(channel=0)
pir = MotionSensor(MOTION_SENSOR_PIN)


def main():
    motion_count = 0
    buzzer = Buzzer(BUZZER_PIN)
    ledUtil = LEDUtil(LED_PIN_OUTS)
    current_state = states.get(READY)
    light_sensor = LightSensor(LIGHT_SENSOR_PIN)
    button_press_length = DEFAULT_BTN_HOLD_TIME
    button = Button(BUTTON_PIN, hold_time=DEFAULT_BTN_HOLD_TIME)

    def start():
        nonlocal current_state
        while True:
            if current_state == states.get(READY):
                next_state = ready()
                current_state = next_state
            if current_state == states.get(SURVEILLANCE):
                next_state = surveillance()
                current_state = next_state
            if current_state == states.get(ALARM):
                next_state = alarm()
                current_state = next_state

    def ready():
        nonlocal button_press_length
        buzzer.off()
        if(light_sensor.light_detected):
            print("Dial potentiometer to select interval of button")
            button_press_length = map_pot_value_to_seconds(pot.value)
            button.hold_time = button_press_length
            ledUtil.led_ready_light_sequence()
        else:
            ledUtil.led_ready_dark_sequence()
            print("Press and Hold {} sec for to enter Surveillance Mode".format(
                button_press_length))
            if(button.is_held):
                pir_timer.start()
                return states.get(SURVEILLANCE)
        return states.get(READY)

    def surveillance():
        nonlocal motion_count
        print('Surveillance Active')
        ledUtil.led_surveillance_sequence()
        if pir.motion_detected:
            print("Time ellapsed", pir_timer.get_ellapsed_time())
            motion_count = motion_count + 1
        if pir_timer.get_ellapsed_time() <= 15 and motion_count >= 2:
            motion_count = 0
            pir_timer.stop()
            return states.get(ALARM)
        elif pir_timer.get_ellapsed_time() > 15 and motion_count < 2:
            pir_timer.restart()
            motion_count = 0
        return states.get(SURVEILLANCE)

    def alarm():
        print("Alarm Mode")
        turn_buzzer(buzzer)
        ledUtil.led_alarm_sequence()
        if button.is_pressed:
            return states.get(READY)
        return states.get(ALARM)

    start()
