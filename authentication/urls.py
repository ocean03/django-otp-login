from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from authentication.views import SignUpView, send_otp, verify_otp

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login', TemplateView.as_view(template_name='login.html'), name='login'),

    path('send_otp/<str:username>', send_otp),
    path('login', verify_otp),

    path('logout/', LogoutView.as_view(next_page='home'), name='logout')

]