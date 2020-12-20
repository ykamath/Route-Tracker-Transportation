from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Location

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        #If this forms validates then create a user with these fields
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Country Name'})}
