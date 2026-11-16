# Mobile Web UI/UX & Responsive Standards

Panduan standar baku perancangan antarmuka (*UI*) dan pengalaman pengguna (*UX*) berbasis **Mobile-First**, dioptimalkan untuk performa perangkat sentuh dan jaringan seluler.

---

## 1. Aturan Baku & Checklist
Dokumen aturan lengkap dan panduan implementasi kode CSS/HTML berada di:
* 👉 **[rules.md](rules.md)**

### Prinsip Pokok:
* **Mobile-First Layout**: Rancang 1 kolom untuk layar kecil terlebih dahulu sebelum menambahkan breakpoint tablet/desktop. Tanpa scroll horizontal.
* **Touch Targets**: Area sentuh tombol minimal **44x44px** (Apple) atau **48x48dp** (Material Design).
* **Core Web Vitals**: Target LCP < 2,5 detik, INP < 200 ms, CLS < 0,1.
* **Media & Gambar**: Format WebP/AVIF, atribut `width`/`height` untuk mencegah pergeseran layout, `loading="lazy"` di bawah fold.
* **Aksesibilitas (WCAG AA)**: Rasio kontras teks minimal 4.5:1, HTML semantik, state focus terlihat.

---

## 2. Project Showcase (*Multi-Repo*)
Proyek desain/landing page responsif dikelola sebagai repositori mandiri dan ditautkan di sini:

| Nama Proyek | Deskripsi Singkat | Stack | Repositori / Demo | Status |
|---|---|---|---|---|
| *(Belum ada)* | — | — | — | — |

---

## 3. Struktur Direktori
```text
ui-ux-mobile/
├── README.md        # Dokumen ringkasan ini
├── rules.md         # Dokumen lengkap aturan UI/UX mobile
├── notes/           # learning-log.md, glossary.md, catatan konsep
└── projects/        # Eksperimen landing page responsif, prototype komponen mobile
```

Catatan belajar: [learning-log](notes/learning-log.md) · [glosarium](notes/glossary.md)
