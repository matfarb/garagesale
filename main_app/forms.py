from django.views.generic import CreateView
from .models import Product
from django.forms import ModelForm

class ProductForm(ModelForm):
  class Meta:
    model = Product
    fields = ['title', 'description', 'price', 'quantity', 'for_sale']

  def form_valid(self, form):
    form.instance.user = self.request.user  # form.instance is the cat
    return super().form_valid(form)