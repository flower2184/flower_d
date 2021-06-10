from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, label="first_name")
    last_name = forms.CharField(max_length=200, label="last_name")


    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")