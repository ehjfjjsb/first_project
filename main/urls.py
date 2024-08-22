from django.urls import path
from main import views

urlpatterns = [
    path('home/', views.home),
    path('contact/', views.contact, name= 'contact'),
]

