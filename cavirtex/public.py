__author__ = '''
Dawson Reid (dreid93@gmail.com)
'''

from exception import *

import requests
import json
import logging
log = logging.getLogger(__name__)


VALID_CURRENCY_PAIRS = ['BTCCAD', 'LTCCAD', 'BTCLTC']
DATE_FORMAT = '%Y-%m-%d'


def _api(endpoint, pair, days, start, end):
  '''
  '''
  if pair not in VALID_CURRENCY_PAIRS:
    raise InvalidCurrencyPair(pair)

  payload = {}

  if pair:
    payload['currencypair'] = pair

  if days:
    payload['days'] = days
  else:
    if start:
      payload['startdate'] = start.strftime(DATE_FORMAT)
    if end:
      payload['endtime'] = end.strftime(DATE_FORMAT)

  api_url = 'https://cavirtex.com/api2/{0}.json'.format(endpoint)
  resp = requests.get(api_url, params=payload)
  return json.loads(resp.text)


def orderbook(pair, days=None, start=None, end=None):
  '''
  '''
  return _api('orderbook', pair, days, start, end)


def tradebook(pair, days=None, start=None, end=None):
  '''
  '''
  return _api('trades', pair, days, start, end)


def ticker(pair=None):
  '''
  '''
  return _api('ticker', pair, None, None, None)
