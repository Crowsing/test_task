import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SecretKey01'
    SQLALCHEMY_DATABASE_URI = 'postgres://mtclcpnvioxrdr:4eea05e39b462a4e20a42519db3f4bf45d6465b792b26ab9798e7699516ebaea@ec2-3-226-134-153.compute-1.amazonaws.com:5432/d8vfeai5knmsbn'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    shop_id = 5
    secret_key = 'SecretKey01'
    payway = 'advcash_rub'  # (для invoice)
