from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
posts = [
    {
        'author': 'Ali Abdulameer',
        'title': 'Blog Post 1',
        'content': 'First Post Content.',
        'date_posted': '2024-03-24',
    },
    {
        'author': 'Abdulameer Farhan',
        'title': 'Blog Post 2',
        'content': 'Second Post Content.',
        'date_posted': '2024-03-26',

    },
    
]

def home(request):
    context = {
        'posts': posts,
        'title': 'Home',
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
