
# CaVirtex Python SDK

This project is a thin wrapper on top of the CaVirtex API allows for easy
integration to the API in the python programming language.

## To Do

- [x] public api
- [ ] trading api
- [ ] merchant api

## Installation

**Note :** This is not yet the case. Please clone and install via `pip install
.` from within the clone, **for now**. This library should be pushed to PyPi
very soon.

```
$ pip install cavirtex-python-sdk
```

## Documentation

Assume all of the following documentation begins with :

```python
>>> import cavirtex as cvx
```

### Public

#### `cavirtex.orderbook`

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

## Authors

- Dawson Reid (dreid93@gmail.com)
