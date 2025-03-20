# The servo will move between 0° and 180° continuously.
#
# Wiring (for a 3-wire SG90 servo):
# VCC (Red) → 5V (Raspberry Pi)
# GND (Brown/Black) → GND (Raspberry Pi)
# PWM (Orange/Yellow) → GPIO 18 (You can change this in the code)

import time

import RPi.GPIO as GPIO

# Pin configuration
SERVO_PIN = 18  # Change to the GPIO pin connected to your servo

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Set up PWM for the servo (50Hz)
pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz frequency
pwm.start(0)  # Start with 0% duty cycle

# Function to set the servo angle
def set_angle(angle):
    duty = (angle / 18) + 2  # Convert angle to duty cycle
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)  # Wait for servo to reach position
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)  # Stop sending signal

try:
    while True:
        set_angle(0)  # Move to 0 degrees
        time.sleep(1)
        set_angle(180)  # Move to 180 degrees
        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting program.")
    pwm.stop()
    GPIO.cleanup()  # Reset GPIO settings
