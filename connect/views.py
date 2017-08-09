from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, EditUsername, FirstCreateProfile, SecondCreateProfile
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import ast

# TODO: Need to add error messages for all possible errors that can come up!
# TODO: 404 Pages!


def landing_page(request):
    sign_form = SignUpForm(request.POST or None)
    login_form = LoginForm(request.POST or None)

    # if request.user is not None:  # TODO: need to add a catch if user is logged in and on landing page!
    #     return redirect('main_page')

    if request.method == 'POST' and 'sign_up' in request.POST:  # TODO: Add error for signup's!
        if sign_form.is_valid():
            user = sign_form.save()
            user.refresh_from_db()
            user_email = sign_form.cleaned_data.get('email')
            if User.objects.filter(email=user_email).exists():  # TODO: Email is duplicate error shows but still creates user!
                print(user_email)
                messages.error(request, 'Email already exists...')
                return redirect('landing_page')
            else:
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
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if username and password:
                if user is not None:
                    login(request, user)
                    return redirect('main_page')
                else:
                    messages.error(request, 'Wrong username or password')
    return render(request, 'landing.html', {'sign_form': sign_form, 'login_form': login_form})


@login_required(login_url=reverse_lazy('landing_page'))
def profile_creation(request):
    first_name = request.user.first_name
    form = FirstCreateProfile(request.POST or None)  # TODO: SEE THE FIX FOR THE POST REQUEST!
    if request.method == 'POST':
        if form.is_valid():
            current_user = request.user
            current_user.profile.gender_choice = form.cleaned_data.get('gender_choice')
            # print(current_user.profile.gender_choice)
            current_user.profile.occupation = form.cleaned_data.get('occupation')
            # print(current_user.profile.occupation)
            current_user.profile.major = form.cleaned_data.get('major')
            # print(current_user.profile.major)
            current_user.save()
            return redirect('creation_finish')
        else:
            form = FirstCreateProfile()
            # return redirect('creation_finish')

    # elif request.method == 'GET':  # if the user decided to skip the form's

    return render(request, "profile_creation.html", {'name':first_name, 'form': form})


@login_required(login_url=reverse_lazy('landing_page'))
def creation_finish(request):
    form = SecondCreateProfile(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            current_user = request.user
            current_user.profile.sport_choice = form.cleaned_data.get('sport_choice')
            current_user.profile.music_choice = form.cleaned_data.get('music_choice')
            current_user.profile.movie_choice = form.cleaned_data.get('movie_choice')
            current_user.profile.god_question = form.cleaned_data.get('god_question')
            current_user.profile.program_question = form.cleaned_data.get('program_question')
            current_user.save()
            return redirect('main_page')
        else:
            form = SecondCreateProfile()
    return render(request, "creation_finish.html", {'form': form})


@login_required(login_url=reverse_lazy('landing_page'))
def main_page(request):  # TODO: If the profile questions aren't answered, bring up error messages here!
    current_user = request.user
    first_name = current_user.profile.first_name
    occupation = current_user.profile.occupation
    major = current_user.profile.major

    sport_choice = current_user.profile.sport_choice
    sport_choice = ast.literal_eval(sport_choice)
    sport_choice = [n.strip() for n in sport_choice]

    music_choice = current_user.profile.music_choice
    music_choice = ast.literal_eval(music_choice)
    music_choice = [n.strip() for n in music_choice]

    movie_choice = current_user.profile.movie_choice
    movie_choice = ast.literal_eval(movie_choice)
    movie_choice = [n.strip() for n in movie_choice]

    god_question = current_user.profile.god_question
    program_question = current_user.profile.program_question

    if len(major) == 0 or len(sport_choice) == 0 or len(music_choice) == 0:
        messages.error(request, "To get accurate recommendation's, please answer the questions!")

    return render(request, "main_page.html", {'name': first_name, 'occupation': occupation,
                                              'major':major, 'sport_choice':sport_choice,
                                              'music_choice':music_choice, 'movie_choice':movie_choice,
                                              'god_question':god_question, 'program_question':program_question})


# TODO: Need to think more about corner cases and stuff that can go wrong here!
@login_required(login_url=reverse_lazy('landing_page'))
def edit_profile(request):  # TODO: pass the existing instance?
    edit_form = EditUsername(request.POST or None)
    if request.method == 'POST':
        if edit_form.is_valid():
            old_username = request.user.username
            new_username = edit_form.cleaned_data.get('username')
            if User.objects.filter(username=new_username).exists():
                messages.error(request, 'Username already exists.')
            else:
                user = User.objects.get(username=old_username)
                user.username = new_username
                user.save()
                return redirect('main_page')
    return render(request, "edit_profile.html", {'form':edit_form, 'old_username': request.user.username})


@login_required(login_url=reverse_lazy('landing_page'))
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
