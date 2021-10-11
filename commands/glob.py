'''
Glob path names.
'''

import glob

from lib import log


logger = log.get_logger(__name__)


def run(args):
  pattern = args.PATTERN

  for pathname in glob.iglob(pattern, recursive=True):
    logger.info(f'Path: {pathname}')


def setup_arg_parser(arg_parser):
  arg_parser.description = __doc__

  arg_parser.add_argument('PATTERN',
    help='glob pattern'
  )
