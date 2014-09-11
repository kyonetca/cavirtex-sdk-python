__author__='''
Dawson Reid (dreid93@gmail.com)
'''

import time
import hmac
import hashlib
import json
import operator
import requests

class User(object):
  '''
  '''

  def __init__(self, token, secret):
    self.token = token
    self.secret = secret


  @property
  def nonce(self):
    return int(time.time())


  def _create_payload_message_component(self, payload):
    sorted_pairs = sorted(payload.iteritems(), key=lambda pair: pair[1])
    payload_message_component = ''.join([value for key, value in sorted_pairs])
    return payload_message_component


  def _create_message(self, nonce, path, payload):
    message = '{{{nonce}}}{{{token}}}{{{path}}}{payload_component}'.format(
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
    signature_hash = hmac.new(self.secret, message, hashlib.sha256)
    return signature_hash.hexdigest()


  def _create_url(self, action):
    url = 'https://cavirtex.com{path}'.format(
      path=self._create_path(action))


  def balance(self):
    action = 'balance'

    nonce = self.nonce
    signature = self._create_signature(nonce, action)

    url = self._create_url(action)
    resp = request.get(url, params={
      'token': self.token,
      'nonce': nonce,
      'signature': signature
    })
    data = json.loads(resp.text)
    return data


  def transactions(self):
    action = 'transactions'


  def trades(self):
    action = 'trades'


  def orders(self):
    action = 'orders'


  def create_order(self):
    action = 'order'


  def cancel_order(self):
    action = 'order_cancel'


  def withdraw(self):
    action = 'withdraw'
