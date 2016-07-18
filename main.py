import rpyc
import time
from log import log
from rpyc_service import RTUService


if __name__ == "__main__":
    print log
    print dir(log)
    try:
        c = rpyc.connect( 'localhost', 8010, service=RTUService)
        log.error(c.root.echo('client here'))
    except Exception as err:
        print err
        log.error('Connection error: {}'.format(err))
