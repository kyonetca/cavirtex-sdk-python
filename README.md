
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

### Public

#### `cavirtex.orderbook`

#### `cavirtex.tradebook`

#### `cavirtex.ticker`

### Private

Currently a work in progress!

## Usage

```python
>>> import cavirtex as cvx
>>> print(cvx.orderbook())
>>> print(cvx.tradebook())
>>> print(cvx.ticker())
```

## Authors

- Dawson Reid (dreid93@gmail.com)
