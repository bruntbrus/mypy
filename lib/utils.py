# Various utilities.


def join_str(list, sep=', '):
  return sep.join(list)


def to_percent(num, dec_len=2):
  return round(num * 100, dec_len)
