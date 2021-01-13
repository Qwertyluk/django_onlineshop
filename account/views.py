from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CreateUserForm, EditUserForm, ChangePasswordForm

# Create your views here.
def registrationPage(request):
    """
    Display a registration page and handle user registration.

    **Context**

    ``form``
        An instance of registration form.

    **Template:**

    :template:`account/registration.html`
    """
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
    """
    Display a login page and handle user login.

    **Template:**

    :template:`account/login.html`
    """
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

@login_required(login_url='login')
def logoutAction(request):
    """
    Logout a user.

    **Template:**
    
    Redirects to the index endpoint.
    """
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def manage(request):
    """
    Displays a user personal iformation management page and handles for managing a user personal information.

    **Context**

    ``editProfileForm``
        An instance of a form to manage user personal information.

    ``editPasswordForm``
        An instance of a form to change a user password.

    **Template:**

    :template:`account/manage.html`
    """
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

@login_required(login_url='login')
def changePassword(request):
    """
    Change user password.

    **Template:**

    If success - redirects to the manage endpoint.
    If not success - renders the :template:`account/manage.html`
    """
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
