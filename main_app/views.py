from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from django.contrib.auth.forms import UserCreationForm

from .models import Product, Profile, ProductPhoto
from django.views.generic.edit import CreateView, UpdateView, DeleteView

S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'penguincollector'

def home(request):
  return render(request, 'home.html')

def marketplace(request):
  products = Product.objects.all()
  return render(request, 'products/marketplace.html', { 'products': products})

@login_required
def inventory(request):
  products = Product.objects.filter(user=request.user)
  return render(request, 'products/inventory.html', { 'products': products})

@login_required
def products_detail(request, product_id):
  product = Product.objects.get(id=product_id)
  return render(request, 'products/detail.html', { 
    'product': product,
  })

class ProductCreate(CreateView, LoginRequiredMixin):
  model = Product
  fields = ['title', 'description', 'price', 'quantity', 'user']

  def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)

  success_url = '/inventory/'

class ProductUpdate(UpdateView, LoginRequiredMixin):
  model = Product
  fields = ['description', 'price', 'quantity']

class ProductBuy(UpdateView):
  model = Product;
  fields = ['description', 'price', 'quantity']
  success_url = '/marketplace/'

class ProductDelete(DeleteView, LoginRequiredMixin):
  model = Product
  success_url = '/inventory/'

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

@login_required
def profile(request):
  print(request.user.id)
  p = Profile.objects.filter(user_id=request.user.id)
  if len(p) > 0:
    print("USER PROFILE FOUND")
    return render(request, 'users/index.html')
  else:
    print("USER PROFILE NOT FOUND")
    return render(request, 'users/add_profile.html')


class ProfileCreate(CreateView, LoginRequiredMixin):
    model = Profile
    fields = ['bio', 'favorite_color']

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

    success_url = '/profile/'

class ProfileUpdate(UpdateView, LoginRequiredMixin):
  model = Profile
  fields = ['bio', 'favorite_color']

@login_required
def photo_products(request, product_id):
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




