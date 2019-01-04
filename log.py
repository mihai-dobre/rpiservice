import logging


def setup_log():
    log = logging.getLogger("RTULog")
    hdlr = logging.FileHandler("RTULog.log", "a")
    hdlr.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s", datefmt="%y-%m-%d %H:%M:%S")
    hdlr.setFormatter(formatter)
    log.addHandler(hdlr)
    log.setLevel(logging.INFO)
    return log


print("here")
log = setup_log()
