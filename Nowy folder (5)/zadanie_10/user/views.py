from django.shortcuts import render, redirect
from .forms import RegistrateForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='strona:main')
    if request.method=='POST':
        form= RegistrateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='strona:main')
        else:
            return render(request, 'user/signup.html', context={'form':form})
    return render(request, 'user/signup.html', context={'form':RegistrateForm()})

def loginuser(request):
    if request.user.is_authenticated:
        return redirect( to='strona:main')
    if request.method=='POST':
        user=authenticate( username= request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect("user:login")
        login(request.user)
        return redirect(to='strona:main')
    return render(request,'user/login.html', context={'form':LoginForm()})
@login_required
def logautuser(request):
    logout(request)
    return redirect(to='strona:main')