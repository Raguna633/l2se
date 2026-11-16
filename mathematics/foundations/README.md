# Matematika — Fondasi Berpikir *Engineer*

> Matematika adalah bahasa untuk memodelkan dunia: mengukur, memprediksi, merancang, dan membuktikan. Topik ini membangun matematika **dari prinsip dasar**, mulai dari pecahan dan rasio sampai kalkulus, aljabar linier, persamaan diferensial, dan metode numerik, dengan satu tujuan: pelajar mampu bernalar tentang masalah yang belum pernah ia lihat, seperti seorang *engineer*.
>
> **Untuk siapa:** pelajar SD–SMA, mahasiswa, *engineer*, guru/dosen, dan pembelajar umum. Titik awal dan kedalaman disesuaikan dengan `LEARNER.md`. Minta AI Mentor: `"sesuaikan topik matematika"`.

**Panduan AI Mentor:** [rules.md](rules.md) (Bagian 1: peran & prinsip) · [rules-misconceptions-and-assessment.md](rules-misconceptions-and-assessment.md) (Bagian 2: miskonsepsi & asesmen) · [roadmap.md](roadmap.md) (fase belajar) · [Protokol STEM](../../docs/stem-pedagogy.md)

---

## 1. Ikhtisar & Target

* **Target Kompetensi Umum:** memahami *asal-usul* konsep (bukan hanya rumus), menerjemahkan masalah nyata menjadi model matematika, memeriksa kewajaran hasil, dan menjelaskan penalaran secara runtut.
* **Alokasi Waktu:** fleksibel; contoh ritme ~3–6 jam per minggu. Sesuaikan dengan `LEARNER.md`.
* **Prasyarat:** tidak ada. Mulai dari fase yang sesuai hasil diagnosis (lihat [roadmap.md](roadmap.md)).
* **Jenjang Sasaran:** SD/SMP sampai universitas tahun 1–2 dan praktisi rekayasa/CS.
* **Kaitan Dunia Nyata:** rasio dan skala (resep, peta, *engineering drawing*), fungsi dan grafik (data, sensor), statistika (keputusan berbasis data), kalkulus (laju perubahan, optimasi), aljabar linier (grafika komputer, *machine learning*), persamaan diferensial (rangkaian, populasi, pendinginan), matematika diskrit (algoritma, kriptografi), metode numerik (simulasi).

---

## 2. Jalur Jenjang

Jalur bukan tangga kaku. Pelajar boleh berada di jalur berbeda untuk area berbeda, mis. kuat di aljabar tetapi perlu mengulang pecahan.

| Jalur | Fase Roadmap | Target Kompetensi | Contoh "Bukti" Penguasaan |
|---|---|---|---|
| **A. Fondasi (SD akhir–SMP)** | Fase 0–2 | Lancar bernalar dengan pecahan, rasio, persen, bilangan negatif; memahami variabel sebagai "bilangan yang belum diketahui atau berubah"; menyusun dan menyelesaikan persamaan linier; luas, volume, Pythagoras. | Menjelaskan *mengapa* $\frac{1}{2} \div \frac{1}{4} = 2$ dengan gambar; menyusun persamaan dari cerita soal. |
| **B. SMA** | Fase 2–6 (awal) | Trigonometri, fungsi dan grafik (linier, kuadrat, eksponensial, logaritma), statistika deskriptif dan peluang dasar, pengantar limit dan turunan. | Membaca grafik untuk memprediksi; menurunkan rumus jumlah deret aritmetika; menjelaskan arti turunan sebagai laju perubahan. |
| **C. Universitas Tahun 1–2** | Fase 5–9 | Kalkulus diferensial & integral, aljabar linier, persamaan diferensial biasa, matematika diskrit, statistika inferensial dasar, bukti matematis sederhana. | Menurunkan aturan turunan dari definisi limit; menafsirkan matriks sebagai transformasi; memodelkan pendinginan dengan PD orde satu. |
| **D. Matematika untuk Rekayasa/CS** | Fase 7–10 + proyek | Memilih model dan metode yang tepat, memahami galat numerik, memakai kode (Python/NumPy) untuk eksplorasi, menimbang *trade-off* akurasi vs biaya komputasi. | Membandingkan metode Euler dan solusi eksak; menjelaskan kenapa `0.1 + 0.2` tidak tepat sama dengan `0.3` di komputer (bersama CS Tutor). |

**Kesetaraan dengan kurikulum sekolah:** jalur di bawah ini disusun menurut prasyarat konsep, bukan menurut kurikulum negara tertentu. Pemetaannya ke kelas dan fase berbeda antar negara dan berubah antar tahun, jadi **cocokkan dengan kurikulum, buku, dan silabus yang dipakai pelajar** (sebutkan di `LEARNER.md`; mentor akan menyesuaikan).

