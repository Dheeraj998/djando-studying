from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Places(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
