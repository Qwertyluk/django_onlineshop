from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm

# Create your views here.
def registrationPage(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Account was created successfully')
            return redirect('login')

    context = {'form': form}
    return render(request, 'account/registration.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('usernameForm')
        password = request.POST.get('passwordForm')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Username OR password is incorrect')
        
    context = {}
    return render(request, 'account/login.html', context)

def logoutAction(request):
    logout(request)
    return redirect('index')