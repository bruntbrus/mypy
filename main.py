'''
My very own command runner!
'''

import sys
import argparse
import importlib

from lib import log


logger = log.get_logger(__name__)


def main(argv):
  del argv[0]

  cmd_name = get_command_name(argv)
  arg_parser = make_arg_parser()
  cmd_arg_parsers = add_command_arg_parsers(arg_parser)

  if not cmd_name:
    if not argv:
      arg_parser.print_usage()
    else:
      arg_parser.parse_args(argv)

    return

  cmd_mod = import_command_module(cmd_name)

  cmd_arg_parser = cmd_arg_parsers.add_parser(cmd_name,
    prog=f'mypy {cmd_name}'
  )

  if hasattr(cmd_mod, 'setup_arg_parser'):
    cmd_mod.setup_arg_parser(cmd_arg_parser)

  args = arg_parser.parse_args(argv)
  cmd_mod.run(args)


def get_command_name(argv):
  return next((arg for arg in argv if arg[0].isalpha()), None)


def make_arg_parser():
  arg_parser = argparse.ArgumentParser(
    prog='mypy',
    description=__doc__
  )

  arg_parser.add_argument('-l', '--log-level',
    dest='LOG_LEVEL',
    default='info',
    help='log level'
  )

  return arg_parser


def add_command_arg_parsers(arg_parser):
  return arg_parser.add_subparsers(help='command name')


def import_command_module(name):
  return importlib.import_module(f'commands.{name}')


if __name__ == '__main__':
  main(sys.argv)
