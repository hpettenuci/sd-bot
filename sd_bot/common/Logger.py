import logging
import sys

from jsonformatter import JsonFormatter


class BotLogger:
    def __init__(self):
        self.logger = self.logging_override(__name__)

    def get_logger(self):
        return self.logger

    def logging_override(self, name: str, log_level=logging.WARNING):
        STRING_FORMAT = """{
            "datetime": "asctime",
            "levelName": "levelname",
            "module": "module",
            "lineNumber": "lineno",
            "process": "process",
            "message": "message"
        }"""

        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)
        formatter = JsonFormatter(
            STRING_FORMAT, mix_extra=True, mix_extra_position="tail"
        )

        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        sh.setLevel(log_level)

        self.logger.addHandler(sh)

        return self.logger

    def exception_handler(
        self, exception_type, exception, traceback, debug_hook=sys.excepthook
    ):
        if self.logger.level == logging.DEBUG:
            debug_hook(exception_type, exception, traceback)
        elif self.logger.level == logging.INFO:
            print(exception_type.__name__, exception)
