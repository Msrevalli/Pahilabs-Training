from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# MySQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sreevalli:gmosvrt!S1@localhost/flask_blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

# Initialize database and create tables
with app.app_context():
    db.create_all()

# Home page displaying posts
@app.route('/')
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

# Route for creating a new post
@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        # Create a new post
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('post.html')

# Route for viewing a single post
@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
