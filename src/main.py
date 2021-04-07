import time
import RPi.GPIO as GPIO

######################################################################
#                                                                    #
# GPIO layout: https://www.raspberrypi.org/documentation/usage/gpio/ #
#                                                                    #
######################################################################

# GPIO.BOARD : index of the pin found in schemes (1-40).
# GPIO.BCM : numbers in the name of the pin (GPIO 1,5,17,..)
GPIO.setmode(GPIO.BOARD)

# pin 11 : GPIO 17
PIN = 11
print("Using pin #" + str(PIN))

# input or output: GPIO.IN or GPIO.OUT
# no power = 0 / GPIO.LOW / False
# power = 1 / GPIO.HIGH / True
GPIO.setup(PIN, GPIO.OUT, initial=GPIO.LOW)

while True:
    print("pin: ON")
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(8)
    print("pin: OFF")
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(2)

# cleans up the setup pins and marks them as unused
# this prevents warnings when turning it off and on again
# however, this will not be reached so far as the test code
# is forever stuck in the while-loop.
GPIO.cleanup()

print("### program has ended ###")
