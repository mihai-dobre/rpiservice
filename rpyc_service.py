import os
import ssl
import rpyc
from rpyc.utils.factory import ssl_connect
from threading import Thread
from log import log
import platform
if platform.machine() != "x86_64":
    from pi_utils import init_window, open_window, close_window, device_sn, is_busy, REMOTE_SERVER
else:
    from laptop_utils import init_window, open_window, close_window, device_sn, is_busy, REMOTE_SERVER


connection = None


class RTUService(rpyc.Service):

    status = False

    def on_connect(self, conn):
        init_window()

    def exposed_get_status(self):
        return "open" if self.status else "closed"

    def exposed_open_window(self):
        log.warning("open_window from server")
        try:
            t = Thread(name='Watering', target=open_window, args=(connection,))
            t.start()
        except Exception as err:
            t.join()
            log.error("thread did not started: %s", err)

        return True
        
    def exposed_close_window(self):
        log.warning("close window from server")
        try:
            t = Thread(name='StopWatering', target=close_window, args=(connection,))
            t.start()
        except Exception as err:
            log.error("thread did not started: %s", err)
        return True
    
    def exposed_get_uuid(self):
        return device_sn

    def exposed_is_busy(self):
        return is_busy()


def connect():
    global connection
    project_path = '/home/mihaido/Projects/rpiservice/ssl'
    # connection = rpyc.connect(REMOTE_SERVER, 18821, RTUService)
    connection = ssl_connect(
        REMOTE_SERVER,
        port=18821,
        service=RTUService,
        keyfile=os.path.join(project_path, 'keys', 'rpi_q_office.key.pem'),
        certfile=os.path.join(project_path, 'certs', 'rpi_q_office.cert.pem'),
        ssl_version=ssl.PROTOCOL_SSLv23,
    )
    return connection
