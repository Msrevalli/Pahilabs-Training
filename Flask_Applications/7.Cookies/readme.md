# Flask Cookie and Session Example

This is a simple Flask web application that demonstrates how to use cookies and sessions for user authentication and preferences.

## Features

### Home Page (`/`)
- Displays a welcome message.
- If the user is logged in, it greets them with their username and provides a logout link.
- If the user is not logged in, it prompts them to log in.
- If a "Remember Me" cookie exists, it retrieves the username from the cookie.

### Login Page (`/login`)
- Users can enter their username.
- A checkbox for "Remember Me" allows users to opt to store their username in a cookie.
- Upon submission, the username is stored in the session, and if "Remember Me" is checked, a cookie is set.

### Logout
- Clicking the logout link removes the username from the session and deletes the "Remember Me" cookie.

