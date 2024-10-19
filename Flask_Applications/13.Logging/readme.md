# Flask Logging Application

A simple Flask application that demonstrates how to handle HTTP requests and log application activity to a file. This project includes endpoints for processing data and provides detailed logging for debugging and monitoring.

## Features

- Basic Flask application setup with logging.
- Two endpoints:
  - `/`: A simple welcome page.
  - `/process-data`: Processes incoming data and returns a processed result.
- Logging of requests and application activity to a file.

## Access the application:

Open your web browser and go to http://127.0.0.1:5000/ to see the welcome message.

## Test the /process-data endpoint:

Use a tool like curl, Postman, or the requests library in Python to send a POST request to the /process-data endpoint.

## Overview of Logging in Flask

Preconfigured Logger: Flask comes with a built-in logger that you can use directly through app.logger. This logger is a standard Python logging.Logger instance, allowing you to log messages at different severity levels.

## Logging Levels:

DEBUG: Detailed information, typically of interest only when diagnosing problems.
INFO: Confirmation that things are working as expected.
WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., ‘disk space low’).
ERROR: A more serious problem that prevented the application from performing a function.
CRITICAL: A very serious error that might prevent the program from continuing to run.
