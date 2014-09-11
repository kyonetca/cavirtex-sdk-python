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


def orderbook(pair, days=None, start=None, end=None):
  if pair not in VALID_CURRENCY_PAIRS:
    raise InvalidCurrencyPair(pair)

  payload = {
    'currencypair': pair
  }

  if days:
    payload['days'] = days
  else:
    if start:
      payload['startdate'] = start.strftime(DATE_FORMAT)
    if end:
      payload['endtime'] = end.strftime(DATE_FORMAT)

  resp = requests.get('https://cavirtex.com/api2/orderbook.json',
    params=payload)
  data = json.loads(resp.text)
  return data

def tradebook():
  pass


def ticker():
  pass
