from django.urls import path, include
from . import views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/create', views.ProductCreate.as_view(), name='product_create'),


    path('marketplace/', views.marketplace, name='index'),
    path('marketplace/<int:product_id>', views.products_detail, name='detail'),
    path('marketplace/update', views.ProductUpdate.as_view(), name='product_update'),
    path('marketplace/delete', views.ProductDelete.as_view(), name='product_delete'),
    path('marketplace/<int:product_id/add_photo', views.add_photo, name='add_photo'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]