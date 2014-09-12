__author__='''
Dawson Reid (dreid93@gmail.com)
'''

import time
import hmac
import hashlib
import json
import operator
import requests

from config import VALID_CURRENCY, VALID_CURRENCY_PAIRS
from exception import *

class User(object):
  '''
  '''

  def __init__(self, token, secret):
    self.token = token
    self.secret = secret
    self._nonce = int(time.time())


  @property
  def nonce(self):
    '''
    A check has been implemented to ensure that the nonce is always
    incrementing.
    '''
    new_nonce = int(time.time())
    if new_nonce <= self._nonce:
      self._nonce += 1
    else:
      self._nonce = new_nonce
    return self._nonce


  def _create_payload_message_component(self, payload):
    payload = payload.copy()
    if 'currencypair' in payload:
      del payload['currencypair']

    sorted_pairs = sorted(payload.iteritems(), key=lambda pair: pair[0])
    payload_message_component = ''.join([value for key, value in sorted_pairs])
    return payload_message_component


  def _create_message(self, nonce, path, payload):
    message = '{nonce}{token}{path}{payload_component}'.format(
      nonce=nonce,
      token=self.token,
      path=path,
      payload_component=self._create_payload_message_component(payload)
    )
    return message


  def _create_path(self, action):
    return '/api2/user/{0}.json'.format(action)


  def _create_signature(self, nonce, action, payload={}):
    path = self._create_path(action)
    message = self._create_message(nonce, path, payload)
    signature_hash = hmac.new(str(self.secret), str(message), hashlib.sha256)
    return signature_hash.hexdigest()


  def _create_url(self, action):
    url = 'https://cavirtex.com{path}'.format(
      path=self._create_path(action))
    return url


  def _api(self, action, payload={}):
    nonce = self.nonce

    payload['signature'] = self._create_signature(nonce, action, payload)
    payload['token'] = self.token
    payload['nonce'] = nonce

    url = self._create_url(action)
    resp = requests.post(url, data=payload)
    data = json.loads(resp.text)
    return data


  def balance(self):
    action = 'balance'
    return self._api(action)


  def transactions(self, currency, days=None, start=None, end=None):
    action = 'transactions'

    if currency not in VALID_CURRENCY:
      raise InvalidCurrency(currency)

    payload = {}
    payload['currency'] = currency

    if days:
      payload['days'] = days
    else:
      if start:
        payload['startdate'] = start.strftime(DATE_FORMAT)
      if end:
        payload['endtime'] = end.strftime(DATE_FORMAT)

    return self._api(action, payload)


  def _build_payload(self, currencypair, days, start, end):
    if currencypair and currencypair not in VALID_CURRENCY_PAIRS:
      raise InvalidCurrencyPair(currencypair)

    payload = {}
    if currencypair:
      payload['currencypair'] = currencypair

    if days:
      payload['days'] = days
    else:
      if start:
        payload['startdate'] = start.strftime(DATE_FORMAT)
      if end:
        payload['endtime'] = end.strftime(DATE_FORMAT)

    return payload


  def trades(self, currencypair=None, days=None, start=None, end=None):
    action = 'trades'
    payload = self._build_payload(currencypair, days, start, end)
    return self._api(action, payload)


  def orders(self, currencypair=None, days=None, start=None, end=None):
    action = 'orders'
    payload = self._build_payload(currencypair, days, start, end)
    return self._api(action, payload)


  def create_order(self, currencypair, mode, amount, price):
    action = 'order'

    if currencypair not in VALID_CURRENCY_PAIRS:
      raise InvalidCurrencyPair(currencypair)

    payload = {
      'currencypair': currencypair,
      'mode': mode,
      'amount': amount,
      'price': price
    }
    return self._api(action, payload)


  def cancel_order(self):
    action = 'order_cancel'


  def withdraw(self):
    action = 'withdraw'
