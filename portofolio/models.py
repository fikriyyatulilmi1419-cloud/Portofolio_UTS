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
class Akademik(models.Model):
    nama = models.CharField(max_length=100)
    institusi = models.CharField(max_length=100)
    tahun_masuk = models.IntegerField()
    tahun_lulus = models.CharField(max_length=5, blank=True, null=True, help_text="Tahun lulus bisa kosong jika masih kuliah")
    deskripsi = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True, help_text="Pisahkan tag dengan koma, misal: S1, Informatika, UNU Yogyakarta")

    def __str__(self):
        return self.nama

    def get_tags(self):
        """Memecah string tags dari database berdasarkan tanda koma menjadi list, sekaligus menghapus spasi ekstra."""
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
        return []

    @property
    def list_tags(self):
        return self.get_tags()
