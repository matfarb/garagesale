from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls.base import reverse

from .models import Product, Profile
from django.views.generic.edit import CreateView, UpdateView

def home(request):
  return render(request, 'home.html')

def marketplace(request):
  products = Product.objects.all()
  return render(request, 'products/marketplace.html', { 'products': products})

def inventory(request):
  products = Product.objects.filter(user=request.user)
  return render(request, 'products/inventory.html', { 'products': products})

def products_detail(request, product_id):
  product = Product.objects.get(id=product_id)
  return render(request, 'products/detail.html', { 
    'product': product
  })

class ProductCreate(CreateView):
  model = Product
  fields = '__all__'

  def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)

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


def profile(request):
  print(request.user.id)
  p = Profile.objects.filter(user_id=request.user.id)
  if len(p) > 0:
    print("USER PROFILE FOUND")
    return render(request, 'users/index.html')
  else:
    print("USER PROFILE NOT FOUND")
    return render(request, 'users/add_profile.html')


class ProfileCreate(CreateView):
    model = Profile
    fields = ['bio', 'favorite_color']

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

    success_url = '/profile/'

class ProfileUpdate(UpdateView):
  model = Profile
  fields = ['bio', 'favorite_color']




