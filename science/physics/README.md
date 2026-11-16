# Fisika

Fisika adalah ilmu yang mencari **aturan sederhana di balik fenomena alam**: kenapa bola jatuh, kenapa jembatan tidak runtuh, kenapa lampu menyala. Bagi calon *engineer*, fisika adalah bahasa untuk memodelkan dunia nyata: membuat asumsi, menyederhanakan, menghitung, lalu memeriksa apakah hasilnya masuk akal. Paket ini membawa pelajar dari fenomena sehari-hari sampai fondasi fisika untuk rekayasa.

> **Untuk AI Mentor:** sebelum mengajar, baca [rules.md](rules.md) (Bagian 1) dan [rules-misconceptions-and-experiments.md](rules-misconceptions-and-experiments.md) (Bagian 2), lalu terapkan [Protokol STEM](../../docs/stem-pedagogy.md). Urutan materi ada di [roadmap.md](roadmap.md).
>
> **Untuk pelajar:** pilih jalur yang sesuai di bawah, atau minta AI Mentor: `"sesuaikan topik fisika"`.

---

## 1. Ikhtisar & Target

* **Jenjang Sasaran:** semua kalangan, dari pelajar SD–SMP sampai mahasiswa, *engineer*, guru, dan pembelajar umum.
* **Alokasi Waktu:** fleksibel; sebagai patokan 3–6 jam per minggu. Satu fase roadmap umumnya 2–4 minggu.
* **Prasyarat:** berbeda per jalur (lihat tabel). Matematika yang dibutuhkan tiap fase dirujuk ke paket Matematika (`mathematics/foundations/roadmap.md`).
* **Kaitan Dunia Nyata:** struktur bangunan, kendaraan, roket dan satelit, pembangkit listrik, elektronika, perangkat medis (sinar-X, MRI), GPS, energi terbarukan.

---

## 2. Jalur Jenjang

| Jalur | Untuk Siapa | Gaya Belajar | Matematika yang Dipakai |
|---|---|---|---|
| **A. Fenomena Sehari-hari** | Pelajar SD–SMP, pembelajar umum tanpa latar matematika | Eksperimen rumahan, pengamatan, penjelasan kualitatif, estimasi sederhana | Aritmetika, pecahan, perbandingan, membaca grafik |
| **B. Fisika SMA** | Pelajar SMA/sederajat, persiapan UTBK atau olimpiade tingkat awal | Model kuantitatif, diagram benda bebas, analisis grafik, praktikum dengan laporan | Aljabar, trigonometri, vektor dasar, fungsi dan grafik |
| **C. Fisika Universitas Tahun 1–2** | Mahasiswa sains/teknik, olimpiade lanjut, pembelajar mandiri | Penurunan dari prinsip dasar, soal terbuka, analisis ketidakpastian, simulasi numerik | Kalkulus diferensial dan integral, vektor, persamaan diferensial sederhana |
| **D. Fisika untuk Rekayasa** | Mahasiswa teknik tingkat lanjut, *engineer*, guru | Pemodelan sistem nyata, *trade-off* desain, verifikasi dengan data dan simulasi | Persamaan diferensial, aljabar linier, metode numerik |

Pelajar boleh berpindah jalur kapan saja. Fase roadmap yang sama dipelajari ulang dengan kedalaman yang berbeda: jalur A menekankan "apa yang terjadi dan kenapa", jalur B menambah "berapa besarnya", jalur C menambah "dari mana rumusnya", jalur D menambah "bagaimana memakainya untuk merancang".

**Kesetaraan dengan kurikulum sekolah:** jalur A ≈ sains dasar SD–SMP, jalur B ≈ fisika SMA, jalur C ≈ fisika universitas tahun 1–2, jalur D ≈ fisika untuk rekayasa. Pembagian materi per kelas dan mata pelajaran berbeda antar negara dan berubah antar tahun, jadi **cocokkan dengan kurikulum yang dipakai pelajar** (lihat `LEARNER.md`).

### Target Kompetensi per Jalur

