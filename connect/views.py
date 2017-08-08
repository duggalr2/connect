from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


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
def main_profile(request):
    return render(request, "main_profile.html")


@login_required(login_url=reverse_lazy('landing_page'))
def feature_request(request):
    return render(request, "feature_request.html")
