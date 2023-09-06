from django.shortcuts import render
from .models import Post

def render_post(request):
    blog = Post.objects.all()
    return render(request, 'posts.html', {'post': blog})