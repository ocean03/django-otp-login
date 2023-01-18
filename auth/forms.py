from django.contrib.auth.forms import UserCreationForm
from django.forms import forms

from auth.models import User


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