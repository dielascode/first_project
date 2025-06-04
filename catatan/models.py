from django.db import models

# Create your models here.
class Catatan(models.Model):
    judul = models.CharField(max_length=100) #ini untuk judul, teks pendek max 100 karakter
    isi = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul