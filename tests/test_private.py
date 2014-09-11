__author__='''
Dawson Reid (dreid93@gmail.com)
'''

import json
f = open('creds.json', 'r')
creds = json.load(f)
f.close()

token = creds['token']
secret = creds['secret']


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

  assert message == '{1}{a}{/some/example/path}Hello World!'


def _test_get_user_balance():
  import cavirtex as cvx
  user = cvx.User(token, secret)
  data = user.balance()
