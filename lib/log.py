# Logging.

import logging
from colorama import Fore


INFO_LEVEL = logging.INFO
WARNING_LEVEL = logging.WARNING
ERROR_LEVEL = logging.ERROR
CRITICAL_LEVEL = logging.CRITICAL
DEBUG_LEVEL = logging.DEBUG
NOTSET_LEVEL = logging.NOTSET

DEFAULT_FORMAT = '%(name_color)s[%(name)s]%(color_reset)s %(level_color)s%(levelname)s%(color_reset)s: %(message)s'


class LoggingFilter(logging.Filter):
  def __init__(self, name='', colorful=False):
    super().__init__(name)
    self.colorful = colorful

  def filter(self, record):
    if self.colorful:
      record.name_color = Fore.LIGHTBLACK_EX
      record.level_color = get_level_color(record.levelno)
      record.color_reset = Fore.RESET
    else:
      record.name_color = ''
      record.level_color = ''
      record.color_reset = ''

    return True


def get_level_color(level):
  color = Fore.WHITE

  if level == INFO_LEVEL:
    color = Fore.LIGHTBLUE_EX
  elif level == WARNING_LEVEL:
    color = Fore.LIGHTYELLOW_EX
  elif level == ERROR_LEVEL:
    color = Fore.LIGHTRED_EX
  elif level == CRITICAL_LEVEL:
    color = Fore.LIGHTMAGENTA_EX
  elif level == DEBUG_LEVEL:
    color = Fore.LIGHTGREEN_EX

  return color


def get_logger(name=__name__, level=INFO_LEVEL, format=DEFAULT_FORMAT, colorful=True):
  logger = logging.getLogger(name)
  syslog = logging.StreamHandler()
  formatter = logging.Formatter(format)
  syslog.setFormatter(formatter)
  logger.setLevel(level)
  logger.addHandler(syslog)
  logger.addFilter(LoggingFilter(colorful=colorful))

  return logger
