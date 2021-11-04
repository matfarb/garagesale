from django.urls import path, include
from . import views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/create/', views.ProductCreate.as_view(), name='product_create'),
    path('inventory/<int:pk>/update/', views.ProductUpdate.as_view(), name='products_update'),
    path('profile/', views.profile, name="profile"),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name="profile_update"),
    path('inventory/<int:product_id>', views.products_detail, name='detail'),
    path('inventory/<int:pk>/delete', views.ProductDelete.as_view(), name='product_delete'),
    path('inventory/<int:product_id>/photo_products', views.photo_products, name='photo_products'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]