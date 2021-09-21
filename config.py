import os


class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://isaac:2face@localhost/pizaaapp'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://isaac:2face@localhost/pizaaapp'
    DEBUG = True

config_options ={
    'development':DevConfig,
    'production':ProdConfig

}