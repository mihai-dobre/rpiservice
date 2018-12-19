import time
from log import log
from threading import Lock
import RPi.GPIO as GPIO


lock = Lock()
device_sn = "test"

WATER_PUMP_PIN = 4

WATERING_TIME = 30


def init_window():
    log.info("Initializing the raspberry pi pins")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(WATER_PUMP_PIN, GPIO.OUT)
    GPIO.output(WATER_PUMP_PIN, GPIO.LOW)


def is_busy():
    return lock.locked()


def open_window(conn):
    """
    Opens the window.
    @return: True or False
    """
    lock.acquire()
    log.info("Start watering")
    GPIO.output(WATER_PUMP_PIN, GPIO.HIGH)
    time.sleep(WATERING_TIME)
    GPIO.output(WATER_PUMP_PIN, GPIO.LOW)
    log.info("Watering ended")
    conn.root.action_finished(device_sn, "open")
    lock.release()


def close_window(conn):
    """
    Stop watering
    @return: True or False
    """
    lock.acquire()
    log.warning("Stop water pump")
    GPIO.output(WATER_PUMP_PIN, GPIO.LOW)
    conn.root.action_finished(device_sn, "close")
    lock.release()
