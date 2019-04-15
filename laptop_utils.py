import time
from log import log
from threading import Lock

lock = Lock()
device_sn = "test_localhost"
REMOTE_SERVER = "localhost"
REMOTE_SERVER = "watering.dev.qadre.io"

WATER_PUMP_PIN = 4

WATERING_TIME = 30

SSL_PATH = "/home/mihaido/Projects/rpiservice/ssl"

def init_window():
    log.info("Laptop/PC, not RPi")


def is_busy():
    return lock.locked()


def open_window(conn):
    """
    Opens the window.
    @return: True or False
    """
    lock.acquire()
    log.info("Start watering")
    time.sleep(WATERING_TIME)
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
    conn.root.action_finished(device_sn, "close")
    lock.release()
