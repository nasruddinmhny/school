from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PeminjamanBuku,CustomUser,SumberDayaManusia,Buku,Penulis,Penerbit,Pendidikan,HistoryPendidikan,Sekolah
from .forms import CreateCustomeUser,Tambah_sdm,Tambah_sekolah,Tambah_History_Pendidikan,Edit_Penulis,Tambah_Buku,Edit_Buku,Tambah_Penulis,Tambah_Pendidikan,Edit_Pendidikan
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta

# Create your views here.

def anggota_dashboard(request):
    
    jumlahBuku = Buku.objects.all().count()
    jumlahPenulis = Penulis.objects.all().count()
    
    listbuku = Buku.objects.all()[:4]
    print('buku = ',listbuku)
    context = {
        'jumlah':jumlahBuku,
        'jumlahPenulis':jumlahPenulis,
        'listbuku':listbuku,
    }
    return render(request,'anggota/dashboard.html',context)

def list_buku(request):
    buku = Buku.objects.all()
    
    context = {
        'title': 'List Buku',
        'buku':buku,
    }
    
    return render(request, 'anggota/buku.html',context)

def pinjam_buku(request,id):
    buku = Buku.objects.filter(id=id).first()
    sudah_pinjam = PeminjamanBuku.objects.filter(
        customuser = request.user.id, #ngecek user login
        buku = buku,
        tanggal_pengembalian__isnull = True
    ).exists()
    
    if sudah_pinjam:
        messages.warning(request,'Kamu Masih Meminjam Buku ini dan belum di kembalikan.')
        return redirect('daftar_peminjaman_buku')
    
    tgl_pinjam = timezone.localdate() # mengambil waktu sekarang sesuai timezone
    tgl_batas = tgl_pinjam + timedelta(days=7) #menambahkan 7 hari dari tgl pinjam
    
    #insert into ke dalam tabel peminjaman
    PeminjamanBuku.objects.create(
        customuser = request.user,
        buku = buku,
        tanggal_pinjam = tgl_pinjam,
        tanggal_batas_peminjaman = tgl_batas,
        tanggal_pengembalian = None
    )
    
    buku.stok -= 1
    buku.save(update_fields=['stok'])
    
    messages.success(request,f'Buku {buku.judul} berhasil di pinjam')
    return redirect('daftar_peminjaman_buku')
    

def daftar_peminjaman_buku(request):
    daftar_buku = PeminjamanBuku.objects.all()
    
    context = {
        'title':'DAFTAR PEMINJAMAN BUKU',
        'daftar':daftar_buku,
    }
    
    return render(request,'anggota/daftar_peminjaman_buku.html',context)

