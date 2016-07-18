import rpyc
from utils import is_open, close_window, open_window

class RTUService(rpyc.Service):
    def exposed_get_status(self): 
        if is_open():
            return True
        return False

    def exposed_open_window(self):
        return open_window()
        
    def exposed_close_window(self):  
        return close_window()


