from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import CreateUserForm, EditUserForm, ChangePasswordForm

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

def manage(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile was changed successfully', extra_tags='editProfile')
        else:
            messages.add_message(request, messages.ERROR, 'Could not change profile', extra_tags='editProfile')
        
        return redirect('manage')
    else:
        editProfileForm = EditUserForm(instance = request.user)
        editPasswordForm = ChangePasswordForm(user = request.user)
        context = {'editProfileForm': editProfileForm, 'editPasswordForm': editPasswordForm}
        return render(request, 'account/manage.html', context)

def changePassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.add_message(request, messages.SUCCESS, 'Password was changed successfully', extra_tags='changePassword')
        editProfileForm = EditUserForm(instance = request.user)
        context = {'editProfileForm': editProfileForm, 'editPasswordForm': form}
        return render(request, 'account/manage.html', context)
    else:
        return redirect('manage')
