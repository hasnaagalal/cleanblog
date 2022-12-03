from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    
    
    
    def __str__ (self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('posts:post', kwargs={'pk': self.pk})

