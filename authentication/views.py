import json
from datetime import timedelta

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.timezone import now

from django.views.generic import CreateView

from authentication.forms import SignUpForm
from authentication.helpers import send_sms
from authentication.models import User


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def send_otp(request, mobile):
    mobile = mobile
    if mobile is not None:
        if len(mobile) == 10 and mobile.isdigit():
            user_obj = User.objects.filter(mobile=mobile).first()
            if user_obj:
                from django.utils.crypto import get_random_string
                otp_number = get_random_string(length=6, allowed_chars='0123456789')
                user_obj.otp = otp_number
                user_obj.last_update_date_time = now()
                user_obj.save()
                send_sms(otp=otp_number)
                response_data = {"message": f"OTP sent to {user_obj.mobile}", "otp": otp_number}
            else:
                response_data = {"message": 'Not a registered mobile number.'}
        else:
            response_data = {"message": 'Not a valid mobile number.'}
    else:
        response_data = {"message": 'mobile number is required.'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def verify_otp(request):
    data = {}
    time_threshold = now() - timedelta(minutes=5)
    mobile = request.POST['phone']
    is_user = User.objects.filter(mobile=mobile).first()
    password = request.POST['otp']
    print(is_user)
    if is_user:
        user = authenticate(username=is_user.username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            data['error'] = "somthing went wong please try again."
    else:
        data['error'] = "OTP expired."
    return render(request, "login.html", {'data': data})