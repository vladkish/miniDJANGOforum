from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Category, Post, SavePost
from .forms import CreatePost
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required
def creation_post(request):
    if request.method == 'POST':
        form = CreatePost(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = CreatePost()

    context = {
        'form' : form
    }
    return render(request, 'posts/create_post.html', context)

def save_post(request, post_id):
    post = Post.objects.get(id=post_id)
    save_posts = SavePost.objects.filter(user=request.user, post=post)
    
    if save_posts.exists():
        
        messages.success(request, 'Пост уже добавлен')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        SavePost.objects.create(user=request.user, post=post)
        
        messages.success(request, 'Пост добавлен!')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
def save_post_view(request):
    context = {
        'favorite_posts' : SavePost.objects.filter(user=request.user)
    }
    return render(request, 'posts/category.html', context)