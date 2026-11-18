from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Proyek, PesanKontak, Akademik


def beranda(request):
    if request.method == 'POST':
        nama = request.POST.get('nama', '').strip()
        email = request.POST.get('email', '').strip()
        pesan = request.POST.get('pesan', '').strip()

        if nama and email and pesan:
            try:
                PesanKontak.objects.create(nama=nama, email=email, pesan=pesan)
                messages.success(request, 'Terima kasih! Pesan Anda berhasil dikirim.')
            except Exception:
                messages.error(request, 'Terjadi kendala saat menyimpan pesan. Silakan coba lagi.')
            return redirect('beranda')
        else:
            messages.error(request, 'Mohon lengkapi semua kolom formulir sebelum mengirim.')
            return redirect('beranda')

    daftar_proyek = Proyek.objects.all().order_by('-tanggal_dibuat')
    
    # Data keahlian dan profil untuk kustomisasi dinamis
    keahlian_kategori = [
        {
            'kategori': 'Backend Development',
            'deskripsi': 'Membangun logika aplikasi, RESTful API, dan integrasi basis data.',
            'items': [
                {'nama': 'Python', 'level': 'Dasar'},
                {'nama': 'Django', 'level': 'Dasar'},
                {'nama': 'Supabase', 'level': 'Dasar'},
            ]
        },
        {
            'kategori': 'Frontend Development',
            'deskripsi': 'Merancang antarmuka web yang modern, interaktif, dan responsif.',
            'items': [
                {'nama': 'HTML5 & CSS3', 'level': 'Dasar'},
                {'nama': 'Tailwind CSS', 'level': 'Menengah'},
            ]
        },
        {
            'kategori': 'Tools & Workflow',
            'deskripsi': 'Perangkat pengembangan, version control, dan lingkungan kerja.',
            'items': [
                {'nama': 'Git & GitHub', 'level': 'Menengah'},
                {'nama': 'VS Code', 'level': 'Dasar'},
            ]
        }
    ]
    daftar_akademik = Akademik.objects.all().order_by('-tahun_masuk')

    context = {
        'daftar_proyek': daftar_proyek,
        'keahlian_kategori': keahlian_kategori,
        'daftar_akademik': daftar_akademik,
        
    }
    return render(request, 'portofolio/beranda.html', context)
