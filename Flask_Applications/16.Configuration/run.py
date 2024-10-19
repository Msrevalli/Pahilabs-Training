import os
from app import create_app

# Get environment from an environment variable (set default to 'development')
env = os.getenv('FLASK_ENV', 'development')

# Create the app based on the environment
app = create_app(env)

if __name__ == '__main__':
    app.run()
