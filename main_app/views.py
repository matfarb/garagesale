from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Product, ProductPhoto
from django.views.generic.edit import CreateView, UpdateView, DeleteView

S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'garagesaled'

def home(request):
  return render(request, 'home.html')

def inventory(request):
  products = Product.objects.filter(user=request.user)
  return render(request, 'products/inventory.html', { 'products': products})

class ProductCreate(CreateView):
  model = Product
  fields = '__all__'

  def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)

  success_url = '/inventory/'

def add_photo_products(request, product_id):
  photo_file = request.FILES.get('photo-file', None)

  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]

    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = ProductPhoto(url=url, product_id=product_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', product_id=product_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('inventory')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ProductUpdate(LoginRequiredMixin, UpdateView):
  model = Product
  fields = ['title', 'description', 'price', 'quantity', 'for sale']

class ProductDelete(LoginRequiredMixin, DeleteView):
  model = Product
  success_url = '/inventory/'

