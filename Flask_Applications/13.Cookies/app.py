from flask import Flask, render_template, request, redirect, url_for, session, make_response

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a random secret key

@app.route('/')
def index():
    # Accessing username from session
    username = session.get('username')
    # Accessing a cookie
    remember_me = request.cookies.get('remember_me')

    # Check if the user has a preference saved in cookies
    if remember_me:
        username = remember_me  # Override session with cookie value if present

    return render_template('index.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        remember = request.form.get('remember')  # Get remember me checkbox value

        session['username'] = username  # Store username in session

        # Set a cookie if the user chooses to be remembered
        resp = make_response(redirect(url_for('index')))
        if remember:
            resp.set_cookie('remember_me', username, max_age=60*60*24*30)  # Cookie expires in 30 days
        else:
            resp.set_cookie('remember_me', '', expires=0)  # Remove cookie if not remembering

        return resp

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from the session
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('remember_me', '', expires=0)  # Remove the remember_me cookie
    return resp

if __name__ == '__main__':
    app.run(debug=True)
