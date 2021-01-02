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

#
# states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
#           "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
#           "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
#           "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
#           "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# state_choices = [tuple([state,state]) for state in states]
class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name']
        # model = Location
        # user_state = forms.CharField(label="Choose a State",)
