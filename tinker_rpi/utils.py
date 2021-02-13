from tinker_rpi.constants import DEFAULT_BTN_HOLD_TIME
from time import sleep

Y_INTERCEPT = 2
ROUNDOFF_DECIMAL_PLACES = 1
SLOPE_FOR_POTENTIOMETER = -1.8


def linear_eq(m, x, c):
    return m * x + c


def map_pot_value_to_seconds(pot_value):
    if not pot_value:
        return DEFAULT_BTN_HOLD_TIME
    time = round(linear_eq(SLOPE_FOR_POTENTIOMETER, pot_value,
                           Y_INTERCEPT), ROUNDOFF_DECIMAL_PLACES)
    return time


def turn_buzzer(buzzer):
    buzzer.on()
    sleep(0.2)
    buzzer.off()
    sleep(0.2)
