import logging
import sys

from jsonformatter import JsonFormatter


class Logger:
    def __init__(self):
        self.logger = self.loggingOverride(__name__)

    def getLogger(self):
        return self.logger

    def loggingOverride(self, name: str, logLevel=logging.WARNING):
        STRING_FORMAT = """{
            "datetime": "asctime",
            "levelName": "levelname",
            "module": "module",
            "lineNumber": "lineno",
            "process": "process",
            "message": "message"
        }"""

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logLevel)
        formatter = JsonFormatter(
            STRING_FORMAT, mix_extra=True, mix_extra_position="tail"
        )

        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        sh.setLevel(logLevel)

        self.logger.addHandler(sh)

        return self.logger

    def exception_handler(
        self, exception_type, exception, traceback, debug_hook=sys.excepthook
    ):
        if self.logger.level == logging.DEBUG:
            debug_hook(exception_type, exception, traceback)
        elif self.logger.level == logging.INFO:
            print(exception_type.__name__, exception)
        else:
            pass
