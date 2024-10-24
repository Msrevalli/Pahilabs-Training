from flask import Blueprint, render_template, redirect, url_for, request
from app.models import Post
from app import db

main = Blueprint('main', __name__)

# Home page displaying posts
@main.route('/')
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

# Route for creating a new post
@main.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        # Create a new post
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('new_post.html')

# Route for viewing a single post
@main.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)
