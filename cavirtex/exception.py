__author__ = '''
Dawson Reid (dreid93@gmail.com)
'''


class CaVirtexException(Exception):
  '''
  '''
  pass


class InvalidCurrencyPair(CaVirtexException):
  pass


class InvalidCurrency(CaVirtexException):
  pass


class InvalidWithdrawCurrency(CaVirtexException):
  pass
