import rpyc
import logging
from rpyc_service import RTUService


if __name__ == "__main__":
    logger = logging.getLogger('RTULog')
    hdlr = logging.handlers.BaseRotatingHandler()
    hdlr.setLevel(logging.DEBUG)
    formater = logging.Formatter()
    logger.addHandler(hdlr)
    c = rpyc.connect(RTUService, "localhost", 18861)
    c.root.hello()