from django.urls import path

from auth.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]