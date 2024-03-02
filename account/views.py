from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .forms import CustomUserCreationForm


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Accounted created successfully!')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            userin = authenticate(request, username=username, password=password)
            login(request, userin)
            return redirect('product:home')
        else:
            messages.error(request, f'{form.errors}')
            print(form.errors)

    else:
        form = CustomUserCreationForm()
    context = {
        'form': form

    }
    return render(request, 'authorization.html', context)


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product:home')

        else:
            print(request)

    return render(request, 'sign-in.html')


def log_out(request):
    logout(request)
    return redirect('product:home')
