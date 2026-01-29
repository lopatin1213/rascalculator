from django.db import models

# Create your models here.
class ErrorLog(models.Model):
    error_type = models.TextField()
    version = models.CharField(max_length=50)
    source = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.created_at} из {self.version}'