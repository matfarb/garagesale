from django.urls import path, include
from . import views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/create', views.ProductCreate.as_view(), name='product_create'),
    path('inventory/<int:pk>/update/', views.ProductUpdate.as_view(), name='products_update'),
    path('profile/', views.profile, name="profile"),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name="profile_update"),
    # path('inventory/<int:product_id>', views.products_detail, name='detail'),
    path('inventory/<int:product_id>', views.products_detail, name='detail'),
    # path('inventory/update', views.ProductUpdate.as_view(), name='product_update'),
    # path('inventory/delete', views.ProductDelete.as_view(), name='product_delete'),
    # path('invientory/<int:product_id/add_photo', views.add_photo, name='add_photo'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]