# Simple imports
import logging
import sys

# Internal imports
from helpers.utils import create_file


class Logger:
    logger_path = 'logs/app.log'
    current_language = ''

    def __init__(self, path=None):
        if path:
            self.logger_path = path
        create_file(self.logger_path)
        logging.basicConfig(
            filename=self.logger_path,
            format='[%(levelname)s]: %(asctime)s - %(message)s',
            level=logging.INFO
        )

    def warning(self, message):
        message = self._prepend_language(message)
        logging.warning(message)

    def error(self, message, exit=False):
        message = self._prepend_language(message)
        logging.error(message)
        if exit:
            sys.exit(0)

    def info(self, message):
        message = self._prepend_language(message)
        logging.info(message)

    def _prepend_language(self, message):
        if self.current_language:
            message = f"[{self.current_language}] {message}"
        return message
