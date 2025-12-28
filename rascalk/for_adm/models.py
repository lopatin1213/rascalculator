from django.db import models
import random
# from django.urls import reverse
# create your models here
class AppRasCalck(models.Model):
    version = models.CharField(max_length=50)
    file = models.FileField(upload_to='media/app_files/')
    description = models.TextField()
    is_latest = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.version}'

class AndroidApp(models.Model):
    version = models.CharField(max_length=50)
    file = models.FileField(upload_to='android/app_files/')
    description = models.TextField()
    is_latest = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.version}'


class UserPro(models.Model):
    user = models.CharField(max_length=50)
    is_pro = models.BooleanField(default=False)
    pro_expiration_date = models.DateField(null=True, blank=True)
    secret_key = models.CharField(max_length=6, editable=True, default=''.join(random.choices('0123456789', k=6)))

    def __str__(self):
        return f"{self.user} - Pro: {self.is_pro}"

class news(models.Model):
    news = models.TextField()
