from django.contrib import admin
from django.urls import path
from .views import dashboard,profil,buku,tambah_buku

urlpatterns = [
   path('',dashboard,name='dashboard'),
   path('profil/',profil,name='profil'),
   path('list-buku/',buku,name='buku'),
   path('tambah-buku/',tambah_buku,name='tambah_buku'),
]