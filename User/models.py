from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profile_pictures')
    phonenumber = models.CharField(max_length=100, default='0126341709')
    def __str__(self):
        return self.user.username






















