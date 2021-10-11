'''
Regular Expression matching.
'''

import re

from lib import log


logger = log.get_logger(__name__)


def run(args):
  pattern = None

  try:
    pattern = re.compile(args.EXP)
  except re.error as e:
    logger.error(e.msg)
    return

  for mo in pattern.finditer(args.TEXT):
    logger.info(f'Match: {mo.group()}')


def setup_arg_parser(arg_parser):
  arg_parser.description = __doc__

  arg_parser.add_argument('EXP',
    help='regular expression'
  )

  arg_parser.add_argument('TEXT',
    help='text to match'
  )
