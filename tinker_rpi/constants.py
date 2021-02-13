READY = 'READY'
SURVEILLANCE = 'SURVEILLANCE'
ALARM = 'ALARM'

states = {
    READY: 1,
    SURVEILLANCE: 2,
    ALARM: 3
}

MOTION_DETECT_COUNT = 2
MOTION_DETECT_PERIOD = 15 #seconds

LED_PIN_OUTS = [21, 20, 16, 12]
MOTION_SENSOR_PIN = 19
LIGHT_SENSOR_PIN = 13
BUZZER_PIN = 26
DEFAULT_BTN_HOLD_TIME = 2  # Seconds
BUTTON_PIN = 2
