from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class InitialPassword(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    first_password = models.CharField(null=True,max_length=50)
    first_changed = models.BooleanField(null=True)