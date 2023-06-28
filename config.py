class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://eop:eop123@127.0.0.1:3306/eop_mysql"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #如果配置成true，falsk-spythqlalchemy会将追踪对象的修改并且发送信号
    SQLALCHEMY_ECHO = True

class DevelopmentConfig(Config):
    '''开发环境配置'''
    DEBUG = True
    ENV = 'development'

class TestingConfig(Config):
    '''测试环境配置'''
    TESTING = True


class ProductionConfig(Config):
    """生产环境配置"""
