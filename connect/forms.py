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
    gender_choice = forms.ChoiceField(choices=GENDER_CHOICES, required=False)
    occupation = forms.ChoiceField(choices=OCCUPATION_CHOICES, required=False)
    major = forms.MultipleChoiceField(choices=PROGRAM_CHOICES, required=False)


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
    ('dance_disco_funk', 'Dance, Disco, Funk'),
    ('folk', 'Folk'),
    ('classical', 'Classical'),
    ('jazz', 'Jazz, Swing'),
    ('rock', 'Rock'),
    ('hip_hop', 'Hip Hop, Rap'),
    ('pop', 'Pop'),
    ('country', 'Country'),
    ('edm', 'EDM'),
    ('musicals', 'Musicals'),
    ('hard_rock', 'Metal, Hard Rock'),
    ('reggae', 'Reggae'),
    ('latin', 'Latin'),
    ('techno', 'Techno, Trance'),
    ('opera', 'Opera'),
    ('rock_roll', 'Rock n Roll'),
    ('alt_music', 'Alternative Music')
)

MOVIE_CHOICES = (
    ('horror', 'Horror'),
    ('adventure', 'Adventure'),
    ('action', 'Action'),
    ('documentary', 'Documentary'),
    ('romance', 'Romantic'),
    ('comedy', 'Comedy'),
    ('thriller', 'Thriller'),
    ('sci-fi', 'Sci-fi'),
    ('war', 'Wars'),
    ('tales', 'Tales'),
    ('tales', 'Tales'),
    ('cartoons', 'Cartoons'),
    ('western', 'Western'),
    ('cartoons', 'Cartoons'),
    ('not_a_fan', 'Not a fan of movies :('),
)

# TODO: Edit this and keep it to subject interest only, probably less physical activity and hobby type questions
SUBJECT_INTEREST_CHOICES = (
    ("History","History"),
    ("Psychology","Psychology"),
    ("Politics","Politics"),
    ("Mathematics","Mathematics"),
    ("Physics","Physics"),
    ("Software_Computers","Software, Computers"),
    ("Economy, Management","Economy Management"),
    ("Biology","Biology"),
    ("Chemistry","Chemistry"),
    ("Poetry_reading","Reading"),
    ("Geography","Geography"),
    ("Foreign_languages","Foreign languages"),
    ("Medicine","Medicine"),
    ("Law","Law"),
    ("Cars","Cars"),
    ("Art","Art exhibitions"),
    ("Religion","Religion"),
    ("Outdoor_activities","Countryside, outdoors"),
    ("Dancing","Dancing"),
    ("Playing musical instruments","Musical instruments"),
    ("Poetry writing","Writing"),
    ("Sport_leisure activities","Sports"),
    ("Gardening","Gardening"),
    ("Celebrity","Celebrities, Celebrity Lifestyle, Gossip"),
    ("Shopping","Shopping"),
    ("Science_technology","Science and technology"),
    ("Theatre","Theatre"),
    ("Socializing","Fun with friends"),
    ("Adrenaline_sports","Adrenaline sports"),
    ("Pets","Pets"),
)

# TODO: Edit this, get feedback on this list!
HOBBY_CHOICES = (
    ('3d_printing', '3D Printing'),
    ('acting', 'Acting'),
    ('coffee_roasting', 'Coffee Roasting'),
    ('computer_programming', 'Computer Programming'),
    ('cooking', 'Cooking'),
    ('dance', 'Dance'),
    ('puzzles', 'Solving Puzzles, Jigsaw Puzzles'),
    ('cryptography', 'Cryptography'),
    ('fashion', 'Fashion'),
    ('gaming', 'Gaming'),
    ('ice_skating', 'Ice Skating'),
    ('knife_making', 'Knife Making'),
    ('juggling', 'Juggling'),
    ('billard', 'Billard'),
    ('knitting', 'Knitting'),
    ('machining', 'Machining'),
    ('origami', 'Origami'),
    ('painting', 'Painting'),
    ('reading', 'Reading'),
    ('yoga', 'Yoga'),
    ('debating', 'Debating'),
    ('writing', 'Writing'),
    ('jogging', 'Jogging'),
    ('basketball', 'Basketball'),
    ('tennis', 'Tennis'),
    ('baseball', 'Baseball'),
    ('fishing', 'Fishing'),
    ('hockey', 'Hockey, Ball Hockey'),
    ('swimming', 'Swimming'),
    ('soccer', 'Soccer'),
    ('rock_climbing', 'Rock Climbing'),
    ('walking', 'Walking'),
    ('biking', 'Biking'),
)


class SecondCreateProfile(forms.Form):
    sport_choice = forms.MultipleChoiceField(choices=SPORT_CHOICES, required=False)
    music_choice = forms.MultipleChoiceField(choices=MUSIC_CHOICES, required=False)
    movie_choice = forms.MultipleChoiceField(choices=MOVIE_CHOICES, required=False)
    god_question = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), required=False)
    program_question = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), required=False)
    subject_interest_question = forms.MultipleChoiceField(choices=SUBJECT_INTEREST_CHOICES, required=False)
    hobby_question = forms.MultipleChoiceField(choices=HOBBY_CHOICES, required=False)
