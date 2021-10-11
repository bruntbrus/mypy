'''
Show environment variables.
'''

import os
from fnmatch import fnmatch

from lib import log


logger = log.get_logger(__name__)


def run(args):
  pattern = args.PATTERN

  for k, v in os.environ.items():
    if not pattern or fnmatch(k, pattern):
      logger.info(f'{k}: {v}')


def setup_arg_parser(arg_parser):
  arg_parser.description = __doc__

  arg_parser.add_argument('PATTERN',
    nargs='?',
    help='filter pattern'
  )
