from datetime import datetime
from json import dumps
from logging import Formatter
from logging import getLogger
from logging import StreamHandler
from os import getenv
from socket import gethostname
from sys import stdout
from traceback import format_exc

import sentry_sdk

from app.common.settings import settings


def create_logger():
    logger = getLogger()
    logger.setLevel(settings.get('log_level'))

    stdout_handler = StreamHandler(stdout)
    stdout_handler.setFormatter(LoggerFormatter())

    logger.addHandler(stdout_handler)

    if 'prod' in getenv('ENV_FOR_DYNACONF'):
        sentry_sdk.init(settings.get('sentry_dsn'))


class LoggerFormatter(Formatter):

    def format(self, record):
        log = {
            'host': gethostname(),
            'level': self._get_log_level(record.levelname),
            'message': record.msg,
            'timestamp': record.created,
            'time_human': str(datetime.now()),
            '_application': 'drink-delivery-api',
            '_environment': getenv('ENV_FOR_DYNACONF'),
            '_log_type': 'application'
        }

        if 'ERROR' in record.levelname and record.exc_info:
            log['_traceback'] = format_exc()

        for attr in vars(record):
            if attr[0] == '_':
                log[attr] = getattr(record, attr)

        return dumps(log)

    def _get_log_level(self, level):
        return {
            'CRITICAL': 2,
            'DEBUG': 7,
            'ERROR': 3,
            'INFO': 6,
            'WARNING': 4,
        }.get(level, 6)
