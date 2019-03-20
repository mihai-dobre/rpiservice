import time
from log import log
from rpyc_service import connect

if __name__ == "__main__":
    connected = False
    while 1:
        time.sleep(1)
        if not connected:
            try:
                c = connect()
                connected = True
                log.info("Connected to server: %s", c._config["connid"])
            except Exception as err:
                print("Error: ", err)
                log.exception("Connection error!")
        else:
            time.sleep(1)
            try:
                c.ping()
            except Exception as err:
                connected = False
                log.error("Connection to server dropped: %s", err)
