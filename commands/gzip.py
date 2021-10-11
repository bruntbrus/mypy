'''
Compress or decompress file with gzip.
'''

import os
import gzip

from lib import log, utils


logger = log.get_logger(__name__)


def run(args):
  action = args.ACTION
  src_filepath = args.SRC_FILEPATH

  if action == 'c':
    compress(src_filepath, src_filepath + '.gz')
  elif action == 'd':
    decompress(src_filepath, os.path.splitext(src_filepath)[0])
  else:
    logger.error('Unknown action.')


def setup_arg_parser(arg_parser):
  arg_parser.description = __doc__

  arg_parser.add_argument('ACTION',
    choices=['c', 'd'],
    help='action: compress or decompress'
  )

  arg_parser.add_argument('SRC_FILEPATH',
    help='source file path'
  )


def read_data(filepath):
  data = None

  try:
    with open(filepath, 'rb') as file:
      data = file.read()
  except FileNotFoundError:
    logger.error(f'File "{filepath}" not found.')

  return data


def write_data(dest_filepath, data):
  try:
    with open(dest_filepath, 'wb') as file:
      file.write(data)
  except FileExistsError:
    logger.error(f'File {dest_filepath} already exists.')


def compress(src_filepath, dest_filepath):
  data = read_data(src_filepath)

  if not data:
    return

  src_size = len(data)
  data = gzip.compress(data)
  dest_size = len(data)

  write_data(dest_filepath, data)

  size_ratio = utils.to_percent(1 - dest_size / src_size)
  logger.info(f'File "{dest_filepath}" is compressed by {size_ratio}%.')


def decompress(src_filepath, dest_filepath):
  data = read_data(src_filepath)

  if not data:
    return

  src_size = len(data)
  data = gzip.decompress(data)
  dest_size = len(data)

  write_data(dest_filepath, data)

  size_ratio = utils.to_percent(dest_size / src_size - 1)
  logger.info(f'File "{dest_filepath}" is decompressed by {size_ratio}%.')
