## Flask Configuration Project

This project demonstrates how to handle environment-specific configurations in a Flask web application. It shows best practices for setting configurations like debug mode, secret keys, and database URIs, and how to use different settings for development and production environments.


## Features

Environment-Specific Configurations: Use different configuration settings based on the environment (development/production).
Debug Mode: Enabled in development for debugging, disabled in production for security.
Secret Key Management: Ensures secure handling of the Flask app's secret key.
Database Configurations: Support for different database URIs based on environment.
Secure Cookie Settings: Production configurations include secure session cookies.

## Running the Application

# Development Mode

export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
python run.py

## Production Mode

To run the application in production mode (debugging disabled, secure settings enabled)

export FLASK_ENV=production  # On Windows: set FLASK_ENV=production
python run.py

