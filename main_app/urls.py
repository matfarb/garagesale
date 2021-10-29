from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.ProductCreate.as_view()),
    path('test/', views.test),
    path('test/test/', views.test2)
]