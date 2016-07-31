import logging
def setup_log():
    log = logging.getLogger('RTULog')
    hdlr = logging.FileHandler('RTULog.log', 'a')
    hdlr.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s', datefmt='%y-%m-%d %H:%M:%S')
    hdlr.setFormatter(formatter)
    log.addHandler(hdlr)
    log.propagate=True
    return log
    
print 'here'
log = setup_log()
