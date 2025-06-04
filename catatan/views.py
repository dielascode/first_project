from django.shortcuts import render
from .models import Catatan
# Create your views here.
def beranda(request):
    data = Catatan.objects.all().order_by('-tanggal')
    return render(request, 'catatan/beranda.html', {'catatan':data})
