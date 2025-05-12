from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import LoginForm, SignForm
from django.contrib import auth
from django.contrib import messages

def main(request):
    return render(request, 'users/user.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            user = auth.authenticate(request, password=password, username=username)
            if user:
                auth.login(request, user)
                
                messages.success(request, 'Вы успешно вошли в аккаунт!')
                return redirect('index')
    else:
        form = LoginForm()
    context = {
        'form' : form
    }
    return render(request, 'users/login.html', context)

def sign(request):
    if request.method == 'POST':
        form = SignForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            
            messages.success(request, 'Вы успешно создали аккаунт!')
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = SignForm()
    context = {
        'form' : form
    }
    return render(request, 'users/sign.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])