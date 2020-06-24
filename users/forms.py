from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# the UserCreationForm contains only the username, password and password confirmation
# creating the UserRegistrationForm and inheriting from UserCreationForm,
# we are able to add more fields to the form during registration
class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()
    # first_name = forms.CharField()
    # last_name = forms.CharField()

    class Meta:
        model = User # performing a form.save() will save to the User model
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']  # fields that will be shown on form in same order


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
