import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SecretKey01'
    SQLALCHEMY_DATABASE_URI = 'postgresql://jyaewwljfdoeuu:0f37a43f1a66521aa5b8c5ebd80ff4f1832a2ccf13806beb5e7de372526de027@ec2-34-193-113-223.compute-1.amazonaws.com:5432/d3929hch22rdn6'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    shop_id = 5
    secret_key = 'SecretKey01'
    payway = 'advcash_rub'  # (для invoice)
