import os
import sys
import time
import rpyc
import threading
import platform
if "{} {}".format(platform.system(), platform.release()) != "Linux 3.16.0-4-amd64":
    import RPi.GPIO as GPIO
from log import log

WINDOW_OPEN_PIN = 5
WINDOW_CLOSE_PIN = 6
WINDOW_STATUS_PIN = 26
# Close = False
# Open = True
status = False
WINDOW_STATUS = {False: "Close", True: "Open"}
device_sn = "test"
connection = None
is_busy = False

REMOTE_SERVER = ""


def init_window():
    log.info("Initializing the raspberry pi pins")
    log.warning("Initializing the raspberry pi pins")
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


def open_window(conn):
    """
    Opens the window.
    @return: True or False 
    """
    global status
    log.warning("window opens")
    log.info("window started to open")
    GPIO.output(WINDOW_CLOSE_PIN, GPIO.LOW)
    GPIO.output(WINDOW_OPEN_PIN, GPIO.HIGH)
    time.sleep(7)
    status = True
    GPIO.output(WINDOW_OPEN_PIN, GPIO.LOW)
    global is_busy
    is_busy = False
    log.info("window opened")
    conn.root.action_finished(device_sn, "open")


def close_window(conn):
    """
    Closes the window.
    @return: True or False
    """
    global status
    log.warning("window started to close")
    GPIO.output(WINDOW_OPEN_PIN, GPIO.LOW)
    GPIO.output(WINDOW_CLOSE_PIN, GPIO.HIGH)
    time.sleep(7)
    status = False
    GPIO.output(WINDOW_CLOSE_PIN, GPIO.LOW)
    global is_busy
    is_busy = False
    log.info("window closed")
    conn.root.action_finished(device_sn, "close")


class RTUService(rpyc.Service):

    def exposed_get_status(self):
        return is_open()

    def exposed_open_window(self):
        log.warning("open_window from server")
        global is_busy
        is_busy = True
#         log.warning("~~ is_busy: %s", is_busy)
        try:
            threading.start_new_thread(open_window, (connection,))
        except Exception as err:
            log.error("thread did not started: %s", err)
        return True
        
    def exposed_close_window(self):
        log.warning("close window from server")
        global is_busy
        is_busy = True
#         log.warning("~~ is_busy: %s", is_busy)
        try:
            threading.start_new_thread(close_window, (connection,))
        except Exception as err:
            log.error("thread did not started: %s", err)
        return True
    
    def exposed_get_uuid(self):
        return device_sn
    
    def exposed_is_busy(self):
        return is_busy


def connect():
    global connection
    connection = rpyc.connect("gen8.doraz.ro", 8010, service=RTUService)
    return connection
