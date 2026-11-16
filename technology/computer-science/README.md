# Computer Science Fundamentals

Folder ini didedikasikan untuk mempelajari fondasi ilmu komputer tingkat rendah (*low-level systems*), mencakup arsitektur komputer, sistem operasi, jaringan komputer, struktur data & algoritma, basis data, bahasa & compiler, serta sistem terdistribusi.

---

## 1. Roadmap & Kurikulum

* 👉 **[Roadmap CS 9 Subjek](roadmap.md)**
  * Menggunakan kurikulum [TeachYourselfCS](https://teachyourselfcs.com/) yang dibagi ke dalam **Fase 0–9** secara berurutan sesuai prasyarat.
  * Menekankan pemahaman level rendah (*one layer below*) dengan bahasa C, Linux, serta alat observasi (`gdb`, `strace`, `valgrind`, `perf`, `tcpdump`, `EXPLAIN ANALYZE`).
  * Mendukung dua mode belajar: **Mode Kurikulum Penuh** (belajar bertahap mendalam) dan **Mode Fokus Proyek** (saat sedang membangun proyek nyata di `projects/`).

---

## 2. AI Tutor Pendamping
Panduan tutor AI personal dengan metode Socratic, *active recall*, teknik Feynman, dan Tangga Bantuan L1–L4 berada di:
* 👉 **[tutor/SKILL.md](tutor/SKILL.md)**

Gunakan di sesi chat dengan pemicu cepat seperti:
* `mulai sesi belajar [topik]`
* `bantu lab [nama lab/proyek]`
* `review kode ini`
* `kuis ulang`
* `uji saya tanpa bantuan [topik]`
* `ulasan mingguan`
* `tinjau parkir`

---

## 3. Project Showcase (*Multi-Repo*)
Proyek laboratorium dan implementasi *low-level* dikelola sebagai repositori GitHub mandiri (atau di dalam `projects/` lokal yang diabaikan `.gitignore` agar framework ini tetap ringan) dan ditautkan di sini:

| Nama Proyek / Lab | Deskripsi Singkat | Bahasa / Tools | Repositori | Status |
|---|---|---|---|---|
| *(Belum ada)* | — | — | — | — |

---

## 4. Struktur Direktori
```text
computer-science/
├── README.md        # Dokumen ikhtisar ini
├── roadmap.md       # Peta belajar 9 subjek CS & eksperimen level rendah
├── tutor/
│   └── SKILL.md     # System prompt AI Tutor CS
├── notes/           # learning-log.md, glossary.md, catatan konsep
└── projects/        # Proyek laboratorium mandiri (C, mini shell, socket server, kv-store, dll.)
```

Catatan belajar: [learning-log](notes/learning-log.md) · [glosarium](notes/glossary.md)
