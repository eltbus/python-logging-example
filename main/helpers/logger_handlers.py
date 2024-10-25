import logging

from .logger_filters import LogContextInjectiveFilter


class CustomHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__()
        self.addFilter(LogContextInjectiveFilter())
