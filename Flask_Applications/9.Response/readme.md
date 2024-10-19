# Flask Response Project

A simple Flask web application that demonstrates various response types and custom error handling. The project includes routes that return string responses, JSON data, and a custom 404 error page.

## Features

- **Home Route**: Returns a simple string response.
- **Data Route**: Returns a JSON response.
- **Custom 404 Error Handling**: Displays a custom error page when a route is not found.

# Flask Response Handling Overview

This document provides an overview of how Flask handles responses in web applications. Understanding these concepts is essential for building effective Flask applications that can return various types of responses based on the needs of the application.

## Automatic Conversion

Flask automatically converts the return values of view functions into response objects based on the type of the return value.

## Response Types

### 1. String
- **Description**: If a view returns a string, Flask creates a response object with a status code of **200** and the `text/html` mimetype.
  
### 2. Dictionary or List
- **Description**: If the return value is a dictionary or list, `jsonify()` is invoked to convert it into a JSON response.

### 3. Iterator or Generator
- **Description**: If the return value is an iterator or generator yielding strings or bytes, it’s treated as a streaming response, allowing for efficient data handling.

### 4. Tuple
- **Description**: Returning a tuple can provide extra information. It can take forms such as:
  - `(response, status)`: Sets the response body and status code.
  - `(response, headers)`: Sets the response body and headers.
  - `(response, status, headers)`: Sets both the response body, status code, and headers.

### 5. WSGI Application
- **Description**: If none of the above applies, Flask assumes the return value is a valid WSGI application and converts it accordingly.

## Custom Response Modifications

If you need to modify the response object (like adding custom headers), you can use the `make_response()` function. This function allows you to wrap your return value and make changes before returning it.



