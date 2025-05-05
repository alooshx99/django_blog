from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home',
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