**Jalur A — Fenomena Sehari-hari**
- Menjelaskan fenomena (bayangan, pelangi, benda terapung, rem sepeda) dengan kata-kata sendiri memakai konsep gaya, energi, dan cahaya.
- Melakukan pengukuran sederhana dengan satuan yang benar dan mencatat data dalam tabel.
- Membuat prediksi sebelum eksperimen dan membandingkannya dengan hasil.

**Jalur B — Fisika SMA**
- Menggambar diagram benda bebas dan menerjemahkannya ke persamaan hukum Newton.
- Memilih prinsip yang tepat (gaya, energi, atau momentum) untuk sebuah soal dan menjelaskan alasannya.
- Membaca dan membuat grafik (posisi–waktu, kecepatan–waktu, arus–tegangan) serta memaknai kemiringan dan luasnya.
- Menulis laporan praktikum singkat lengkap dengan ketidakpastian pengukuran.

**Jalur C — Fisika Universitas Tahun 1–2**
- Menurunkan hubungan penting (persamaan gerak, teorema usaha–energi, periode osilator) dari hukum dasar dengan kalkulus.
- Memecahkan soal terbuka yang menuntut asumsi sendiri, lalu memeriksa hasil dengan analisis dimensi dan kasus ekstrem.
- Membuat simulasi numerik sederhana (mis. metode Euler di Python) dan membandingkannya dengan solusi analitik.

**Jalur D — Fisika untuk Rekayasa**
- Memodelkan sistem nyata (struktur, rangkaian, sistem termal, getaran) dengan asumsi yang dinyatakan eksplisit.
- Mengestimasi orde besaran dan batas keselamatan sebelum menghitung rinci.
- Menjelaskan *trade-off* desain dan mendokumentasikan keputusan dengan [template-decision-record.md](../../templates/template-decision-record.md).

---

## 3. Roadmap Ringkas

Rincian setiap fase (konsep inti, matematika prasyarat, eksperimen dan simulasi, kaitan rekayasa, tanda sudah menguasai) ada di **[roadmap.md](roadmap.md)**.

| Fase | Materi Pokok | Status |
|---|---|---|
| **0** | Pengukuran, satuan SI, ketidakpastian, analisis dimensi, estimasi | [ ] Belum |
| **1** | Kinematika (gerak lurus, gerak parabola, gerak melingkar) | [ ] Belum |
| **2** | Dinamika (hukum Newton, gesekan, diagram benda bebas) | [ ] Belum |
| **3** | Usaha, energi, dan momentum | [ ] Belum |
| **4** | Rotasi dan kesetimbangan benda tegar | [ ] Belum |
| **5** | Gravitasi | [ ] Belum |
| **6** | Osilasi dan gelombang (termasuk bunyi) | [ ] Belum |
| **7** | Fluida | [ ] Belum |
| **8** | Suhu, kalor, dan termodinamika | [ ] Belum |
| **9** | Listrik, magnet, dan rangkaian | [ ] Belum |
| **10** | Optik | [ ] Belum |
| **11** | Pengantar fisika modern | [ ] Belum |

---

## 4. Cara Belajar Bersama AI Mentor

