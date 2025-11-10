from django.contrib import admin
from django.urls import path
from .views import dashboard,profil,buku

urlpatterns = [
   path('dashboard/',dashboard,name='dashboard'),
   path('profil/',profil,name='profil'),
   path('list-buku/',buku,name='buku'),
]