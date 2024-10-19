class ProductionConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'prod-secret-key'  # Ensure this is set through environment variables in real apps
    ENV_NAME = 'Production'
    DATABASE_URI = 'sqlite:///prod.db'
    SESSION_COOKIE_SECURE = True  # Only send cookies over HTTPS in production
