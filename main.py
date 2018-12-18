import time
from log import log
from utils import init_window
from rpyc_service import connect

if __name__ == "__main__":
    init_window()
    connected = False
    while 1:
        time.sleep(1)
        if not connected:
            try:
                c = connect()
                connected = True
                log.warning("Connected to server: %s", c._config["connid"])
            except Exception as err:
                print("Error: %s", err)
                log.warning("Connection error: {}".format(err))
        else:
            time.sleep(1)
            try:
                c.ping()
            except Exception as err:
                connected = False
                log.error("Connection to server dropped: %s", err)
