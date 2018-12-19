import rpyc
import _thread
from log import log
import platform
if platform.machine() != "x86_64":
    from pi_utils import init_window, open_window, close_window, device_sn, is_busy
else:
    from laptop_utils import init_window, open_window, close_window, device_sn, is_busy


connection = None

REMOTE_SERVER = "watering.dev.qadre.io"


class RTUService(rpyc.Service):

    status = False

    def on_connect(self, conn):
        init_window()

    def exposed_get_status(self):
        return "open" if self.status else "closed"

    def exposed_open_window(self):
        log.warning("open_window from server")
        try:
            t = _thread.start_new_thread(open_window, (connection,))
        except Exception as err:
            log.error("thread did not started: %s", err)

        return True
        
    def exposed_close_window(self):
        log.warning("close window from server")
        try:
            t = _thread.start_new_thread(close_window, (connection,))
        except Exception as err:
            log.error("thread did not started: %s", err)
        return True
    
    def exposed_get_uuid(self):
        return device_sn
    
    def exposed_is_busy(self):
        return is_busy()


def connect():
    global connection
    connection = rpyc.connect(REMOTE_SERVER, 8010, service=RTUService)
    return connection
