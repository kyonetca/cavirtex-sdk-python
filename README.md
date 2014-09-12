
# CaVirtex Python SDK

This project is a thin wrapper on top of the CaVirtex API allows for easy
integration to the API in the python programming language.

## To Do

- [x] public api
- [x] trading api
- [ ] merchant api

I am currently unsure what the merchant API looks like, or how much use it
would be supporting it here.

## Installation

**Note :** This is not yet the case. Please clone and install via `pip install
.` from within the clone, **for now**. This library should be pushed to PyPi
very soon.

```
$ pip install cavirtex-sdk
```

## Documentation

Assume all of the following documentation begins with :

```python
>>> import cavirtex as cvx
```

### Public

#### `cavirtex.orderbook`

```python
>>> orders = cvx.orderbook()
```

The number of days back to run may also be included

```python
>>> orders = cvx.orderbook(days=10) # retrieves the previous 10 days of orders
```

or a date range may be specified using python date objects  

```python
>>> import datetime
>>> orders = cvx.orderbook(
...  start=datetime.date(year=2014, month=03, day=10)
...  end=datetime.date(year=2014, month=03, day=20))
```

#### `cavirtex.tradebook`

#### `cavirtex.ticker`

### Private

All private API requests are based around a user object. The user object is
created with the token and secret :

```python
>>> user = cvx.User(token, secret)
```

The user may then be queried for the following :

#### `cavirtex.User.balance`

**Returns :**

```javascript
{
  BTC: ...,
  CAD: ...,
  LTC: ...
}
```

#### `cavirtex.User.transactions`

#### `cavirtex.User.trades`

#### `cavirtex.User.orders`

**Note :** The following methods are not covered by tests.

#### `cavirtex.User.create_order`

#### `cavirtex.User.cancel_order`

#### `cavirtex.User.withdraw`

## Authors

- Dawson Reid (dreid93@gmail.com)
