#Model form: It's a python way to build out our forms, add them into a template and process and save that data.
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *

class CreateUserForm(UserCreationForm): #form to create a new user in the register page.
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']