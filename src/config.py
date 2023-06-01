class Config:
    SECRET_KEY = 'wdqj---/qwpodijqodi12!!!!qopwdkp'


class DevelopmentConfig(Config):
    DEBUG=True

config={
    'development': DevelopmentConfig
}