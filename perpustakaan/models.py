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