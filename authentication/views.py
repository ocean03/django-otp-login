import json

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.timezone import now

from django.views.generic import CreateView

from authentication.forms import SignUpForm, UserUpdateForm
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
            if user_obj and not user_obj.is_blocked():
                from django.utils.crypto import get_random_string
                otp_number = get_random_string(length=6, allowed_chars='0123456789')
                user_obj.otp = otp_number
                user_obj.last_update_date_time = now()
                user_obj.save()
                send_sms(otp=otp_number)
                response_data = {"message": f"OTP sent to {user_obj.mobile}", "otp": otp_number}
            else:
                response_data = {
                    "message": 'Not a registered mobile number or You are temporarily blocked. please try after 5 min.'
                }
        else:
            response_data = {"message": 'Not a valid mobile number.'}
    else:
        response_data = {"message": 'mobile number is required.'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def verify_otp(request):
    data = {}
    mobile = request.POST['phone']
    is_user = User.objects.filter(mobile=mobile).first()
    password = request.POST['otp']
    print(is_user)
    if is_user and not is_user.login_attempts >= 3:
        user = authenticate(username=is_user.username, password=password)
        if user:
            login(request, user)
            is_user.login_attempts = 0
            is_user.save()
            return redirect('home')
        else:
            is_user.login_attempts += 1
            is_user.save()
            data['error'] = "invalid otp."
    else:
        data['error'] = "OTP expired or You are temporarily blocked. please try after 5 min"
    return render(request, "login.html", {'data': data})


def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserUpdateForm(instance=request.user)

    context={'form': form}
    return render(request, 'profile.html',context )