from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=[('teacher', 'Teacher'), ('student', 'Student')], required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "role")

class LoginForm(AuthenticationForm):
    pass
