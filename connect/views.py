from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import login

def landing_page(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('profile_creation')
    else:
        form = UserForm()
    return render(request, 'landing.html', {'form': form})

#
# def landing_page(request):
#     return render(request, "landing.html")

def profile_creation(request):
    return render(request, "profile_creation.html")

def creation_finish(request):
    return render(request, "creation_finish.html")

def main_page(request):
    return render(request, "main_page.html")

def main_profile(request):
    return render(request, "main_profile.html")

def feature_request(request):
    return render(request, "feature_request.html")