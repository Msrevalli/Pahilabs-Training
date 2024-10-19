class DevelopmentConfig:
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'dev-secret-key'
    ENV_NAME = 'Development'
    DATABASE_URI = 'sqlite:///dev.db'
