from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, EditUsername
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def landing_page(request):
    sign_form = SignUpForm(request.POST or None)
    login_form = LoginForm(request.POST or None)
    if request.method == 'POST' and 'sign_up' in request.POST:
        if sign_form.is_valid():
            user = sign_form.save()
            user.refresh_from_db()
            user.profile.first_name = sign_form.cleaned_data.get('first_name')
            user.profile.last_name = sign_form.cleaned_data.get('last_name')
            user.profile.email = sign_form.cleaned_data.get('email')
            user.save()
            raw_password = sign_form.cleaned_data.get('password1')
            username = user.username
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile_creation')
        else:
            sign_form = SignUpForm()

    elif request.method == 'POST' and 'login' in request.POST:
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')  # TODO: Is this safe lol?
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main_page')
    return render(request, 'landing.html', {'sign_form': sign_form, 'login_form': login_form})


@login_required(login_url=reverse_lazy('landing_page'))
def profile_creation(request):
    first_name = request.user.first_name
    return render(request, "profile_creation.html", {'name':first_name})


@login_required(login_url=reverse_lazy('landing_page'))
def creation_finish(request):
    return render(request, "creation_finish.html")


@login_required(login_url=reverse_lazy('landing_page'))
def main_page(request):
    return render(request, "main_page.html")


@login_required(login_url=reverse_lazy('landing_page'))
def edit_profile(request):
    edit_form = EditUsername(request.POST or None)
    if request.method == 'POST':
        if edit_form.is_valid():
            # TODO: Checking if the username is unique
            old_username = request.user.username
            new_username = edit_form.cleaned_data.get('username')
            if User.objects.filter(username=new_username).exists():
                messages.error(request, 'Username already exists.')
            else:
                user = User.objects.get(username=old_username)
                user.username = new_username
                user.save()
                return redirect('main_page')
    return render(request, "edit_profile.html", {'form':edit_form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('main_page')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_reset.html', {
        'form': form
    })


@login_required(login_url=reverse_lazy('landing_page'))
def feature_request(request):
    return render(request, "feature_request.html")
