# Changelog

Semua perubahan penting pada *framework* ini dicatat di berkas ini.

Format mengikuti [Keep a Changelog](https://keepachangelog.com/id-ID/1.1.0/), dan versi mengikuti [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Diubah
- Onboarding di `AGENTS.md`, `docs/cara-kerja.md`, `docs/getting-started.md`, dan `docs/platform-compatibility.md`: menerapkan **Profil Mini Wajib (3 konteks)** sebelum masuk ke materi serta *progressive profiling*, beserta aturan penanganan input ambigu (maksimal 1 klarifikasi konkret).
- Penguatan *tone* mentor di `AGENTS.md`, `mathematics/foundations/rules.md`, dan `science/physics/rules.md`: **hangat tetapi tegas** (*anti-sycophancy*, tidak meloloskan jawaban setengah benar, menahan desakan jawaban instan).
- Sinkronisasi `PROTOKOL-BERSAMA` **v6** di tiga berkas mentor *software*.

## [0.1.0] - 2026-11-18

Rilis beta pertama dengan nama **L2SE — Learner to Systems Engineer**.

### Ditambahkan
- `AGENTS.md` sebagai sumber aturan AI Mentor lintas platform: Tangga Bantuan L1–L4, adaptasi per peran (pelajar, mahasiswa, *engineer*, guru/dosen, pembelajar umum), integritas akademik, serta Zona Framework vs Zona Pengguna.
- Onboarding lewat `"atur profil saya"` dan template profil `templates/template-learner.md`.
- Perintah baru: `"perbarui profil"`, `"sesuaikan topik [nama]"`, `"rancang materi ajar [topik]"`, dan `"buat bank soal [topik]"`.
- `notes/learning-log.md` di semua topik, dan `notes/glossary.md` di topik STEM beserta `templates/template-glossary.md`.
- **Protokol STEM** (`docs/stem-pedagogy.md`): pemetaan kerangka teoretis **TPACK** (Mishra & Koehler, 2006), prinsip dasar sebelum rumus, kerangka Pólya, cek kewajaran, prediksi–amati–jelaskan, banyak representasi, proses desain rekayasa, soal terbuka berbasis rubrik, serta penanganan miskonsepsi dan klasifikasi kesalahan (`[KONSEP]`, `[MODEL]`, `[EKSEKUSI]`).
- Perintah STEM: `"turunkan [rumus]"`, `"uji lisan [topik]"`, `"dampingi kuliah [judul/URL]"`, `"baca bersama [teks]"`, dan `"jelajah frontier [bidang]"`.
- **Paket mentor Matematika** (`mathematics/foundations/`): jalur SD/SMP → SMA → universitas → rekayasa/CS, roadmap 11 fase, aturan mentor, serta ±35 miskonsepsi, soal terbuka, dan rubrik.
- **Paket mentor Fisika** (`science/physics/`): jalur fenomena → SMA → universitas → rekayasa, roadmap 12 fase, aturan mentor dengan keselamatan eksperimen, katalog eksperimen rumahan dan simulasi PhET, miskonsepsi, soal terbuka, dan rubrik.
- **Integritas Akademik & Keselamatan** kanonik di `AGENTS.md` (tidak dapat dikalahkan aturan lain): tugas bernilai maks L3, ujian dan kompetisi yang sedang berlangsung tidak dibantu, lab/praktikum dinilai maks L3, serta urutan prioritas sumber kebenaran.
- `templates/template-topic-rules.md`, template issue **Laporan Uji Platform**, `CITATION.cff`, badge, dan bagian *Rencana Berikutnya* di README.
- Panduan Jalur A: daftar unggahan per topik, cara menyimpan `LEARNER.md` tanpa koding, catatan batas usia platform, dan contoh sesi untuk guru (Modul Ajar).
- `scripts/check_docs.py` kini memeriksa *anchor*, tautan gaya referensi, dan tautan yang keluar dari repositori; CI hanya berjalan di repositori utama.
- **`docs/cara-kerja.md`**: tabel masalah dan solusi, serta tujuh diagram *flowchart* (Mermaid) dalam enam alur: dari pemasangan sampai siap belajar, satu sesi belajar, keputusan bantuan (batas integritas dan Tangga Bantuan L1–L4), rekam dan kuis ulang, evaluasi berkala dan karya nyata, serta pembaruan framework. Semua diagram sudah dirender dan diperiksa. **`docs/img/l2se-infografis.svg`** sebagai ringkasan visual yang juga ditampilkan di README.
- **Topik `languages/japanese`** (*Japanese for STEM*): rujukan ke situs resmi Kedutaan Besar Jepang untuk informasi beasiswa MEXT (S1, Kosen, Senshu Gakko) tanpa menyalin syaratnya, jalur kana → kanji → STEM → ujian, roadmap 6 fase, pedoman mentor, dan glosarium istilah STEM Jepang–Indonesia–Inggris.
- Dokumentasi `docs/`: panduan memulai (tiga jalur), kompatibilitas platform beserta status pengujian, cara memperbarui, FAQ, dan contoh profil serta sesi.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, *issue/PR template*, CI pemeriksa dokumen (`scripts/check_docs.py`), `.gitattributes`, dan `.editorconfig`.

### Diubah
- Protokol Bersama v5 (sudut pandang "pelajar", peran UI/UX, batas integritas di Tangga Bantuan). Sebelumnya v4: aturan mentor Go, React, dan CS kini netral persona dan merujuk mentor STEM lain; jembatan konsep mengikuti `LEARNER.md` dan tidak lagi mengasumsikan latar Java/Next.js.
- Bahasa komunikasi mengikuti `LEARNER.md`, dengan Bahasa Indonesia sebagai *default*.
- **Fokus STEM → Engineer:** identitas, visi, dan misi diarahkan ke STEM untuk semua kalangan; kategori disusun ulang menjadi `mathematics/`, `science/`, `technology/`, `engineering/`, dan `languages/`.
- `languages/english` diarahkan ulang menjadi *English for STEM* (bahasa sebagai gerbang pendidikan STEM dunia).
- `template-learner.md` mendapat bagian Profil STEM (jenjang matematika, bidang minat, bahasa target, alat) serta target ujian/kompetisi/beasiswa.
- *Project Showcase* mencakup eksperimen, karya ilmiah, dan kompetisi.

### Dihapus
- Profil pribadi `LEARNER.md` dari repositori *framework*.
- Topik `general/finance` dari paket bawaan (di luar fokus STEM; pengguna tetap dapat membuat topik non-STEM sendiri).