- **`"mulai sesi belajar fisika [konsep]"`**: sesi 6 langkah, dimulai dari fenomena dan prediksi.
- **`"turunkan [rumus]"`**: menurunkan rumus dari prinsip dasar (mis. persamaan GLBB dari grafik kecepatan–waktu).
- **`"uji lisan [sistem]"`**: ujian papan tulis, mis. "rancang alat ukur percepatan gravitasi dengan bandul".
- **`"bantu lab [nama praktikum]"`**: pendamping eksperimen dan laporan praktikum (praktikum/laporan yang dinilai: maksimal L3 tanpa pengecualian, tanpa mengarang data; ujian atau kompetisi yang sedang berlangsung tidak dibantu, lihat [rules.md](rules.md#integritas-akademik-khusus-fisika)).
- **`"dampingi kuliah [judul/URL]"`**: mendampingi kuliah terbuka, mis. dari MIT OpenCourseWare.
- **`"catat log"`**: mencatat sesi ke [notes/learning-log.md](notes/learning-log.md); istilah baru dicatat di [notes/glossary.md](notes/glossary.md).

---

## 5. Sumber Rujukan Utama

* **Buku teks terbuka (gratis):** OpenStax — *Physics* (SMA), *College Physics 2e*, *University Physics* Volume 1–3: https://openstax.org/subjects/science
* **Buku teks klasik:** Halliday, Resnick & Walker, *Fundamentals of Physics*; Serway & Jewett, *Physics for Scientists and Engineers*; Paul G. Hewitt, *Conceptual Physics* (cocok untuk jalur A dan pembelajar tanpa latar matematika); Kleppner & Kolenkow, *An Introduction to Mechanics* (jalur C dan olimpiade).
* **Ketidakpastian pengukuran:** John R. Taylor, *An Introduction to Error Analysis*.
* **Kuliah terbuka:** MIT OpenCourseWare (mis. 8.01 *Classical Mechanics*, 8.02 *Electricity and Magnetism*, 8.03 *Vibrations and Waves*): https://ocw.mit.edu/
* **Bacaan mendalam:** *The Feynman Lectures on Physics* (versi daring gratis): https://www.feynmanlectures.caltech.edu/
* **Video dan latihan:** Khan Academy Physics: https://www.khanacademy.org/science/physics
* **Simulasi interaktif:** PhET Interactive Simulations (University of Colorado Boulder): https://phet.colorado.edu/
* **Tools:** kertas dan pensil, kalkulator, spreadsheet, Python (NumPy, Matplotlib), aplikasi sensor ponsel untuk eksperimen (pilih yang tepercaya), GeoGebra atau Desmos untuk grafik.

---

## 6. Project Showcase & Praktik (`projects/`)

*(Proyek besar dapat dikelola di repositori mandiri lalu ditautkan di sini. Eksperimen kecil, data, dan laporan praktikum disimpan di folder `projects/`.)*

| Nama Proyek / Karya | Jenis | Deskripsi Singkat | Alat / Media | Tautan | Status |
|---|---|---|---|---|---|
| *(Contoh: Mengukur g dengan Bandul)* | Eksperimen | *(Mengukur periode untuk beberapa panjang tali, menghitung g beserta ketidakpastiannya)* | *(Stopwatch ponsel, meteran, spreadsheet)* | `[Tautan](...)` | [ ] Rencana |
| *(Contoh: Simulasi Gerak Parabola dengan Hambatan Udara)* | Proyek | *(Metode Euler di Python, dibandingkan dengan solusi tanpa hambatan)* | *(Python, Matplotlib)* | `[Tautan](...)` | [ ] Rencana |
| *(Contoh: Kajian Efisiensi Kompor)* | Karya Ilmiah | *(Mengukur kalor yang diterima air untuk dua jenis panci)* | *(Termometer, laporan)* | `[Tautan](...)` | [ ] Rencana |
| *(Contoh: Persiapan OSN Fisika)* | Kompetisi | *(Catatan latihan dan refleksi soal)* | *(Buku, log)* | `[Tautan](...)` | [ ] Rencana |

Jenis karya: **Proyek** (simulasi, alat, kode), **Eksperimen** (praktikum dan laporan), **Karya Ilmiah** (penelitian kecil, lomba karya tulis), **Kompetisi** (olimpiade, lomba sains/robotik).

---

## 7. Struktur Folder Topik Ini

```text
physics/
├── README.md                                 # Dokumen ini: jalur, target, sumber
├── roadmap.md                                # Fase belajar berurutan berdasar prasyarat
├── rules.md                                  # Aturan AI Mentor Fisika (Bagian 1)
├── rules-misconceptions-and-experiments.md   # Miskonsepsi, eksperimen, soal, rubrik (Bagian 2)
├── notes/
│   ├── learning-log.md                       # Log sesi, kuis ulang, daftar parkir
│   └── glossary.md                           # Istilah teknis fisika
└── projects/                                 # Eksperimen, data, simulasi, laporan praktikum
```
