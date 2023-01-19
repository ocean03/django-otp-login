from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from authentication.views import SignUpView, send_otp, verify_otp, update_profile

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login', TemplateView.as_view(template_name='login.html'), name='login'),

    path('send_otp/<str:mobile>', send_otp, name='send_otp'),
    path('verify_otp', verify_otp, name='verify_otp'),

    path('profile', update_profile, name='update_profile'),

    path('logout/', LogoutView.as_view(next_page='home'), name='logout')

]