from django.db import models
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextField
from django.utils import timezone

class Games(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    create_date_str = models.CharField(max_length=100)


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    games = models.ForeignKey(Games, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    create_date_str = models.CharField(max_length=100)