---

## 3. Roadmap

Urutan lengkap berdasarkan prasyarat, beserta intuisi, kaitan rekayasa, ide proyek, dan "tanda sudah menguasai": **[roadmap.md](roadmap.md)**.

Ringkasan urutan: Fase 0 Bilangan & aritmetika → 1 Aljabar → 2 Geometri & trigonometri → 3 Fungsi & grafik → 4 Statistika & peluang → 5 Kalkulus diferensial → 6 Kalkulus integral → 7 Aljabar linier → 8 Persamaan diferensial → 9 Matematika diskrit → 10 Metode numerik.

---

## 4. Sumber Rujukan Utama

Semua sumber di bawah gratis dan terbuka. URL yang tercantum sudah diperiksa saat ditulis; bila tautan berubah, cari dari situs induknya.

* **Buku teks terbuka:** [OpenStax Math](https://openstax.org/subjects/math), mis. [Prealgebra 2e](https://openstax.org/details/books/prealgebra-2e), [Algebra and Trigonometry 2e](https://openstax.org/details/books/algebra-and-trigonometry-2e), [Calculus Volume 1](https://openstax.org/details/books/calculus-volume-1), [Introductory Statistics 2e](https://openstax.org/details/books/introductory-statistics-2e).
* **Latihan bertahap:** [Khan Academy Math](https://www.khanacademy.org/math).
* **Intuisi visual:** [3Blue1Brown](https://www.3blue1brown.com/) (seri *Essence of Linear Algebra* dan *Essence of Calculus*).
* **Catatan kuliah:** [Paul's Online Notes](https://tutorial.math.lamar.edu/) (aljabar, kalkulus, persamaan diferensial).
* **Kuliah terbuka (MIT OpenCourseWare):** [18.01SC Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/), [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), [18.06 Linear Algebra (Gilbert Strang)](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/), [18.03SC Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/), [6.042J Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/). Dampingi dengan `"dampingi kuliah [judul/URL]"`.
* **Buku (tanpa tautan):** George Pólya, *How to Solve It*; Gilbert Strang, *Introduction to Linear Algebra*.
* **Alat praktik:** kertas & pensil, kalkulator, spreadsheet, [GeoGebra](https://www.geogebra.org/), [Desmos](https://www.desmos.com/), Python (NumPy, Matplotlib).

---

## 5. Project Showcase & Praktik (`projects/`)

*(Proyek besar sebaiknya dikelola di repositori terpisah lalu ditautkan di sini. Folder lokal `projects/` dipakai untuk eksperimen kecil, buku catatan, atau lembar kerja.)*

| Nama Proyek / Karya | Jenis | Deskripsi Singkat | Alat / Media | Tautan | Status |
|---|---|---|---|---|---|
| *(Contoh: Eksplorasi Fungsi Kuadrat)* | Eksperimen | Mengubah $a, b, c$ pada $y = ax^2 + bx + c$ dan menjelaskan efeknya | Desmos / GeoGebra | `[Tautan](...)` | [ ] Rencana |
| *(Contoh: Simulasi Pendinginan Kopi)* | Proyek | Model PD orde satu, dibandingkan dengan data termometer | Python / spreadsheet | `[Tautan](...)` | [ ] Rencana |
| *(Contoh: Survei & Analisis Data Kelas)* | Karya Ilmiah | Pertanyaan riset, pengambilan data, statistika deskriptif, keterbatasan | Spreadsheet / laporan | `[Tautan](...)` | [ ] Rencana |
| *(Contoh: Persiapan OSN/kompetisi)* | Kompetisi | Catatan strategi dan soal latihan dari arsip resmi (bukan soal yang sedang berjalan) | Kertas / catatan | `[Tautan](...)` | [ ] Rencana |

Jenis karya: **Proyek** (kode, model, alat), **Eksperimen** (eksplorasi atau pengukuran), **Karya Ilmiah** (laporan, esai, publikasi), **Kompetisi** (olimpiade, lomba).

---

## 6. Struktur Folder Topik Ini

```text
mathematics/foundations/
├── README.md                                # Dokumen ini (jalur, target, sumber, showcase)
├── roadmap.md                               # Fase belajar berurutan berdasar prasyarat
├── rules.md                                 # Aturan AI Mentor Matematika (Bagian 1)
├── rules-misconceptions-and-assessment.md   # Miskonsepsi, soal terbuka, rubrik (Bagian 2)
├── notes/
│   ├── learning-log.md                      # Riwayat sesi, kuis ulang, daftar parkir
│   └── glossary.md                          # Istilah teknis (asli ↔ Indonesia)
└── projects/                                # Eksperimen, simulasi, laporan, karya
```

Log: [notes/learning-log.md](notes/learning-log.md) · Glosarium: [notes/glossary.md](notes/glossary.md)
