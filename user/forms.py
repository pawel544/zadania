from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistrateForm(UserCreationForm):
    username= forms.CharField(min_length=3,
                              max_length=100,
                              required=True,
                              widget=forms.TextInput())

    email= forms.CharField(min_length=5,
                           max_length=20,
                           required=True,
                           widget=forms.TextInput())

    password1 = forms.CharField(min_length=3,
                                max_length=20,
                                required=True,
                                widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=3,
                                max_length=20,
                                required=True,
                                widget=forms.PasswordInput())
    class Meta():
        model= User
        fields=['username', 'password1', 'password2']
class LoginForm(AuthenticationForm):
    class Meta():
        model=User
        fields=['username','password']
