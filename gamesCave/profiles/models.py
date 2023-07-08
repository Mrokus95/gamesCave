from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    FREE_ACCOUNT = "FREE"
    PREMIUM_ACCOUNT = "PREMIUM"
    TYPE_ACCOUNT_CHOICES = [
        (FREE_ACCOUNT, "Free account"),
        (PREMIUM_ACCOUNT, "Premium account"),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick = models.CharField(max_length=20, blank=False, unique=True)
    photo = models.ImageField(upload_to='users/avatars/', default='users/avatars/anonymous.png', blank=True)
    phone_number = models.CharField(max_length=9, blank=True, null=True)
    bank_account = models.CharField(max_length=26, blank=True, null=True)
    account_type = models.CharField(max_length=7, choices=TYPE_ACCOUNT_CHOICES, default=FREE_ACCOUNT)

    def __str__(self):
        return self.nick
    
    def save(self, *args, **kwargs):
        if not self.nick:
            self.nick = self.user.username
        super().save(*args, **kwargs)