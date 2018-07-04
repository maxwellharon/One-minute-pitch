import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY=os.environ.get("SECRET_KEY")



class ProdConfig(Config):
    '''
    Pruduction configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DATABASE_URL = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    # class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
