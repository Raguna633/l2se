# Rules: UI/UX Landing Page untuk Mobile

Dokumen ini adalah aturan baku (rules) untuk merancang dan membangun landing page yang nyaman di perangkat mobile. Gunakan sebagai acuan saat desain, implementasi, dan review.

> *Instruksi AI: Dokumen ini mendefinisikan peran AI agent sebagai **Mentor UI/UX Mobile-First**: pendamping yang membangun pemahaman desain, bukan pembuat halaman instan. Sebelum mengajar, baca `LEARNER.md` di root repositori (bila ada) untuk menyesuaikan bahasa, jenjang, dan analogi. Aturan inti [AGENTS.md](../../../AGENTS.md) tetap berlaku, termasuk **Integritas Akademik**, keamanan data/kredensial, dan **Tangga Bantuan L1–L4** (mulai dari pertanyaan penuntun; draf solusi L4 hanya bila diminta eksplisit setelah pelajar mencoba). Kode di [§11](#11-contoh-implementasi) adalah **contoh belajar (L3)** untuk memahami konsep, bukan untuk ditempel langsung ke proyek tugas. Lihat juga [README](README.md).*

Kata kunci penting:
- **WAJIB**: harus dipenuhi, tidak boleh dilanggar.
- **DISARANKAN**: praktik terbaik, boleh dikecualikan dengan alasan jelas.
- **HINDARI**: jangan dilakukan kecuali ada alasan kuat.

---

## Daftar Isi

1. [Prinsip Dasar](#1-prinsip-dasar)
2. [Struktur Konten](#2-struktur-konten-urutan-section)
3. [Layout dan Spacing](#3-layout-dan-spacing)
4. [Tipografi dan Warna](#4-tipografi-dan-warna)
5. [Tombol dan Area Sentuh](#5-tombol-dan-area-sentuh)
6. [Performa](#6-performa)
7. [Form](#7-form)
8. [Navigasi](#8-navigasi)
9. [Aksesibilitas](#9-aksesibilitas)
10. [Pengujian](#10-pengujian)
11. [Contoh Implementasi](#11-contoh-implementasi)
12. [Checklist Review](#12-checklist-review)

---

## 1. Prinsip Dasar

| No | Aturan | Level |
|----|--------|-------|
| 1.1 | Rancang dan tulis CSS untuk layar kecil terlebih dahulu (mobile-first), lalu perluas ke tablet dan desktop. | WAJIB |
| 1.2 | Satu halaman hanya memiliki **satu tujuan** dan **satu aksi utama** (daftar, beli, unduh). | WAJIB |
| 1.3 | Pesan inti harus bisa dipahami dalam beberapa detik, karena pengguna mobile cenderung scan, bukan membaca. | WAJIB |
| 1.4 | Prioritaskan konten yang paling penting; buang yang tidak mendukung tujuan halaman. | DISARANKAN |
| 1.5 | Banyak CTA dengan tujuan berbeda. | HINDARI |

**Alasan:** layar kecil memaksa kita fokus. Jika sebuah elemen tidak membantu pengguna mencapai aksi utama, elemen itu mengganggu.

---

## 2. Struktur Konten (Urutan Section)

Susun section dengan urutan berikut:

1. **Hero** (WAJIB)
   - Berisi: headline singkat, subheadline satu kalimat, satu CTA, dan visual pendukung.
   - Harus terlihat tanpa scroll (*above the fold*).
2. **Masalah dan solusi / value proposition** (DISARANKAN)
   - Jelaskan **manfaat** bagi pengguna, bukan sekadar daftar fitur.
3. **Fitur atau manfaat utama** (WAJIB)
   - Maksimal 3-5 poin.
   - Tampilkan sebagai kartu yang ditumpuk vertikal.
4. **Social proof** (DISARANKAN)
   - Testimoni, logo klien, atau angka (contoh: "10.000+ pengguna").
5. **FAQ** (DISARANKAN)
   - Gunakan accordion agar halaman tidak terlalu panjang.
6. **CTA penutup** (WAJIB)
   - Ulangi ajakan aksi untuk pengguna yang sudah sampai bagian bawah.
7. **Footer** (WAJIB)
   - Minimal: kontak dan tautan penting saja.

---

## 3. Layout dan Spacing

| No | Aturan | Level |
|----|--------|-------|
| 3.1 | Gunakan **satu kolom** pada tampilan mobile. | WAJIB |
| 3.2 | Tidak boleh ada **scroll horizontal** dan tidak boleh memaksa pengguna zoom. | WAJIB |
| 3.3 | Beri padding samping **16-24px** agar teks tidak menempel ke tepi layar. | WAJIB |
| 3.4 | Gunakan jarak vertikal antar section yang konsisten, kelipatan 8px (32, 48, 64px). | DISARANKAN |
| 3.5 | Batasi lebar maksimum konten di layar besar (`max-width`). | DISARANKAN |

---

## 4. Tipografi dan Warna

| No | Aturan | Level |
|----|--------|-------|
| 4.1 | Ukuran teks isi **minimal 16px** agar nyaman dibaca. Khusus kolom input (`input`, `select`, `textarea`): bila font-size-nya di bawah 16px, iOS Safari otomatis zoom saat kolom itu difokuskan. | WAJIB |
| 4.2 | `line-height` paragraf sekitar **1.5**. | DISARANKAN |
| 4.3 | Rasio kontras teks terhadap latar **minimal 4.5:1** (WCAG AA). | WAJIB |
| 4.4 | Batasi maksimal **2 font family**. | DISARANKAN |
| 4.5 | Jangan hanya mengandalkan warna untuk menyampaikan informasi (contoh: error hanya ditandai merah). | WAJIB |

**Alasan:** layar mobile sering dipakai di luar ruangan dengan cahaya terang, sehingga kontras rendah sulit dibaca.

---

## 5. Tombol dan Area Sentuh

| No | Aturan | Level |
|----|--------|-------|
| 5.1 | Ukuran target sentuh **minimal 44x44px** (Apple) atau **48x48dp** (Material Design). | WAJIB |
| 5.2 | Beri jarak antar elemen yang bisa diklik agar tidak salah tekan. | WAJIB |
| 5.3 | Letakkan CTA utama di **thumb zone** (bagian bawah layar), misalnya dengan sticky CTA. | DISARANKAN |
| 5.4 | Beri umpan balik visual saat tombol ditekan (`:active`). | DISARANKAN |
| 5.5 | Teks tombol berupa kata kerja yang jelas ("Daftar Sekarang"), bukan "Klik di sini". | DISARANKAN |

---

## 6. Performa

Pengguna mobile sering memakai jaringan lambat. Target **Core Web Vitals** (ambang "baik" menurut web.dev, diukur pada **persentil ke-75 / p75** kunjungan):

| Metrik | Penjelasan | Target |
|--------|------------|--------|
| LCP | Kecepatan konten utama muncul | ≤ 2,5 detik |
| INP | Responsivitas terhadap interaksi | ≤ 200 ms |
| CLS | Pergeseran layout tak terduga | ≤ 0,1 |

Aturan:

| No | Aturan | Level |
|----|--------|-------|
| 6.1 | Kompres gambar dan gunakan format modern (**WebP/AVIF**). | WAJIB |
| 6.2 | Gunakan `srcset` dan `sizes` agar ponsel tidak mengunduh gambar ukuran desktop. | WAJIB |
| 6.3 | Selalu tulis atribut `width` dan `height` pada gambar untuk mencegah CLS. | WAJIB |
| 6.4 | Gunakan `loading="lazy"` untuk gambar **di bawah fold**. | WAJIB |
| 6.5 | **Jangan** pasang `loading="lazy"` pada gambar hero di atas fold (memperlambat LCP). | WAJIB |
| 6.6 | Kurangi JavaScript yang tidak perlu. | DISARANKAN |

---

## 7. Form

| No | Aturan | Level |
|----|--------|-------|
| 7.1 | Gunakan tipe input yang tepat: `type="email"`, `type="tel"` untuk nomor telepon, dan `inputmode="numeric"` untuk angka murni (mis. kode OTP). | WAJIB |
| 7.2 | Tambahkan atribut `autocomplete` (contoh: `autocomplete="email"`). | DISARANKAN |
| 7.3 | Minta data **seminimal mungkin**. Setiap kolom tambahan menurunkan konversi. | WAJIB |
| 7.4 | Selalu gunakan `<label>`. Placeholder bukan pengganti label karena hilang saat mengetik. | WAJIB |
| 7.5 | Tampilkan pesan error yang jelas, tepat di dekat kolom yang bermasalah. | DISARANKAN |

---

## 8. Navigasi

| No | Aturan | Level |
|----|--------|-------|
| 8.1 | Sederhanakan navigasi. Landing page cukup dengan logo dan satu tombol CTA. | DISARANKAN |
| 8.2 | Menu panjang yang mengalihkan perhatian. | HINDARI |
| 8.3 | Jika memakai hamburger menu, ikon minimal 44px dan beri `aria-label`. | WAJIB |

---

## 9. Aksesibilitas

| No | Aturan | Level |
|----|--------|-------|
| 9.1 | Gunakan elemen HTML semantik (`<header>`, `<main>`, `<section>`, `<button>`), bukan `<div>` untuk semuanya. | WAJIB |
| 9.2 | Semua elemen interaktif harus bisa dijangkau dan memiliki **fokus yang terlihat**. | WAJIB |
| 9.3 | Setiap gambar informatif memiliki atribut `alt` yang bermakna. | WAJIB |
| 9.4 | Gambar dekoratif diberi `alt=""` agar diabaikan pembaca layar. | DISARANKAN |

---

## 10. Pengujian

| No | Aturan | Level |
|----|--------|-------|
| 10.1 | Uji di **perangkat asli**, minimal satu Android dan satu iPhone jika memungkinkan. DevTools saja tidak cukup. | WAJIB |
| 10.2 | Jalankan **Lighthouse** (Chrome DevTools) untuk performa, aksesibilitas, dan SEO. | WAJIB |
| 10.3 | Simulasikan jaringan lambat lewat DevTools (throttling **Slow 4G**). | DISARANKAN |

---

## 11. Contoh Implementasi

### 11.1 Viewport meta tag

```html
<!-- Tanpa ini, browser mobile menampilkan halaman seolah layar desktop lalu mengecilkannya -->
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

**Penjelasan:**
- `width=device-width` membuat lebar halaman mengikuti lebar layar perangkat.
- `initial-scale=1` mengatur zoom awal 100%.
- `viewport-fit=cover` membuat halaman mengisi seluruh layar (termasuk area notch/home indicator); tanpanya, `env(safe-area-inset-*)` pada contoh 11.4 umumnya bernilai 0. Bila memakainya, gunakan `env(safe-area-inset-*)` agar konten penting tidak tertutup.
- Wajib ada pada semua halaman responsif.

### 11.2 CSS mobile-first

```css
/* Gaya DEFAULT = untuk mobile (tanpa media query) */
.container {
  padding: 16px;          /* jarak aman dari tepi layar */
  max-width: 1100px;      /* batasi lebar di layar besar */
  margin: 0 auto;         /* pusatkan container */
}

body {
  font-size: 16px;        /* ukuran teks minimal yang nyaman */
  line-height: 1.5;       /* jarak antar baris */
}

.features {
  display: grid;
  grid-template-columns: 1fr;  /* mobile: 1 kolom */
  gap: 16px;                   /* jarak antar kartu */
}

/* Baru di layar lebih lebar, kita tambah kolom */
@media (min-width: 768px) {
  .features {
    grid-template-columns: repeat(3, 1fr); /* tablet/desktop: 3 kolom */
  }
}
```

**Penjelasan:**
- Gaya dasar ditulis untuk mobile, lalu `min-width` hanya menambahkan penyesuaian untuk layar lebih besar.
- Pendekatan ini lebih ringan dan mudah dirawat daripada menulis gaya desktop lalu menimpanya untuk mobile.
- `gap` mengatur jarak antar kartu tanpa perlu margin manual.

### 11.3 Tombol CTA yang ramah sentuhan

```css
.btn-primary {
  display: block;
  width: 100%;              /* penuh lebar agar mudah ditekan */
  min-height: 48px;         /* memenuhi standar target sentuh */
  padding: 12px 24px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 8px;
  border: none;
  background: #1a56db;
  color: #fff;              /* kontras tinggi terhadap latar */
}

.btn-primary:active {
  transform: scale(0.98);   /* umpan balik visual saat ditekan */
}
```

**Penjelasan:**
- `min-height: 48px` menjamin area sentuh cukup besar.
- `width: 100%` membuat tombol mudah dijangkau ibu jari.
- Efek `:active` memberi tahu pengguna bahwa tekanan mereka terdeteksi.

### 11.4 Sticky CTA di bagian bawah

```css
.sticky-cta {
  position: fixed;          /* menempel ke layar, tidak ikut scroll */
  bottom: 0;
  left: 0;
  right: 0;
  padding: 12px 16px;
  /* env(...) menghindari area home indicator di iPhone;
     umumnya baru bernilai > 0 bila meta viewport memuat viewport-fit=cover (11.1) */
  padding-bottom: calc(12px + env(safe-area-inset-bottom));
  background: #fff;
  box-shadow: 0 -2px 8px rgba(0,0,0,0.1); /* pemisah visual dari konten */
}

/* Ruang tambahan agar konten terakhir tidak tertutup tombol sticky */
body {
  padding-bottom: 80px;
}
```

**Penjelasan:**
- `position: fixed` membuat tombol selalu terlihat dan berada di thumb zone.
- `safe-area-inset-bottom` mencegah tombol tertutup indikator gestur di perangkat modern (pastikan meta viewport memuat `viewport-fit=cover`).
- `padding-bottom` pada `body` memastikan konten paling bawah tidak terhalang tombol.

### 11.5 Gambar responsif dan hemat data

```html
<!-- Gambar hero (di atas fold): TANPA loading="lazy", diprioritaskan -->
<img
  src="hero-800.webp"
  srcset="hero-400.webp 400w, hero-800.webp 800w, hero-1200.webp 1200w"
  sizes="100vw"
  width="800" height="600"
  alt="Pengguna sedang memakai aplikasi di ponsel"
  fetchpriority="high">

<!-- Gambar di bawah fold: boleh lazy -->
<img src="fitur-400.webp" width="400" height="300"
  alt="Tampilan fitur jadwal" loading="lazy">
```

**Penjelasan:**
- `srcset` dan `sizes`: browser memilih ukuran gambar sesuai layar, sehingga ponsel tidak mengunduh gambar berukuran desktop.
- `width` dan `height`: memesan ruang sebelum gambar dimuat, mencegah layout bergeser (CLS).
- `fetchpriority="high"`: memberi petunjuk ke browser agar gambar hero (biasanya elemen LCP) diunduh lebih awal. Hero **tidak** diberi `loading="lazy"` (aturan 6.5), karena justru memperlambat LCP.
- `loading="lazy"`: menunda unduhan sampai gambar mendekati layar; pakai hanya untuk gambar **di bawah fold** (aturan 6.4).
- `alt`: penting untuk aksesibilitas.

### 11.6 Form yang ramah mobile

```html
<form>
  <!-- label tetap terlihat, tidak hilang seperti placeholder -->
  <label for="email">Email</label>
  <input
    id="email"
    name="email"
    type="email"          
    autocomplete="email"  
    required
    placeholder="nama@contoh.com">

  <label for="phone">Nomor HP</label>
  <input
    id="phone"
    name="phone"
    type="tel"
    autocomplete="tel">

  <button type="submit" class="btn-primary">Daftar Sekarang</button>
</form>
```

**Penjelasan:**
- `<label for="...">` terhubung ke input lewat `id`, sehingga mengetuk label ikut memfokuskan input.
- `type="email"` memunculkan keyboard dengan tombol `@`; `type="tel"` memunculkan keypad telepon (termasuk `+`), jadi untuk nomor HP cukup `type="tel"`.
- `inputmode` hanya **petunjuk** jenis keyboard, bukan paksaan atau validasi. `inputmode="numeric"` cocok untuk angka murni seperti kode OTP; jangan dipakai untuk nomor telepon karena di iOS keyboard-nya tidak menyediakan `+`.
- `autocomplete` memungkinkan browser mengisi data otomatis.
- `required` memberi validasi dasar dari browser tanpa JavaScript tambahan.
- Ingat: ukuran font input juga **minimal 16px** agar iOS tidak melakukan zoom otomatis.

---

## 12. Checklist Review

Gunakan sebelum landing page dirilis.

**Dasar**
- [ ] Viewport meta tag sudah ada
- [ ] Satu kolom, tanpa scroll horizontal
- [ ] Hanya ada satu tujuan dan satu CTA utama

**Visual**
- [ ] Teks isi ≥ 16px
- [ ] Kontras teks ≥ 4,5:1
- [ ] Padding samping 16-24px
- [ ] Maksimal 2 font family

**Interaksi**
- [ ] Target sentuh ≥ 44-48px dengan jarak yang cukup
- [ ] CTA utama terlihat di atas fold
- [ ] Ada umpan balik saat tombol ditekan

**Performa**
- [ ] Gambar dikompres (WebP/AVIF) dan responsif (`srcset`)
- [ ] `width` dan `height` ada pada semua gambar
- [ ] Lazy loading dipakai kecuali pada gambar hero
- [ ] LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 (p75)

**Form**
- [ ] Tipe input dan `autocomplete` sesuai
- [ ] Setiap input punya `<label>`
- [ ] Data yang diminta seminimal mungkin

**Aksesibilitas**
- [ ] Elemen HTML semantik
- [ ] Fokus keyboard terlihat
- [ ] Semua gambar informatif punya `alt`

**Pengujian**
- [ ] Diuji di perangkat asli (Android dan iPhone)
- [ ] Lighthouse dijalankan dan hasilnya memadai
- [ ] Diuji dengan jaringan Slow 4G
