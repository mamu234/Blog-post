import os 

class Config:
    SECRET_KEY = '<Flask WTF Secret Key>'
    QUOTE_URL = "http://quotes.stormconsultancy.co.uk/random.json"

    EMAIL = ""
    PASSWORD = ""
  
class TestConfig(Config):
    pass


class ProdConfig(Config):
    MAIL_USE_SSL = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USERNAME = ""
    MAIL_PASSWORD =""

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:4477@localhost/myblog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}