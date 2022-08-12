from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import CreateuserForm

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateuserForm()
        if request.method == 'POST':
            form = CreateuserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
            return redirect('loginpage')
        return render(request, 'authentication/register.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR Password is incorrect')

        return render(request, 'authentication/login.html')


def signout(request):
    logout(request)
    return redirect('loginpage')

