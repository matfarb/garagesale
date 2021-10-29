from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    for_sale = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'penguin_id': self.id})

class ProductPhoto(models.Model):
  url = models.CharField(max_length=200)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for product_id: {self.product_id} @{self.url}"
