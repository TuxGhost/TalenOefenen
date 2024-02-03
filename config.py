import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('abcdefghijklmnopqrstuvwxyz')
class Config:
     #SECRET_KEY = os.environ.get('abcdefghijklmnopqrstuvwxyz')
    SECRET_KEY = 'abcdefghijklmnopqrstuvwxyz'