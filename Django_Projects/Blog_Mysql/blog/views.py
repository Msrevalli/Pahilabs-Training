from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        Post.objects.create(title=title, content=content, author=author)
        return redirect('index')
    return render(request, 'blog/create_post.html')

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('index')
