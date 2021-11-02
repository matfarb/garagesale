from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    for_sale = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'product_id': self.id})

    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ProductPhoto(models.Model):
  url = models.CharField(max_length=200)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for product_id: {self.product_id} @{self.url}"

class Profile(models.Model):
    COLOR_CHOICES = [
        ("blue", "Blue"), 
        ("green", "Green"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    favorite_color = models.CharField(max_length=50, blank=True, default="blue")

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('profile')
