'''
Show platform info.
'''

import platform

from lib import log, utils


logger = log.get_logger(__name__)


def run(args):
  logger.info(f'Architecture: {utils.join_str(platform.architecture())}')
  logger.info(f'Machine: {platform.machine()}')
  logger.info(f'Node: {platform.node()}')
  logger.info(f'Processor: {platform.processor()}')
  logger.info(f'Release: {platform.release()}')
  logger.info(f'System: {platform.system()}')
  logger.info(f'Version: {platform.version()}')
  logger.info(f'Python build: {utils.join_str(platform.python_build())}')
  logger.info(f'Python compiler: {platform.python_compiler()}')
  logger.info(f'Python branch: {platform.python_branch()}')
  logger.info(f'Python implementation: {platform.python_implementation()}')
  logger.info(f'Python revision: {platform.python_revision()}')
  logger.info(f'Python version: {platform.python_version()}')


def setup_arg_parser(arg_parser):
  arg_parser.description = __doc__
