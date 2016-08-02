import os
import sys
import time
import platform
if '{} {}'.format(platform.system(), platform.release()) != 'Linux 3.16.0-4-amd64':
    import RPi.GPIO as GPIO
from log import log

WINDOW_OPEN_PIN = 5
WINDOW_CLOSE_PIN = 6
WINDOW_STATUS_PIN = 26
# Close = False
# Open = True
status = False
WINDOW_STATUS = {False: 'Close', True: 'Open'}

def init_window():
    log.info('Initializing the raspberry pi pins')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(WINDOW_OPEN_PIN, GPIO.OUT)
    GPIO.setup(WINDOW_CLOSE_PIN, GPIO.OUT)
    GPIO.output(WINDOW_OPEN_PIN, GPIO.LOW)
    GPIO.output(WINDOW_CLOSE_PIN, GPIO.LOW)
    #GPIO.setup(WINDOW_STATUS_PIN, GPIO.IN)

# taking input value from Pin 11
#input_value = GPIO.input(11)
#GPIO.output(13, GPIO.LOW)

def is_open():
    """
    Check if the window is open or closed.
    @return: True or False
    """
    return WINDOW_STATUS[status]

def open_window():
    """
    Opens the window.
    @return: True or False 
    """
    global status
    GPIO.output(WINDOW_CLOSE_PIN, GPIO.LOW)
    GPIO.output(WINDOW_OPEN_PIN, GPIO.HIGH)
    time.sleep(1)
    status = True
    GPIO.output(WINDOW_OPEN_PIN, GPIO.LOW)
    return True

def close_window():
    """
    Closes the window.
    @return: True or False
    """
    global status
    GPIO.output(WINDOW_OPEN_PIN, GPIO.LOW)
    GPIO.output(WINDOW_CLOSE_PIN, GPIO.HIGH)
    time.sleep(1)
    status = False
    GPIO.output(WINDOW_CLOSE_PIN, GPIO.LOW)
    return True
