class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_ARTICLES_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True