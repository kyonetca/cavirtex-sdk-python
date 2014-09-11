
# CaVirtex Python SDK

This project is a thin wrapper on top of the CaVirtex API allows for easy
integration to the API in the python programming language.

## To Do

- [ ] public api
- [ ] trading api
- [ ] merchant api

## Installation

```
$ pip install cavirtex-python-sdk
```

## Documentation

### Public

#### `cavirtex.orderbook`

#### `cavirtex.tradebook`

#### `cavirtex.ticker`

### Private

I do not currently have an API key to use in developing the private component,
though hopefully will soon.

## Usage

```python
>>> import cavirtex as cvx
>>> print(cvx.orderbook())
>>> print(cvx.tradebook())
>>> print(cvx.ticker())
```

## Authors

- Dawson Reid (dreid93@gmail.com)
