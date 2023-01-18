from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class User(AbstractUser):
    otp = models.CharField(max_length=6, blank=True, verbose_name=_('OTP'))
    last_update_date_time = models.DateTimeField(default=now, blank=True, null=True)
    is_vendor = models.BooleanField(default=False)
    is_ebyer = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'UserProfile'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def check_otp(self, password):
        if password != self.otp:
            return False
        return True
