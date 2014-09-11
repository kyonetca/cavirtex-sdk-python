
# CaVirtex Python SDK

This project is a thin wrapper on top of the CaVirtex API allows for easy
integration to the API in the python programming language.

## To Do

- [ ] public api
- [ ] private api
- [ ] merchant api
- [ ] trading api

## Installation

```
$ pip install cavirtex-python-sdk
```

## Usage

```python
import cavirtex as cvx
print(cvx.orderbook())
print(cvx.tradebook())
print(cvx.ticker())
```

## Authors

- Dawson Reid (dreid93@gmail.com)
