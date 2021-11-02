from django.urls import path, include
from . import views

from . import views

urlpatterns = [
    path('inventory/create/<int:product_id>/add_photo', views.photo_products, name='photo_products'),
    path('', views.home, name='home'),
    # path('marketplace/', views.marketplace, name='index'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/create/', views.ProductCreate.as_view(), name='product_create'),
    # path('inventory/<int:product_id>', views.products_detail, name='detail'),
    path('inventory/update', views.ProductUpdate.as_view(), name='product_update'),
    path('inventory/delete', views.ProductDelete.as_view(), name='product_delete'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]