from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from authentication.views import SignUpView, LoginView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout')
]