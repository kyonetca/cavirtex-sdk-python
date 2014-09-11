__author__ = '''
Dawson Reid (dreid93@gmail.com)
'''

# configure logging
import logging.config
logging.config.dictConfig({
  'version': 1,
  'disable_exsisting_loggers': False,
  'formatters': {
    'simple': {
      'format': '[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s'
    },
    'coloured': {
      '()': 'colorlog.ColoredFormatter',
      'format': "[%(asctime)s] {%(filename)s:%(lineno)d} %(log_color)s%(levelname)s%(reset)s - %(purple)s%(name)s%(reset)s - %(message)s",
      'log_colors' : {
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARN': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red'
      }
    }
  },
  'handlers': {
    'console': {
      'class': 'logging.StreamHandler',
      'level': 0,
      'formatter': 'coloured',
      'stream': 'ext://sys.stdout'
    }
  },
  'root': {
    'level': 0,
    'handlers': ['console']
  }
})

from .public import orderbook, tradebook, ticker
