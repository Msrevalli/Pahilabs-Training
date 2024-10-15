from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))  # Output: /
    print(url_for('login'))  # Output: /login
    print(url_for('login', next='/'))  # Output: /login?next=/
    print(url_for('profile', username='JohnDoe'))  # Output: /user/John%20Doe

if __name__ == "__main__":
    app.run(debug=True)
