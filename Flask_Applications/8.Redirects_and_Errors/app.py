from flask import Flask, redirect, url_for, render_template, abort

app = Flask(__name__)

# Dummy user check for access control
def user_has_access():
    # Simulate user access; change this to `False` to trigger the 401 error
    return False

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/protected')
def protected():
    if not user_has_access():
        abort(401)  # Simulate unauthorized access
    return "Welcome to the protected area."

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.errorhandler(401)
def unauthorized(error):
    return render_template('unauthorized.html'), 401

if __name__ == '__main__':
    app.run(debug=True)
