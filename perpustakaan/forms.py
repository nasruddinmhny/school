from django import forms
from .models import Buku

#class form

class Tambah_Buku(forms.ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'