from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Create profile everytime a user is created
# User is sender. Profile is receiver.
@receiver(post_save, sender=User) # when a user is saved, send this signal. signal is received by the receiver
def create_profile(sender, instance, created, **kwargs): # the receiver is create_profile function. the arguments are passed by post_save
    if created:
        Profile.objects.create(user=instance) # if user is created, create profile with user that was created

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
