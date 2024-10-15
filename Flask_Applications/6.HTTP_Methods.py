from flask import Flask, request, render_template_string

app = Flask(__name__)

# Sample login page template
login_form_template = '''
<form method="post">
    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="Login">
</form>
'''

def do_the_login():
    username = request.form['username']
    password = request.form['password']
    # Here you would normally check the username and password against a database
    if username == "admin" and password == "password":  # Example condition
        return f"Welcome, {username}!"
    else:
        return "Invalid username or password!"

def show_the_login_form():
    return render_template_string(login_form_template)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)
