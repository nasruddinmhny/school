from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Buku,Penulis,Penerbit,Pendidikan,HistoryPendidikan
from .forms import Edit_Penulis,Tambah_Buku,Edit_Buku,Tambah_Penulis,Tambah_Pendidikan,Edit_Pendidikan
from django.contrib import messages


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
    context = {
        'buku':buku,
    }
    
    return render(request,'buku.html',context)  

def tambah_buku(request):
    
    if request.method == 'POST':
        form = Tambah_Buku(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Disimpan')
            return redirect('buku')
            
    else:
        form = Tambah_Buku()
    
    context ={
        'form':form,
    }  
        
    return render(request,'tambah_buku.html',context)


def hapus_buku(request,idbuku):
    bukuid = Buku.objects.get(id = idbuku)
    bukuid.delete()
    messages.success(request,'Data Berhasil Dihapus')
    return redirect('buku')

def edit_buku(request,idbuku):
    #bukuid = Buku.objects.get(id = idbuku)
    ambildata = Buku.objects.get(id=idbuku)
    print(ambildata)
    if request.method == "POST":
        form = Edit_Buku(request.POST, instance=ambildata)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Di Perbaharui')
            return redirect('buku')
    else:
        form = Edit_Buku(instance=ambildata)
        
    context = {
        'form':form,
    }
    return render(request,'edit_buku.html',context)

def penulis(request):
    
    #select * from buku
    penulis = Penulis.objects.all()
    context = {
        'penulis':penulis,
    }
    
    return render(request,'penulis.html',context)  

def tambah_penulis(request):
    
    if request.method == 'POST':
        form = Tambah_Penulis(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Disimpan')
            return redirect('penulis')
            
    else:
        form = Tambah_Penulis()
    
    context ={
        'form':form,
    }  
        
    return render(request,'tambah_penulis.html',context)

def edit_penulis(request,id):
    #bukuid = Buku.objects.get(id = idbuku)
    ambildata = Penulis.objects.get(id=id)
    print(ambildata)
    if request.method == "POST":
        form = Edit_Penulis(request.POST, instance=ambildata)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Di Perbaharui')
            return redirect('penulis')
    else:
        form = Edit_Penulis(instance=ambildata)
        
    context = {
        'form':form,
    }
    return render(request,'edit_penulis.html',context)

def pendidikan(request):
    
    #select * from buku
    pendidikan = Pendidikan.objects.all()
    context = {
        'pendidikan':pendidikan,
    }
    
    return render(request,'pendidikan.html',context)  

def tambah_pendidikan(request):
    
    if request.method == 'POST':
        form = Tambah_Pendidikan(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Disimpan')
            return redirect('pendidikan')
            
    else:
        form = Tambah_Pendidikan()
    
    context ={
        'form':form,
    }  
        
    return render(request,'tambah_pendidikan.html',context)


def edit_pendidikan(request,id):
    #bukuid = Buku.objects.get(id = idbuku)
    ambildata = Pendidikan.objects.get(id=id)
    print(ambildata)
    if request.method == "POST":
        form = Edit_Pendidikan(request.POST, instance=ambildata)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Di Perbaharui')
            return redirect('pendidikan')
    else:
        form = Edit_Pendidikan(instance=ambildata)
        
    context = {
        'form':form,
    }
    return render(request,'edit_pendidikan.html',context)


def view_penulis(request,id):
    view = Penulis.objects.filter(id=id).first()
    history = HistoryPendidikan.objects.filter(penulis_id = id)
    print('history = ',history)
    
    
    context = {
        'view':view,
        'history':history,
    }
    
    return render(request,'view_penulis.html',context)