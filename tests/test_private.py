__author__='''
Dawson Reid (dreid93@gmail.com)
'''

import json
f = open('creds.json', 'r')
creds = json.load(f)
f.close()

token = creds['token']
secret = creds['secret']

import cavirtex as cvx
user = cvx.User(token, secret)

def test_import_User():
  from cavirtex import User


def test_create_payload_message_component():
  import cavirtex as cvx
  user = cvx.User('a', 'b')
  payload_component = user._create_payload_message_component(
    {'a': 'Hello ', 'b': 'World!'})

  assert payload_component == 'Hello World!'


def test_create_payload_message_component_sorting():
  import cavirtex as cvx
  user = cvx.User('a', 'b')
  payload_component = user._create_payload_message_component(
    {'b': 'World!', 'a': 'Hello '})

  assert payload_component == 'Hello World!'


def test_create_message():
  import cavirtex as cvx
  user = cvx.User('a', 'b')
  message = user._create_message(
    1, '/some/example/path', {'b': 'World!', 'a': 'Hello '})

  assert message == '1a/some/example/pathHello World!'


def test_create_message_using_cavirtex_example():
  token = "asdfghjklmnbvcxz"
  secret = "qwertyuioplkjhgfdsa"
  path = '/api2/user/order.json'
  nonce = 1410477538
  payload = {
    'amount': '0.1',
    'mode': 'buy',
    'currencypair': 'BTCCAD',
    'price': '965.45'
  }

  import cavirtex as cvx
  user = cvx.User(token, secret)
  message = user._create_message(nonce, path, payload)

  assert message == '1410477538asdfghjklmnbvcxz/api2/user/order.json0.1buy965.45'


def test_create_signature():
  token = "asdfghjklmnbvcxz"
  secret = "qwertyuioplkjhgfdsa"
  action = 'order'
  nonce = 1410477538
  payload = {
    'amount': '0.1',
    'mode': 'buy',
    'currencypair': 'BTCCAD',
    'price': '965.45'
  }

  import cavirtex as cvx
  user = cvx.User(token, secret)
  signature = user._create_signature(nonce, action, payload)

  assert signature == 'aab5c9501fd2980b79b0d8e7655cd2cec49d3b650ec28fa9a33354738a928efe'


def test_get_user_balance():
  data = user.balance()

  assert 'balance' in data
  assert 'CAD' in data['balance']
  assert 'BTC' in data['balance']
  assert 'LTC' in data['balance']


def test_get_user_transactions():
  data = user.transactions('CAD')
  assert 'transactions' in data


def test_get_user_trades():
  data = user.trades()
  assert 'trades' in data


def test_get_user_orders():
  data = user.orders()
  assert 'orders' in data
