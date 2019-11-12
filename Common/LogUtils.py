import logging
from . import GetDirectory

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def createLog(filename):
    try:
        f = GetDirectory.getDir() + "\\" + filename + '.log'
        fh = logging.FileHandler(f)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s [line:%(lineno)d] %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    except Exception as err:
        logger.debug("Error when creating log file, error message: {}".format(str(err)))


def Log(message):
    logger.debug(message)
