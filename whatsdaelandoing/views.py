# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from whatsdaelandoing.apps.blog.models import Post
 
def home(request):
	posts = Post.objects.all()
	return render(request, 'whatsdaelandoing/index.html', {'posts':posts})

def home_files(request, filename):
	return render(request, filename, {}, content_type='text/plan')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'whatsdaelandoing/post_detail.html', {'post': post})