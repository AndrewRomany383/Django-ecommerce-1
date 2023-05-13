from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

def default():
    return {"the default is":"blank"}

class product(models.Model):
    def __str__(self):
        return f'The product{self.name} uploaded by{self.seller_name}'

    def get_absolute_url(self):
        return reverse("product:products")

    seller_name = models.ForeignKey(User, on_delete=models.CASCADE, default=default)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    specs = models.TextField()
    img = models.ImageField(blank=True, upload_to="media")

class Logo(models.Model):
    logo = models.ImageField(upload_to="media")






















