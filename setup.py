from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
  name = 'AsyncTelegramBot',
  packages = ['AsyncTelegramBot'],
  version = '0.2',
  description = 'Wrapper for Telegram`s Bot API utilizing asyncio',
  author = 'Jan Siebert',
  author_email = 'jansie@live.com',
  url = 'https://github.com/JanSiebert/async-telegram-bot-python',
  download_url = 'https://github.com/JanSiebert/async-telegram-bot-python/tarball/0.1',
  keywords = ['testing', 'async', 'bot', 'api', 'telegram', 'wrapper'],
  classifiers = [],
)
