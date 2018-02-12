from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


app_name = 'blog'
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})