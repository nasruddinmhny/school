from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import PeminjamanBuku,CustomUser,SumberDayaManusia,Buku,Penulis,Penerbit,Pendidikan,HistoryPendidikan,Sekolah
from .forms import FilterTanggalPinjamForm,UbahStatusPeminjaman,CreateCustomeUser,Tambah_sdm,Tambah_sekolah,Tambah_History_Pendidikan,Edit_Penulis,Tambah_Buku,Edit_Buku,Tambah_Penulis,Tambah_Pendidikan,Edit_Pendidikan
from django.contrib import messages
from perpustakaan.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.db.models import Count,Q

from django.utils import timezone

#pdf 
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


# Create your views here.
def loginpage(request):
    return render(request,'login.html')

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Not allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
        #user = request.POST.get('username')
        print(user)
        if user != None:
            login(request,user)
            user_type = user.user_type
            cus = CustomUser.objects.filter(username = user).first()
            print(cus)
            
            if user_type == '1':
                return redirect('admin_dashboard')
                #return HttpResponse('<h1>Selamat datang admin_home</h2>')
            elif user_type == '2': 
                return redirect('anggota_dashboard')
                #return HttpResponse('<h1>Selamat datang anggota</h2>')
            else:
                messages.error(request,'Login Gagal')
                return redirect('login')
        else:
            messages.error(request, "Login Gagal.")
            return redirect('login')


def admin_dashboard(request):
    
    jumlahBuku = Buku.objects.all().count()
    jumlahPenulis = Penulis.objects.all().count()
    
    context = {
        'jumlah':jumlahBuku,
        'jumlahPenulis':jumlahPenulis,
    }
    return render(request,'admin_home/dashboard.html',context)

def profil(request):
    return render(request,'admin_home/profil.html')

def kontak(request):
    pass

def buku(request):
    
    #select * from buku
    buku = Buku.objects.all()
    context = {
        'buku':buku,
        'title': 'Manage Buku',
    }
    
    return render(request,'admin_home/buku.html',context)  

