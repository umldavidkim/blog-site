from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # argument allows for date_posted to be editable
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if user is deleted, post is deleted as well

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # reverse returns full path as a string. different from redirect
        return reverse('post-detail', kwargs={'pk': self.pk})
