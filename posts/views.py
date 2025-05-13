from django.shortcuts import render
from .models import Category, Post

def index(request):
    
    context = {
        'posts' : Post.objects.all(),
        'categoryies' : Category.objects.all()
    }
    
    return render(request, 'posts/index.html', context)

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {
        'posts' : category.posts.all()
    }
    return render(request, 'posts/category.html', context)