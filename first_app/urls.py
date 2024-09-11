from django.urls import path
# from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('help/', views.help, name='help'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
          
]
