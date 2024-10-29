from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

posts = [
    {
        'author': 'Shakira Kiesha Bhea Gumpay',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 17, 2024'
    },
    {
        'author': 'Athea Lean Requina',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 20, 2024'

    },
    {
        'author': 'Levin Arthur Morata',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'October 28, 2024'
    }
]

def home(request):
    context = {
        'posts': posts 
    }
        
    #return HttpResponse('<h1> WELCOME HOME !!! </h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    #return HttpResponse('<h1> THIS IS ABOUT PAGE </h1>') 
    return render(request, 'blog/about.html')