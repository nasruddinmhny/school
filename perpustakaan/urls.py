from django.contrib import admin
from django.urls import path
from .views import edit_penulis,view_penulis,edit_pendidikan,tambah_pendidikan,dashboard,profil,buku,tambah_buku,hapus_buku,edit_buku,penulis,tambah_penulis,pendidikan

urlpatterns = [
   path('',dashboard,name='dashboard'),
   path('profil/',profil,name='profil'),
   path('list-buku/',buku,name='buku'),
   path('tambah-buku/',tambah_buku,name='tambah_buku'),
   path('hapus-data-buku/<int:idbuku>/',hapus_buku,name='hapus_buku'),
   path('edit-buku/<int:idbuku>/',edit_buku,name='edit_buku'),
   
   path('penulis/',penulis,name='penulis'),
   path('tambah-penulis/',tambah_penulis,name='tambah_penulis'),
   path('edit-penulis/<int:id>/',edit_penulis,name='edit_penulis'),
   
   
   path('pendidikan/',pendidikan,name='pendidikan'),
   path('tambah-ppendidikan/',tambah_pendidikan,name='tambah_pendidikan'),
   path('edit-pendidikan/<int:id>/',edit_pendidikan,name='edit_pendidikan'),
   path('view-detail-penulis/<int:id>/',view_penulis,name='view_penulis'),
]