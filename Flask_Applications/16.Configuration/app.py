from flask import Flask

# Initialize the app
app = Flask(__name__)

# Load configuration based on environment
def create_app(env_name):
    if env_name == 'development':
        app.config.from_object('config.development.DevelopmentConfig')
    elif env_name == 'production':
        app.config.from_object('config.production.ProductionConfig')
    else:
        raise ValueError('Invalid environment name')
    
    # Define a simple route
    @app.route('/')
    def home():
        return f"Hello from {app.config['ENV_NAME']} environment!"

    return app
