import sys
import time
import RPi.GPIO as GPIO

######################################################################
#                                                                    #
# GPIO layout: https://www.raspberrypi.org/documentation/usage/gpio/ #
#                                                                    #
######################################################################

# GPIO.BOARD -- Board numbering scheme. The pin numbers follow the pin numbers on header P1.
# GPIO.BCM -- Broadcom chip-specific pin numbers. These pin numbers follow the lower-level
#             numbering system defined by the Raspberry Pi's Broadcom-chip brain.
GPIO.setmode(GPIO.BOARD)

# pin 3  : GPIO 02 (SDA)
# pin 11 : GPIO 17
PIN = 3
print("Using pin" + str(PIN))

# input or output: GPIO.IN or GPIO.OUT
GPIO.setup(PIN, GPIO.OUT)

# no power = 0 / GPIO.LOW / False
# power = 1 / GPIO.HIGH / True
GPIO.output(PIN, 1)

while True:
    GPIO.output(PIN, 1)
    time.sleep(3)
    GPIO.output(PIN, 0)
    time.sleep(3)

print("### program has ended ###")