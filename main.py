import rpyc
import time
from log import log
from utils import init_window
from rpyc_service import RTUService, connect

if __name__ == "__main__":
    #init_window()
    connected = False
    while 1:
        if not connected:
            try:
                c = connect()
                connected = True
                log.info('Connected to server: %s', c._config)
            except Exception as err:
                print err
                log.error('Connection error: {}'.format(err))
        else:
            time.sleep(1)
            try:
                c.ping()
            except Exception as err:
                connected = False
                log.error('Connection to server droped: %s', err)
