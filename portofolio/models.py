from django.db import models

class Proyek(models.Model):
    judul = models.CharField(max_length=150)
    deskripsi = models.TextField()
    teknologi = models.CharField(max_length=100, help_text="Contoh: Python, Django, HTML")
    link_proyek = models.URLField(blank=True, null=True)
    tanggal_dibuat = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.judul

class PesanKontak(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    pesan = models.TextField()
    waktu_kirim = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pesan dari {self.nama}"
