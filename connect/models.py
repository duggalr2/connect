from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250, default='first_name')
    last_name = models.CharField(max_length=250, default='last_name')
    email = models.EmailField(default='ibrahul24@gmail.com')
    gender_choice = models.CharField(max_length=500, blank=True)
    occupation = models.CharField(max_length=500, blank=True)
    major = models.CharField(max_length=500, blank=True)
    sport_choice = models.CharField(max_length=500, blank=True)
    music_choice = models.CharField(max_length=500, blank=True)
    movie_choice = models.CharField(max_length=500, blank=True)
    god_question = models.CharField(max_length=500, blank=True)
    program_question = models.CharField(max_length=500, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
