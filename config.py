# config.py

class Config(object):
    """
    common config settings
    """
    DEBUG = True

class DevelopmentConfig(object):
    """
    Dev config
    """
    SQLALCHEMY_ECHO = True

class ProductionConfig(object):
    """
    Production Config
    """
    DEBUG = False

class TestingConfig(object):
    """
    Testing configurations
    """
    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'production' : ProductionConfig,
    'testing': TestingConfig
}

