# LEARNER.md — Contoh: Engineer Python yang Belajar Go (fiktif)

## 1. Identitas & Peran
* **Nama / Panggilan:** Bima
* **Peran Utama:** Engineer
* **Tingkat Pengalaman:** *Backend engineer* 3 tahun.

## 2. Latar Belakang untuk Jembatan Konsep
* **Bidang yang Sudah Dikuasai:** Python (Django, FastAPI), PostgreSQL, Docker.
* **Pengalaman Tambahan:** Sedikit JavaScript.
* **Hal yang Ingin Dibangun Ulang dari Dasar:** *Concurrency* dan cara kerja memori; selama ini mengandalkan `asyncio` tanpa paham bagian bawahnya.

## 3. Target Pembelajaran
1. **Target Utama:** Menulis layanan *backend* Go yang idiomatik.
2. **Target Pendukung:** Memahami OS dan jaringan di level *system call*.

## 3b. Profil STEM
* **Tingkat Matematika Saat Ini:** Kalkulus dan statistika dasar; aljabar linier sudah lupa.
* **Bahasa Target:** Bahasa Inggris tingkat lanjut (membaca dokumentasi dan paper).
* **Alat yang Tersedia:** Laptop, Python, Go, Docker, Linux.

## 4. Waktu & Ritme Belajar
* **Alokasi Waktu:** 6 jam per minggu.
* **Durasi Sesi Ideal:** 45 menit.

## 5. Preferensi Gaya Belajar & Bahasa
* **Bahasa Komunikasi:** Bahasa Indonesia, istilah teknis dalam bahasa Inggris.
* **Tingkat Kedalaman:** Mendalam sampai *trade-off*.
* **Gaya Penjelasan Favorit:** Contoh kode dan eksperimen langsung.
* **Metode yang Disukai:** *Socratic* dan eksperimen dengan alat observasi.
* **Mode Pembaruan Memori:** Otomatis *(di AI IDE)*.

## 8. Catatan Pengamatan Mentor (Diisi & Diperbarui oleh AI Mentor)
* **Analogi & Representasi yang Terbukti Efektif:** Perbandingan langsung antara `asyncio` event loop Python vs Go runtime scheduler (`GMP model`) serta pembuktian lewat `pprof` dan `strace`.
* **Pola Kesalahan yang Perlu Diwaspadai (`[KONSEP]` / `[MODEL]` / `[EKSEKUSI]`):** `[MODEL]` Kadang membawa pola *exception hierarchy* Python ke Go alih-alih menangani `error` sebagai nilai eksplisit; `[EKSEKUSI]` lupa menutup *cancel function* dari `context.WithTimeout`.
* **Kalibrasi Tingkat & Ketegasan Aktual:** Siap diberi pertanyaan tajam setara *senior code review* dan *whiteboard interview* tanpa perlu pengantar dasar pemrograman.
