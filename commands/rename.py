'''
Rename multiple files.
'''

import os
import re

from lib import log


logger = log.get_logger(__name__)


def run(args):
  src_dir_path = args.SRC_DIR_PATH
  filename_re = args.FILENAME_RE
  replace_exp = args.REPLACE_EXP
  find_pattern = None

  try:
    find_pattern = re.compile(filename_re)
  except re.error as e:
    logger.error(e.msg)
    return

  rename_count = 0

  with os.scandir(src_dir_path) as it:
    for entry in it:
      name = entry.name

      if name.startswith('.') or not entry.is_file():
        continue

      match = find_pattern.fullmatch(name)

      if not match:
        continue

      new_name = replace_exp.replace('$0', name)
      group_num = 0

      for group in match.groups():
        group_num += 1
        new_name = new_name.replace(f'${group_num}', group)

      os.rename(name, new_name)
      rename_count += 1

      logger.info(f'Renamed "{name}" to "{new_name}".')

  logger.info(f'{rename_count} file(s) renamed.')


def setup_arg_parser(arg_parser):
  arg_parser.description = __doc__

  arg_parser.add_argument('SRC_DIR_PATH',
    help='source directory path'
  )

  arg_parser.add_argument('FILENAME_RE',
    help='filename regular expression'
  )

  arg_parser.add_argument('REPLACE_EXP',
    help='replace expression'
  )
