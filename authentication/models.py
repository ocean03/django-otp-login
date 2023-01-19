from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class User(AbstractUser):
    mobile = models.CharField(max_length=10)
    otp = models.CharField(max_length=6, blank=True)
    last_update_date_time = models.DateTimeField(default=now, blank=True, null=True)
    login_attempts = models.IntegerField(default=0)
    alternate_email = models.EmailField(blank=True, null=True)

    class Meta:
        db_table = 'UserProfile'

    def __str__(self):
        return self.email

    def check_otp(self, password):
        if password != self.otp:
            return False
        return True
