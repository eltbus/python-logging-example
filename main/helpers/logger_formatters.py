import logging
import time


class CustomFormatter(logging.Formatter):
    converter = time.gmtime
