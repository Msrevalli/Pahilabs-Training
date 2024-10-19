from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        # Accessing form data
        name = request.form.get('name', 'Guest')
        return f'Hello, {name}!'
    else:
        return 'Hello, GET request!'

if __name__ == '__main__':
    app.run(debug=True)
