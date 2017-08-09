from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2',)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    fields = ('username', 'password')


class EditUsername(forms.Form):
    username = forms.CharField(max_length=30)
    # password = forms.CharField(widget=forms.PasswordInput())
    # email = forms.EmailField()
    fields = ('username',)


GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)

OCCUPATION_CHOICES = (
    ('undergraduate', 'Undergraduate'),
    ('graduate', 'Graduate'),
    ('phd', 'PHD'),
    ('post_doc', 'PostDoc'),
    ('alumni', 'Alumni'),
)


# TODO: UPDATE THIS WITH ALL THE MAJORS FROM THE UOFT SITE!
PROGRAM_CHOICES = (
    ('computer_science', 'Computer Science'),
    ('commerce_business', 'Commerce/Business/Finance'),
    ('humanities_lifesci', 'Humanities/LifeSci/HealthSci'),
    ('math_physics_statistics', 'Math/Physics/Statistics'),
    ('engineering', 'Engineering'),
)


class FirstCreateProfile(forms.Form):
    gender_choice = forms.ChoiceField(choices=GENDER_CHOICES,)
    occupation = forms.ChoiceField(choices=OCCUPATION_CHOICES, )
    major = forms.MultipleChoiceField(choices=PROGRAM_CHOICES, )


SPORT_CHOICES = (
    ('basketball', 'Basketball'),
    ('hockey', 'Hockey'),
    ('tennis', 'Tennis'),
    ('boxing', 'Boxing'),
    ('football', 'Football'),
    ('soccer', 'Soccer'),
    ('baseball', 'Baseball'),
    ('golf', 'Golf'),
)

MUSIC_CHOICES = (
    ('jazz', 'Jazz'),
    ('rock', 'Rock'),
    ('hip_hop', 'Hip Hop'),
    ('pop', 'Pop'),
    ('country', 'Country'),
    ('heavy_metal', 'Heavy Metal'),
    ('edm', 'Electronic Dance Music'),
    ('drill_trap', 'Drill Trap Music'),
    ('k_pop', 'K-Pop'),
)

MOVIE_CHOICES = (
    ('horror', 'Horror'),
    ('adventure', 'Adventure'),
    ('action', 'Action'),
    ('documentary', 'Documentary'),
    ('romance', 'Romantic'),
    ('comedy', 'Comedy'),
)


class SecondCreateProfile(forms.Form):
    sport_choice = forms.MultipleChoiceField(choices=SPORT_CHOICES, )
    music_choice = forms.MultipleChoiceField(choices=MUSIC_CHOICES, )
    movie_choice = forms.MultipleChoiceField(choices=MOVIE_CHOICES, )
    god_question = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')))
    program_question = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')))
