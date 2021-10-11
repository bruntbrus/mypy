'''
Simple debug.
'''

from lib import log


logger = log.get_logger(__name__)


def run(args):
  logger.info(f'Arguments: {args}')


def setup_arg_parser(arg_parser):
  arg_parser.description = __doc__

  arg_parser.add_argument('X',
    nargs='*',
    help='anything'
  )
