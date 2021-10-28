from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test),
    path('test/test/', views.test2)
]