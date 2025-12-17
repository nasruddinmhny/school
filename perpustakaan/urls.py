from django.contrib import admin
from django.urls import path
from .admin_views import ubah_status_peminjaman,list_peminjam_buku,logout_user,tambah_user_anggota,manage_akun_anggota,doLogin,loginpage,tambah_sdm,sumberdayamanusia,view_buku,tambah_sekolah,sekolah,tambah_history_pendidikan,edit_penulis,view_penulis,edit_pendidikan,tambah_pendidikan,admin_dashboard,profil,buku,tambah_buku,hapus_buku,edit_buku,penulis,tambah_penulis,pendidikan
from .anggota_views import anggota_dashboard,list_buku,pinjam_buku,daftar_peminjaman_buku
urlpatterns = [
   
   #login form
   path('',loginpage,name='loginpage'),
   path('doLogin/', doLogin, name="doLogin"),
   path('logout-user/',logout_user,name='logout_user'),

   #halaman admin
   path('admin-dashboard/',admin_dashboard,name='admin_dashboard'),
   path('profil/',profil,name='profil'),
   
   path('manage-akun-anggota/',manage_akun_anggota,name='manage_akun_anggota'),
   path('tambah-akun-anggota/',tambah_user_anggota,name='tambah_user_anggota'),
   
   path('list-buku/',buku,name='buku'),
   path('tambah-buku/',tambah_buku,name='tambah_buku'),
   path('hapus-data-buku/<int:idbuku>/',hapus_buku,name='hapus_buku'),
   path('edit-buku/<int:idbuku>/',edit_buku,name='edit_buku'),
   path('view-buku/<int:idbuku>/',view_buku,name='view_buku'),
   
   path('penulis/',penulis,name='penulis'),
   path('tambah-penulis/',tambah_penulis,name='tambah_penulis'),
   path('edit-penulis/<int:id>/',edit_penulis,name='edit_penulis'),
   
   
   path('pendidikan/',pendidikan,name='pendidikan'),
   path('tambah-ppendidikan/',tambah_pendidikan,name='tambah_pendidikan'),
   path('edit-pendidikan/<int:id>/',edit_pendidikan,name='edit_pendidikan'),
   path('view-detail-penulis/<int:id>/',view_penulis,name='view_penulis'),
   
   path('tambah-history-pendidikan/<int:idpenulis>/',tambah_history_pendidikan,name='tambah_history_pendidikan'),
   
   
   path('sekolah/',sekolah, name='sekolah'),
   path('tambah-sekolah/',tambah_sekolah,name='tambah_sekolah'),
   
   path('sumber-daya-manusia/',sumberdayamanusia,name='sdm'),
   path('tambah-sdm/',tambah_sdm,name='tambah_sdm'),
   
   
   path('daftar/peminjam/buku/',list_peminjam_buku, name='list_peminjam_buku'),
   path('admin/peminjaman/<int:id>/ubah-status/', ubah_status_peminjaman, name='ubah_status_peminjaman'),

   
   #halaman anggota
   path('anggota-dashboard/',anggota_dashboard, name='anggota_dashboard'),
   path('list-buku-perpustakaan/',list_buku,name='list_buku'),
   path('anggota/buku/<int:id>/pinjam/',pinjam_buku,name='pinjam_buku'),
   path('daftar/pinjam/buku/',daftar_peminjaman_buku,name='daftar_peminjaman_buku'),
   
]