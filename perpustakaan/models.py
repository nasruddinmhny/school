from django.db import models

# Create your models here.
class Buku(models.Model):
    bukuId  = models.CharField(max_length=50,null=False,blank=False,verbose_name="Buku ID")
    judul   = models.CharField(max_length=250,null=False,blank=False, verbose_name="Judul")
    isbn    = models.CharField(max_length=50, null=True,blank=True,verbose_name="ISBN")
    tahunTerbit = models.CharField(max_length=20,null=True,blank=True,verbose_name="Tahun Terbit")
    sinopsis = models.TextField(null=False,blank=False,verbose_name="Sinopsis") 
    
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

    def __str__(self):
        return self.namapenulis
    
class HistoryPendidikan(models.Model):
    penulis = models.ForeignKey(Penulis,on_delete=models.CASCADE,null=True, blank=True, verbose_name='Penulis')
    pendidikan = models.ForeignKey(Pendidikan,on_delete=models.CASCADE, null=True, blank=True, verbose_name='Pendidikan')
    
    
class Penerbit(models.Model):
    penerbitId = models.CharField(max_length=50,null=False,blank=False,verbose_name="Penerbit ID")
    namapenerbit = models.CharField(max_length=200,null=False,blank=False,verbose_name="Nama Penerbit")
    
    def __str__(self):
        return self.namapenerbit