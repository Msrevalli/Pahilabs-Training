from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        # Retrieving form data from the POST request
        name = request.form.get('name')
        email = request.form.get('email')

        # Basic validation
        if not name or not email:
            error = "Both name and email are required!"
        else:
            return redirect(url_for('welcome', name=name))
    return render_template('register.html', error=error)

# Welcome route (redirect after registration)
@app.route('/welcome')
def welcome():
    name = request.args.get('name', 'Guest')
    return f"Welcome, {name}!"

# Search route
@app.route('/search')
def search():
    search_query = request.args.get('q', '')
    if search_query:
        return f"You searched for: {search_query}"
    else:
        return "No search query provided!"

if __name__ == '__main__':
    app.run(debug=True)
