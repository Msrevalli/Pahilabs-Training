from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database Configuration
db_config = {
    'user': 'sreevalli',  # Your MySQL username
    'password': 'gmosvrt!S1',  # Your MySQL password
    'host': 'localhost',
    'database': 'flask_app_db'  # Database name you created
}

# Establish the connection with the database
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Route for Home
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', users=users)

# Route for adding a new user
@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
