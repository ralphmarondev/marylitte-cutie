# The IR sensor will output HIGH (1) when no object is detected and LOW (0) when an object is detected.
#
# Wiring:
# VCC → 5V (or 3.3V, depending on your sensor)
# GND → GND
# OUT → GPIO 17 (You can change this in the code)

import time

import RPi.GPIO as GPIO

# Pin configuration
IR_SENSOR_PIN = 17  # Change this if you're using a different GPIO pin

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(IR_SENSOR_PIN) == 0:
            print("Object detected!")
        else:
            print("No object detected.")
        time.sleep(0.5)  # Delay to avoid excessive printing

except KeyboardInterrupt:
    print("\nExiting program.")
    GPIO.cleanup()  # Reset GPIO settings
