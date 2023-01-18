from django.contrib.auth.forms import UserCreationForm
from django import forms

from authentication.models import User


class SignUpForm(UserCreationForm):
    mobile = forms.CharField(max_length=12)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'mobile',
            'password1',
            'password2',
            ]

class LoginForm(forms.Form):
    mobile = forms.CharField(max_length=63)
    otp = forms.CharField(max_length=63, widget=forms.PasswordInput)