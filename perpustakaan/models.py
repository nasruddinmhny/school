
# perpustakaan/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.
#custome
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('1', 'Admin'),
        ('2', 'Anggota'),
    )

    user_type = models.CharField(
        max_length=1,
        choices=USER_TYPE_CHOICES,
        default='1',
        verbose_name="Tipe User"
    )

    def __str__(self):
        return self.username



class Buku(models.Model):
    bukuId  = models.CharField(max_length=50,null=False,blank=False,verbose_name="Buku ID")
    judul   = models.CharField(max_length=250,null=False,blank=False, verbose_name="Judul")
    isbn    = models.CharField(max_length=50, null=True,blank=True,verbose_name="ISBN")
    tahunTerbit = models.CharField(max_length=20,null=True,blank=True,verbose_name="Tahun Terbit")
    stok = models.IntegerField(null=True,blank=True,verbose_name='Stok Buku')
    sinopsis = models.TextField(null=False,blank=False,verbose_name="Sinopsis") 
    foto = models.ImageField(upload_to='foto_buku',null=True, blank=True)
    
    def __str__(self):
        return self.judul
    

class Pendidikan(models.Model):
    pendidikanID = models.CharField(max_length=50,null=False,blank=False,verbose_name="Pendidikan ID")
    jenjang = models.CharField(max_length=50,null=False,blank=False,verbose_name="Jenjang Pendidikan")
    namasingkatan = models.CharField(max_length=50,null=False,blank=False,verbose_name="Singkatan")
    
    def __str__(self):
        return self.jenjang
    
class Penulis(models.Model):
    penulisId = models.CharField(max_length=50,null=False,blank=False,verbose_name="Penulis ID")
    namapenulis = models.CharField(max_length=200,null=False,blank=False,verbose_name="Nama Penulis")
    jkelamin = (
        ('PRIA','PRIA'),
        ('WANITA','WANITA'),
    )
    jk = models.CharField(max_length=50,choices=jkelamin,null=True,blank=True,verbose_name="Jenis Kelamin")
    instagram = models.CharField(max_length=50,null=True,blank=True,verbose_name="Instagram")
    foto = models.ImageField(upload_to='foto_penulis',null=True, blank=True)

    def __str__(self):
        return self.namapenulis
    
    
class Sekolah(models.Model):
    sekolahId =  models.CharField(max_length=50,null=False,blank=False,verbose_name="Sekolah ID")   
    namasekolah = models.CharField(max_length=200,null=False,blank=False,verbose_name="Nama Sekolah")
    
    def __str__(self):
        return self.namasekolah
    
    
class HistoryPendidikan(models.Model):
    penulis = models.ForeignKey(Penulis,on_delete=models.CASCADE,null=True, blank=True, verbose_name='Penulis')
    pendidikan = models.ForeignKey(Pendidikan,on_delete=models.CASCADE, null=True, blank=True, verbose_name='Pendidikan')
    sekolah = models.ForeignKey(Sekolah,on_delete=models.CASCADE,null=True,blank=True, verbose_name="Sekolah")

    
    
class Penerbit(models.Model):
    penerbitId = models.CharField(max_length=50,null=False,blank=False,verbose_name="Penerbit ID")
    namapenerbit = models.CharField(max_length=200,null=False,blank=False,verbose_name="Nama Penerbit")
    
    def __str__(self):
        return self.namapenerbit
    
    
class SumberDayaManusia(models.Model):
    nik = models.CharField(max_length=50,null=False,blank=False,verbose_name="No. Induk Kepegawaian")
    nama = models.CharField(max_length=200,null=False,blank=False,verbose_name="Nama Lengkap")
    jkelamin = (
        ('PRIA','PRIA'),
        ('WANITA','WANITA'),
    )
    jk = models.CharField(max_length=50,choices=jkelamin,null=True,blank=True,verbose_name="Jenis Kelamin")
    nohp = models.CharField(max_length=50,null=False,blank=False,verbose_name="No.Hp")
    tgllahir = models.DateField(verbose_name="Tanggal Lahir")
    tempatlahir = models.CharField(max_length=200,null=False,blank=False,verbose_name="Tempat Lahir")
    alamat = models.TextField(null=False,blank=False,verbose_name="Alamat") 
    pendidikan = models.ForeignKey(Pendidikan,on_delete=models.CASCADE, null=True, blank=True, verbose_name='Pendidikan')
    
    
    def __str__(self):
        return self.nik
    
    
class PeminjamanBuku(models.Model):
    customuser = models.ForeignKey(CustomUser,on_delete=models.CASCADE, verbose_name='Nama')
    buku = models.ForeignKey(Buku,on_delete=models.CASCADE, verbose_name='Buku')
    tanggal_pinjam = models.DateField(verbose_name='Tanggal Pinjam')
    tanggal_batas_peminjaman = models.DateField(verbose_name='Tanggal Berakhir')
    tanggal_pengembalian = models.DateField(blank=True, null=True,verbose_name='Tanggal Pengembalian')
    status_pinjam = (
        ('Pinjam','Pinjam'),
        ('Kembali','Kembali')
    )
    status = models.CharField(max_length=50, choices=status_pinjam,verbose_name='Status Peminjaman', null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.customuser.username 
    
    @property
    def sisa_hari(self):
        hari_ini = timezone.localdate() #mengambil tanggal hari ini
        return (self.tanggal_batas_peminjaman - hari_ini).days
    
    
    @property
    def hari_terlambat(self):
        
        if self.tanggal_pengembalian:
            #mencari selisih antar tanggal pengembalian/tgl hari ini dengan tgl_batas_peminjaman
            selisih = (self.tanggal_pengembalian - self.tanggal_batas_peminjaman).days
        else:
            hari_ini = timezone.localdate() #mengambil tanggal hari ini
            selisih = (hari_ini - self.tanggal_batas_peminjaman).days
            
        return selisih if selisih > 0 else 0 #megembalikan nilai sesuai kondisi
        
    @property
    def denda(self):
        TARIF_DENDA_PER_HARI = 2000 # tarif dendan keterlamnbatan 1 hari
        return self.hari_terlambat * TARIF_DENDA_PER_HARI #mengembalikan dendan sesuai dengan keterlambatan