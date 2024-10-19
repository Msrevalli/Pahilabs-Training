## Files Overview

1.Simple_app.py: A basic Flask application that displays "Hello, World!".
2.HTML_escaping.py: Demonstrates HTML escaping in Flask routes.
3.Variable_rules.py: Shows how to use variable rules in Flask routes.
4.Unique_url.py: Illustrates creating unique URLs for different pages.
5.Url_Building.py: Showcases URL building using Flask's url_for() function.
6.HTTP_Methods.py: Demonstrates handling different HTTP methods in Flask.
7.Static_example.py: Shows how to serve static files and render HTML templates in Flask.

## Detailed Description

### 1. Simple App (1.Simple_app.py)

This script creates a minimal Flask application with a single route:

- Route "/": Returns "Hello, World!".

### 2. HTML Escaping (2.HTML_escaping.py)

This script demonstrates HTML escaping in Flask:

- Route "/": Returns "Index Page".
- Route "/hello": Returns "Hello, World".
- Route "/<name>": Returns a greeting with the name, ensuring it is escaped.

### 3. Variable Rules (3.Variable_rules.py)

This script shows how to use variable rules in Flask routes:

- Route "/": Returns "Hello".
- Route "/user/<username>": Displays a user profile.
- Route "/post/<int:post_id>": Shows a post with a given ID.
- Route "/path/<path:subpath>": Demonstrates subpath handling.

### 4. Unique URLs (4.Unique_url.py)

This script creates unique URLs for different pages:

- Route "/": Returns "Hello".
- Route "/projects/": The project page.
- Route "/about": The about page.

### 5. URL Building (5.Url_Building.py)

This script showcases URL building using Flask's url_for() function:

- Routes:
  - "/": Index page.
  - "/login": Login page.
  - "/user/<username>": User profile page.
- Features:
  - Generating URLs dynamically using url_for().
  - Passing parameters to routes.

### 6. HTTP Methods (6.HTTP_Methods.py)

This script demonstrates handling different HTTP methods in Flask:

- Routes:
  - "/login": Handles both GET and POST requests.
- Features:
  - A simple form for username and password input.
  - Basic authentication logic.

### 7. Static Files (7.Static_example.py)

This script shows how to serve static files and render HTML templates in Flask:
