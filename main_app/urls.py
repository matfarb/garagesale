from django.urls import path
from . import views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/create', views.ProductCreate.as_view(), )
]