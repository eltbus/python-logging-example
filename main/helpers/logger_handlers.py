import logging


class CustomHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__()

    def emit(self, record: logging.LogRecord):
        super().emit(record=record)
