from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Home route
@app.route('/')
def home():
    person = request.args.get('person')  # Get person from URL query params
    return render_template('home.html', person=person)

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Login route
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        session['logged_in'] = True
        return redirect(url_for('home'))
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    session['logged_in'] = False
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
