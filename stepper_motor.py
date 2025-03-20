# Updated Wiring (Raspberry Pi to ULN2003 Driver Module)
# IN1 → GPIO 5
# IN2 → GPIO 6
# IN3 → GPIO 13
# IN4 → GPIO 19
# VCC → 5V
# GND → GND

import time

import RPi.GPIO as GPIO

# Define new GPIO pins
IN1 = 5
IN2 = 6
IN3 = 13
IN4 = 19

# Define step sequence for 28BYJ-48 stepper motor
STEP_SEQUENCE = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Function to rotate stepper motor
def rotate_stepper(steps, direction, delay=0.002):
    for _ in range(steps):
        for step in (STEP_SEQUENCE if direction == "cw" else reversed(STEP_SEQUENCE)):
            GPIO.output(IN1, step[0])
            GPIO.output(IN2, step[1])
            GPIO.output(IN3, step[2])
            GPIO.output(IN4, step[3])
            time.sleep(delay)

try:
    while True:
        print("Rotating Clockwise")
        rotate_stepper(512, "cw")  # 512 steps ≈ 1 full rotation
        time.sleep(1)

        print("Rotating Counter-Clockwise")
        rotate_stepper(512, "ccw")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting program.")
    GPIO.cleanup()
