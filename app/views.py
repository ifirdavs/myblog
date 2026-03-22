from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'app/home.html',)

def blog(request):
    data = {
        'articles': Article.objects.order_by('-date'),
    }
    return render(request, 'app/blog.html', data)

def article(request, num):
    data = {
        'article': Article.objects.get(id=num)
    }
    return render(request, 'app/article.html', data)

def about(request):
    return render(request, 'app/about.html',)

def interview(request):
    data = {
        'interviews': Interview.objects.order_by('-date')
    }
    return render(request, 'app/interview.html', data)

