from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # alex made a comment
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
]