'''
Show file stat.
'''

import os
from stat import *
from pathlib import Path
from datetime import datetime

from lib import log


logger = log.get_logger(__name__)


def run(args):
  pathname = args.PATHNAME
  stat_result = None

  try:
    stat_result = os.stat(pathname)
  except FileNotFoundError as e:
    logger.error('File not found.')
    return

  logger.info(f'Type: {get_type(stat_result)}')
  logger.info(f'Size: {get_size(stat_result)}')
  logger.info(f'Mode: {get_file_mode(stat_result)}')
  logger.info(f'Owner: {get_owner(stat_result)}')
  logger.info(f'Group: {get_group(stat_result)}')
  logger.info(f'Accessed: {datetime.fromtimestamp(get_time_accessed(stat_result))}')
  logger.info(f'Modified: {datetime.fromtimestamp(get_time_modified(stat_result))}')


def setup_arg_parser(arg_parser):
  arg_parser.description = __doc__

  arg_parser.add_argument('PATHNAME',
    help='pathname'
  )


def get_mode(stat_result):
  return stat_result[ST_MODE]


def get_type(stat_result):
  stat_mode = get_mode(stat_result)
  mode_type = None

  if S_ISDIR(stat_mode):
    mode_type = 'Directory'
  elif S_ISREG(stat_mode):
    mode_type = 'File'
  elif S_ISLNK(stat_mode):
    mode_type = 'Symbolic link'
  elif S_ISSOCK(stat_mode):
    mode_type = 'Socket'
  elif S_ISFIFO(stat_mode):
    mode_type = 'FIFO'
  elif S_ISCHR(stat_mode):
    mode_type = 'Character device'
  elif S_ISBLK(stat_mode):
    mode_type = 'Block device'
  else:
    mode_type = 'Other'

  return mode_type


def get_size(stat_result):
  return stat_result[ST_SIZE]


def get_file_mode(stat_result):
  return filemode(get_mode(stat_result))


def get_owner(stat_result):
  return stat_result[ST_UID]


def get_group(stat_result):
  return stat_result[ST_GID]


def get_time_accessed(stat_result):
  return stat_result[ST_ATIME]


def get_time_modified(stat_result):
  return stat_result[ST_MTIME]
