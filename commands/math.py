'''
Evaluate Python expression with math.
'''

import math
import cmath
import decimal
import fractions

from lib import log


MATH_NAMES = (
  'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh',
  'ceil', 'comb', 'copysign', 'cos', 'cosh',
  'degrees', 'dist',
  'e', 'erf', 'erfc', 'exp', 'expm1',
  'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum',
  'gamma', 'gcd',
  'hypot',
  'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt',
  'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2',
  'modf',
  'nan', 'nextafter',
  'perm', 'pi', 'pow', 'prod',
  'radians', 'remainder',
  'sin', 'sinh', 'sqrt',
  'tan', 'tanh', 'tau', 'trunc',
  'ulp',
)

CMATH_NAMES = (
  'acos', 'acosh', 'asin', 'asinh', 'atan', 'atanh',
  'cos', 'cosh',
  'exp',
  'infj', 'isclose', 'isfinite', 'isinf', 'isnan',
  'log', 'log10',
  'nanj',
  'phase', 'polar',
  'rect',
  'sin', 'sinh',
  'tan', 'tanh',
)

DECIMAL_NAMES = (
  'Decimal',
  'getcontext',
  'localcontext',
  'setcontext',
)

FRACTIONS_NAMES = (
  'Fraction',
)

logger = log.get_logger(__name__)


def run(args):
  exp = args.EXP
  value = None

  try:
    value = eval_ctx(exp)
  except Exception as e:
    logger.error(f'{e}')
    return

  logger.info(f'Value: {value}')


def setup_arg_parser(arg_parser):
  arg_parser.description = __doc__

  arg_parser.add_argument('EXP',
    help='math expression'
  )


def eval_ctx(exp):
  ctx = {name: getattr(math, name) for name in MATH_NAMES}

  for name in CMATH_NAMES:
    new_name = name

    if name in MATH_NAMES:
      new_name += '_c'

    ctx[new_name] = getattr(cmath, name)

  ctx.update({name: getattr(decimal, name) for name in DECIMAL_NAMES})
  ctx.update({name: getattr(fractions, name) for name in FRACTIONS_NAMES})

  return eval(exp, None, ctx)
