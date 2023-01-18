from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


from auth.forms import SignUpForm


def home(request):
    return render(request, 'home.html')

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