def tambah_buku(request):
    
    if request.method == 'POST':
        form = Tambah_Buku(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Disimpan')
            return redirect('buku')
            
    else:
        form = Tambah_Buku()
    
    context ={
        'form':form,
    }  
        
    return render(request,'admin_home/tambah_buku.html',context)


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
        form = Edit_Buku(request.POST,request.FILES, instance=ambildata)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Di Perbaharui')
            return redirect('buku')
    else:
        form = Edit_Buku(instance=ambildata)
        
    context = {
        'form':form,
    }
    return render(request,'admin_home/edit_buku.html',context)

def penulis(request):
    
    #select * from buku
    penulis = Penulis.objects.all()
    context = {
        'penulis':penulis,
    }
    
    return render(request,'admin_home/penulis.html',context)  

def tambah_penulis(request):
    
    if request.method == 'POST':
        form = Tambah_Penulis(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Disimpan')
            return redirect('penulis')
            
    else:
        form = Tambah_Penulis()
    
    context ={
        'form':form,
    }  
        
    return render(request,'admin_home/tambah_penulis.html',context)

def edit_penulis(request,id):
    #bukuid = Buku.objects.get(id = idbuku)
    ambildata = Penulis.objects.get(id=id)
    print(ambildata)
    if request.method == "POST":
        form = Edit_Penulis(request.POST,request.FILES, instance=ambildata)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Di Perbaharui')
            return redirect('penulis')
    else:
        form = Edit_Penulis(instance=ambildata)
        
    context = {
        'form':form,
    }
    return render(request,'admin_home/edit_penulis.html',context)


def view_buku(request,idbuku):
    buku = Buku.objects.filter(id = idbuku).first()
    
    context = {
        'buku':buku,
    }
    return render(request,'admin_home/view_buku.html',context)



def pendidikan(request):
    
    #select * from buku
    pendidikan = Pendidikan.objects.all()
    context = {
        'pendidikan':pendidikan,
    }
    
    return render(request,'admin_home/pendidikan.html',context)  

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
        
    return render(request,'admin_home/tambah_pendidikan.html',context)


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
    return render(request,'admin_home/edit_pendidikan.html',context)


def view_penulis(request,id):
    view = Penulis.objects.filter(id=id).first()
    history = HistoryPendidikan.objects.filter(penulis_id = id)
    print('history = ',history)
    
    
    context = {
        'view':view,
        'history':history,
    }
    
    return render(request,'admin_home/view_penulis.html',context)

def tambah_history_pendidikan(request,idpenulis):
    
    #select * from penulis where id = idpenulis
    penulisid = Penulis.objects.get(id=idpenulis)
    
    if request.method == "POST":
        form = Tambah_History_Pendidikan(request.POST)
        if form.is_valid():
            writer = form.save(commit=False)
            writer.penulis_id =  penulisid.id
            #print(writer.penulis_id)
            form.save()
            messages.success(request,'Data Pendidikan Berhasil Ditambah')
            return redirect('view_penulis',id = penulisid.id)
    else:
        form = Tambah_History_Pendidikan()
        
    context = {
        'form':form,
    }
    return render(request,'admin_home/tambah_history_pendidikan.html',context)
    
def sekolah(request):
    sekolah = Sekolah.objects.all()
    
    context = {
        'sekolah':sekolah,
        'title':'MANAGE SEKOLAH',
    }
    
    return render(request,'admin_home/sekolah.html',context)


def tambah_sekolah(request):
    
    if request.method == "POST":
        form = Tambah_sekolah(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Sekolah Disimpan')
            return redirect('sekolah')
    else:
        form = Tambah_sekolah()
    
    context = {
        'form':form,
    }
    return render(request,'admin_home/tambah_sekolah.html',context)


def sumberdayamanusia(request):
    sdm = SumberDayaManusia.objects.all()
    
    context = {
        'sdm':sdm,
    }
    return render (request,'admin_home/sdm.html',context)


def tambah_sdm(request):
    
    if request.method == "POST":
        form = Tambah_sdm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Ditambah') 
            return redirect('sdm')
    else:
        form = Tambah_sdm()
        
    context = {
        'form':form,
    }   
    return render(request,'admin_home/tambah_sdm.html',context)


def manage_akun_anggota(request):
    
    akun = CustomUser.objects.all()
    
    context = {
        'title':'MANAGE AKUN ANGGOTA',
        'akunanggota':akun,
    }
    return render (request,'admin_home/manage_akun_anggota.html',context)

def tambah_user_anggota(request):
    
    if request.method == "POST":
        form = CreateCustomeUser(request.POST)
        if form.is_valid():
            frm = form.save(commit=False)
            frm.user_type = 2
            frm.save()
            messages.success(request,'Akun Berhasil Dibuat')
            return redirect('manage_akun_anggota')
    else:
        form = CreateCustomeUser()
    
    context = {
        'title':'FORM TAMBAH USER ANGGOTA',
        'form':form,
    }
    return render(request,'admin_home/tambah_akun_anggota.html',context)


def logout_user(request):
    logout(request)
    return redirect('loginpage')


def list_peminjam_buku(request):
    list_peminjam = PeminjamanBuku.objects.all()
    
    context = {
        'title':'DAFATAR PEMINJAM',
        'list_peminjam':list_peminjam,
    }
    
    return render(request,'admin_home/daftar_peminjaman_buku.html',context)

'''
def ubah_status_peminjaman(request,id):
    
    ambil_id_peminjaman = get_object_or_404(PeminjamanBuku, id=id)
    hari_ini = timezone.localdate()
    
    if request.method == "POST":
        form = UbahStatusPeminjaman(request.POST,instance=ambil_id_peminjaman)
        if form.is_valid():
            ubah = form.save(commit=False)
            ubah.status = 'Kembali'
            ubah.tanggal_pengembalian = hari_ini
            ubah.save()
            messages.success(request,'Status Berhasil Di ubah')
        else:
            messages.error(request,'Status gagal di ubah')
            
    
    return redirect('list_peminjam_buku')
'''
def ubah_status_peminjaman(request, id):
    peminjaman = get_object_or_404(PeminjamanBuku, id=id)
    if request.method == "POST":
        peminjaman.status = "Kembali"
        peminjaman.tanggal_pengembalian = timezone.localdate()
        peminjaman.save(update_fields=["status", "tanggal_pengembalian"])
        messages.success(request, "Status berhasil diubah menjadi Kembali.")
    return redirect("list_peminjam_buku")


def rekap_anggota_pinjam(request):
    rekap = (
                PeminjamanBuku.objects
                .values(
                    'customuser__id','customuser__username'
                ).annotate(
                    jumlah_buku = Count('id'),
                    #menghitung jumlah buku yang sudah kembali berdasarkan tanggal kembali
                    jumlah_kembali = Count('id',filter=Q(tanggal_pengembalian__isnull = False)),
                    #menghitung jumlah buku yang belum kembali berdasarkan tanggal kembali
                    jumlah_belum_kembali = Count('id',filter=Q(tanggal_pengembalian__isnull = True)),
                    
                ).order_by('customuser__username')
             
             )
    
    context ={
        'title':'REKAP PEMINJAMAN BUKU',
        'rekap':rekap,
    }
    return render(request,'admin_home/rekap_anggota_pinjam.html',context)


def rekap_anggota(request):
    rekap = CustomUser.objects.all()
    statistik = CustomUser.objects.aggregate(
            jumlah_aktif = Count('id',filter=Q(is_active=True)),
            jumlah_tidak_Aktif = Count('id',filter=Q(is_active=False)),
            total_anggota = Count('id')
    )
    
    context={
        'title':'REKAP ANGGOTA',
        'rekap':rekap,
       'statistik':statistik,
    }
    return render(request,'admin_home/rekap_anggota.html',context)


def laporan_anggota_pdf(request):
    statistik = CustomUser.objects.aggregate(
        total=Count('id'),
        aktif=Count('id', filter=Q(is_active=True)),
        tidak_aktif=Count('id', filter=Q(is_active=False)),
    )

    # === ambil data anggota (opsional) ===
    anggota = CustomUser.objects.all().order_by('username')
    
      # === response PDF ===
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="laporan_anggota.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []
    
     # === Judul ===
    elements.append(Paragraph("<b>LAPORAN DATA ANGGOTA PERPUSTAKAAN</b>", styles['Title']))
    elements.append(Spacer(1, 12))

    # === Ringkasan ===
    elements.append(Paragraph(f"Jumlah Anggota : {statistik['total']}", styles['Normal']))
    elements.append(Paragraph(f"Anggota Aktif : {statistik['aktif']}", styles['Normal']))
    elements.append(Paragraph(f"Anggota Tidak Aktif : {statistik['tidak_aktif']}", styles['Normal']))
    elements.append(Spacer(1, 16))

    # === Tabel detail anggota ===
    table_data = [
        ["No", "Username", "Status"]
    ]

    for i, a in enumerate(anggota, start=1):
        status = "Aktif" if a.is_active else "Tidak Aktif"
        table_data.append([i, a.username, status])

    table = Table(table_data, colWidths=[40, 200, 120])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('ALIGN', (-1,1), (-1,-1), 'CENTER'),
        ('FONT', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 10),
    ]))

    elements.append(table)

    doc.build(elements)
    return response

def peminjaman_filter_tanggal_pinjam(request):
    form = FilterTanggalPinjamForm(request.GET or None)

    # Default: jangan tampilkan data sebelum user filter
    daftar = PeminjamanBuku.objects.none()
    tampilkan = False

    if form.is_valid():
        mulai = form.cleaned_data["mulai"]
        selesai = form.cleaned_data["selesai"]

        daftar = (
            PeminjamanBuku.objects
            .select_related("customuser", "buku")
            .filter(tanggal_pinjam__range=(mulai, selesai))
            .order_by("-tanggal_pinjam")
        )
        tampilkan = True

    context = {
        "title": "Filter Peminjaman (Berdasarkan Tanggal Pinjam)",
        "form": form,
        "daftar": daftar,
        "tampilkan": tampilkan,
    }
    return render(request, "admin_home/peminjaman_filter_pinjam.html", context)
