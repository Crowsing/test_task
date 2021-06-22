import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SecretKey01'
    SQLALCHEMY_DATABASE_URI = 'postgresql://uuoopvieyzkfsk:57dc5abdaffb2efd770abb0dd83ed2403e60f621b4336ed467db194a87bb86a1@ec2-54-157-100-65.compute-1.amazonaws.com:5432/d4ldu45rueerni'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    shop_id = 5
    secret_key = 'SecretKey01'
    payway = 'advcash_rub'  # (для invoice)
