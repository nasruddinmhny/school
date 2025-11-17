from django.shortcuts import render
from django.http import HttpResponse
from .models import Buku
from .forms import Tambah_Buku


# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')
def profil(request):
    return render(request,'profil.html')

def kontak(request):
    pass

def buku(request):
    
    #select * from buku
    buku = Buku.objects.all()
    ''' 
    bukuId = "BK001"
    judul = "Belajar Django"
    isbn = "123456"
    tahun = "2025"
    sinopsis = "Buku yang menjelaskan"
    
    context = {
        'bukuid':bukuId,
        'judul':judul,
        'isbn': isbn,
        'tahun':tahun,
        'sinopsi':sinopsis,
    }
    '''
    
    return render(request,'buku.html')  

def tambah_buku(request):
    
    if request.method == 'POST':
        form = Tambah_Buku(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Tambah_Buku()
    
    context ={
        'form':form,
    }  
        
    return render(request,'tambah_buku.html',context)
