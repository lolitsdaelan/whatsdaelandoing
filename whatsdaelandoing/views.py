# -*- coding: utf-8 -*-
from django.shortcuts import render
from whatsdaelandoing.apps.blog.models import Post
 
def home(request):
	posts = Post.objects.all()
	return render(request, 'whatsdaelandoing/index.html', {})

def home_files(request, filename):
	return render(request, filename, {}, content_type='text/plan')
	