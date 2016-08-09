import rpyc
from log import log
from utils import is_open, close_window, open_window

device_sn = '12345678abcdefgh'

class RTUService(rpyc.Service):
    def exposed_get_status(self): 
        return is_open()

    def exposed_open_window(self):
        return open_window()
        
    def exposed_close_window(self):  
        return close_window()
    
    def exposed_get_uuid(self):
        return device_sn
    
def connect():
    return rpyc.connect( 'localhost', 8010, service=RTUService)
