# Flask Request Context

In Flask, the request context is an important concept that allows you to access information about the current request being processed. It contains various details about the incoming request, such as form data, query parameters, headers, and more. Understanding the request context is crucial for handling incoming requests effectively in your Flask applications.

## What is Request Context?

The request context is an instance of the `Request` class that Flask creates for each incoming request. It includes data related to the request and is only available during the handling of that request. The context is managed automatically by Flask, meaning you usually don’t have to create or destroy it manually.


# Flask Greeting Application

This is a simple Flask web application that greets users based on the name they enter in a form. It demonstrates basic form handling and routing in Flask, along with unit testing.

## Features

- A home page with a form to enter your name.
- A greeting displayed upon form submission.
- Supports both GET and POST requests.
- Includes unit tests to validate the functionality.

# For running Unit tests
# python -m unittest test_app.py