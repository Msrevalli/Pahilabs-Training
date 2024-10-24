from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy (without linking to the app yet)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # MySQL database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sreevalli:gmosvrt!S1@localhost/flaskSQL_blog'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db.init_app(app)

    # Register your routes blueprint
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
