from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Product
from .forms import ProductForm
from django.contrib.auth.models import User

## mehdi chanfe on urls gigt braasdfasdfasdfasd
## MEHIDHDDIHDID

def home(request):
  return render(request, 'home.html')

def test(request):
  product_form = ProductForm()
  return render(request, 'test.html', {
    'product_form': product_form
  })
  # return HttpResponse("test page for mehdi")

def test2(request):
  form = ProductForm(request.POST)
  if form.is_valid():
    product = form.save(commit=False)
    product.user = User.objects.get(user=request.user)
    product.save()
  print(Product.objects.get())
  return redirect('test')