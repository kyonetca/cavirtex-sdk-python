__author__='''
Dawson Reid (dreid93@gmail.com)
'''


def test_import():
  from cavirtex import tradebook, orderbook, ticker


def test_orderbook_BTCCAD():
  from cavirtex import orderbook
  data = orderbook('BTCCAD')

  assert 'status' in data
  assert data['status'] == 'ok'
  assert 'apirate' in data
  assert 'message' in data
  assert data['message'] == ''
  assert 'orderbook' in data
