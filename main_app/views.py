from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Product
from django.views.generic.edit import CreateView

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

def signup(request):
  error_message = ''
  if request.method == 'POST':
<<<<<<< HEAD
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('inventory')
    else:
      error_message = 'Invalid sign up - try again'
=======
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
>>>>>>> 5d2c683405f87325eab81e517e1881b688d0aa85
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)