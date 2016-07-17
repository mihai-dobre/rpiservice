import rpyc

class RTUService(rpyc.Service):
    def exposed_get_status(self): 
        if window_status:
            return 'open'
        return 'close'

    def exposed_open_window(self):
        return actuator_open()
        
    def exposed_close_window(self):  
        return actuator_close()

if __name__ == "__main__":
    c = rpyc.connect(RTUService, "localhost", 18861)
    c.root.hello()
