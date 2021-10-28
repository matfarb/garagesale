from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Product
from .forms import ProductForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

## mehdi chanfe on urls gigt braasdfasdfasdfasd
## MEHIDHDDIHDID

def home(request):
  return render(request, 'home.html')

## this should just render the form ? 
@login_required
def test(request):
  product_form = ProductForm()
  return render(request, 'test.html', {
    'product_form': product_form
  })
  # return HttpResponse("test page for mehdi")

## this should save the form data?
@login_required
def test2(request):
  if request.method == 'POST':
    print(request.POST)
    form = ProductForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('test')