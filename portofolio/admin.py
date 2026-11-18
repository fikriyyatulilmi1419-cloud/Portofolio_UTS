from django.contrib import admin
from .models import Proyek, PesanKontak, Akademik

@admin.register(Proyek)
class ProyekAdmin(admin.ModelAdmin):
    list_display = ('judul', 'teknologi', 'tanggal_dibuat')
    search_fields = ('judul', 'teknologi', 'deskripsi')
    list_filter = ('tanggal_dibuat',)

@admin.register(PesanKontak)
class PesanKontakAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'waktu_kirim')
    search_fields = ('nama', 'email', 'pesan')
    list_filter = ('waktu_kirim',)
    readonly_fields = ('nama', 'email', 'pesan', 'waktu_kirim')

@admin.register(Akademik)
class AkademikAdmin(admin.ModelAdmin):
    list_display = ('nama', 'institusi', 'tahun_masuk', 'tahun_lulus')
    search_fields = ('nama', 'institusi', 'deskripsi', 'tags')
    list_filter = ('tahun_masuk', 'tahun_lulus')

