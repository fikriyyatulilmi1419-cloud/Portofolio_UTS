document.addEventListener('DOMContentLoaded', () => {
  const header = document.getElementById('site-header');
  const mobileNav = document.getElementById('mobile-nav');

  if (!header) return;

  let lastScrollY = window.scrollY;
  const scrollThreshold = 10; // Ambang batas (px) untuk mencegah getar/jitter

  window.addEventListener('scroll', () => {
    const currentScrollY = window.scrollY;

    // 1. Efek Melayang: Beri shadow dan background saat halaman di-scroll
    if (currentScrollY > 20) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }

    // 2. Jika menu mobile sedang dibuka, navbar tetap tampil
    if (mobileNav && mobileNav.classList.contains('open')) {
      header.classList.remove('nav-hidden');
      lastScrollY = currentScrollY;
      return;
    }

    // 3. Mencegah glitch pada bounce scroll (macOS/iOS elastic scroll)
    if (currentScrollY <= 0) {
      header.classList.remove('nav-hidden');
      lastScrollY = 0;
      return;
    }

    // 4. Logika Sembunyi & Muncul:
    // Scroll ke bawah melewati 100px -> Sembunyikan navbar
    if (currentScrollY > lastScrollY + scrollThreshold && currentScrollY > 100) {
      header.classList.add('nav-hidden');
    } 
    // Scroll ke atas sedikit -> Munculkan navbar
    else if (currentScrollY < lastScrollY - scrollThreshold) {
      header.classList.remove('nav-hidden');
    }

    lastScrollY = currentScrollY;
  }, { passive: true });
});
