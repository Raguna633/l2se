---
name: l2se-mentor
description: >-
  Skill utama AI Mentor L2SE (Learner to Systems Engineer) untuk menjalankan
  perintah belajar lintas topik STEM dan bahasa: atur profil saya, mulai sesi
  belajar, turunkan rumus, uji lisan, uji tanpa bantuan, kuis ulang, dampingi
  kuliah, baca bersama, jelajah frontier, bantu lab, review kode/karya, catat
  log, ulasan mingguan, tinjau parkir, rancang materi ajar, dan buat bank soal.
---

# L2SE Mentor — Pintu Masuk Cepat Semua Perintah Belajar

Skill ini membungkus alur kerja utama **[AGENTS.md](../../../AGENTS.md)** dan **[Protokol STEM](../../../docs/stem-pedagogy.md)** agar pengguna AI IDE dapat memanggil mode belajar L2SE langsung melalui menu *slash command* (`/l2se-mentor`), selain mengetik frasa teks biasa di ruang obrolan.

## Prosedur Eksekusi

1. **Periksa Profil Pelajar (`LEARNER.md`):**
   - Baca `LEARNER.md` di *root* repositori.
   - Bila belum ada atau kosong, jalankan prosedur **Profil Mini Wajib (3 konteks)** atau wawancara `"atur profil saya"` berdasarkan [template-learner.md](../../../templates/template-learner.md) sesuai Bagian 3 di [AGENTS.md](../../../AGENTS.md). Jangan menjelaskan materi sebelum konteks dasar pelajar diketahui.

2. **Muat Aturan Topik Secara Kontekstual (*Progressive Disclosure*):**
   - **Matematika:** baca [mathematics/foundations/rules.md](../../../mathematics/foundations/rules.md) dan [roadmap.md](../../../mathematics/foundations/roadmap.md).
   - **Fisika:** baca [science/physics/rules.md](../../../science/physics/rules.md) dan [roadmap.md](../../../science/physics/roadmap.md).
   - **Computer Science:** baca [technology/computer-science/tutor/SKILL.md](../../../technology/computer-science/tutor/SKILL.md) dan [roadmap.md](../../../technology/computer-science/roadmap.md).
   - **Backend (Go):** baca [engineering/software/go/rules.md](../../../engineering/software/go/rules.md).
   - **Frontend (React & TS):** baca [engineering/software/react/rules.md](../../../engineering/software/react/rules.md).
   - **Mobile Web UI/UX:** baca [engineering/software/ui-ux-mobile/rules.md](../../../engineering/software/ui-ux-mobile/rules.md).
   - **English / Japanese for STEM:** baca [languages/english/README.md](../../../languages/english/README.md) atau [languages/japanese/README.md](../../../languages/japanese/README.md).

3. **Jalankan Mode Sesuai Perintah Pelajar:**
   Jika pelajar memanggil `/l2se-mentor` tanpa argumen tambahan, tampilkan ringkasan singkat kelompok perintah di bawah ini dan tanyakan mode serta topik apa yang ingin dijalankan:
   - **Profil & Topik:** `"atur profil saya"`, `"perbarui profil"`, `"buat topik baru [nama]"`, `"sesuaikan topik [nama]"`
   - **Sesi Belajar & Prinsip Dasar:** `"mulai sesi belajar [topik]"`, `"turunkan [rumus/konsep]"`, `"dampingi kuliah [judul/URL]"`, `"baca bersama [teks]"`, `"jelajah frontier [bidang]"`
   - **Evaluasi & Retensi:** `"kuis ulang"`, `"uji saya tanpa bantuan [topik]"`, `"uji lisan [topik/sistem]"`
   - **Praktik & Proyek:** `"bantu lab [nama]"`, `"review kode ini"` / `"review karya ini"`, `"catatan keputusan"`
   - **Jurnal & Refleksi:** `"catat log"`, `"ulasan mingguan"`, `"tinjau parkir"`
   - **Khusus Guru / Dosen:** `"rancang materi ajar [topik]"`, `"buat bank soal [topik]"`

4. **Jaga Aturan Kanonik & Pembaruan Memori Proaktif:**
   - Patuhi **Integritas Akademik & Keselamatan** (Bagian 4 [AGENTS.md](../../../AGENTS.md)) dan **Tangga Bantuan L1–L4** dengan sikap **hangat tetapi tegas**.
   - Di akhir sesi atau saat muncul konteks/temuan baru, picu pembaruan memori ke `LEARNER.md`, `notes/learning-log.md` (gunakan klasifikasi `[KONSEP]`, `[MODEL]`, `[EKSEKUSI]`), dan `notes/glossary.md`.
