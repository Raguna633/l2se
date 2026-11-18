# Panduan Memulai

Panduan ini membantu Anda mulai belajar STEM bersama AI Mentor, apa pun latar belakang Anda. Pilih **jalur** sesuai alat yang Anda punya, lalu baca **tips per peran** di bagian bawah. Ingin melihat gambaran besar dulu? Lihat [cara-kerja.md](cara-kerja.md) (infografis dan *flowchart*).

---

## Jalur A — Tanpa Koding (lewat aplikasi chat)

Cocok untuk guru, pelajar, dan pembelajar umum yang tidak memakai Git atau AI IDE.

**Yang dibutuhkan:** akun Claude, ChatGPT, atau Gemini yang mendukung fitur *Projects* / *Gems* (fitur ini bisa berbeda antar paket langganan; periksa di aplikasi Anda).

> **Batas usia:** setiap platform AI punya batas usia minimum dan aturan izin orang tua di syarat layanannya. Pelajar sekolah sebaiknya memeriksanya dan belajar dengan pendampingan orang tua atau guru bila diperlukan.

1. **Unduh framework.** Di halaman GitHub repositori ini, klik **Code → Download ZIP**, lalu ekstrak (klik kanan → *Extract All* di Windows).
2. **Buat ruang belajar** dan tempel seluruh isi `AGENTS.md` sebagai instruksi:
   - **Claude:** *Project* baru → bagian *instructions*.
   - **ChatGPT:** *Project* baru → *instructions*.
   - **Gemini:** *Gem* baru → instruksi Gem.

   Bila kolom instruksi terlalu pendek untuk seluruh `AGENTS.md`, unggah `AGENTS.md` sebagai berkas, lalu isi kolom instruksi dengan: *"Ikuti berkas AGENTS.md yang terunggah sebagai aturan utama mentor. Baca juga docs/stem-pedagogy.md dan LEARNER.md bila ada."*
3. **Unggah berkas pendukung** ke bagian *knowledge / files* sesuai [tabel di bawah](#daftar-berkas-yang-diunggah-per-topik).
4. **Buat profil.** Ketik `"atur profil saya"` (atau langsung ketik topik yang ingin dipelajari—mentor akan menanyakan **3 konteks mini** sekitar 30 detik terlebih dahulu). Setelah profil disusun:
   - **Unduh berkas langsung (paling mudah):** di Claude (*Artifacts*) atau ChatGPT, mentor akan membuatkan berkas `LEARNER.md` yang bisa langsung Anda klik **Download**.
   - **Cadangan manual (Komputer Windows):** bila tombol unduh berkas tidak muncul, buka Notepad → tempel draf → *File → Save As* → pada *Save as type* pilih **All Files (\*.\*)** → beri nama `LEARNER.md` (agar tidak menjadi `LEARNER.md.txt`).
   - **Ponsel:** bila tidak bisa mengunggah berkas, tempel draf profil di kolom instruksi, di bawah instruksi utama.

   Unggah `LEARNER.md` ke bagian *files / knowledge* ruang belajar yang sama.
5. **Belajar.** Ketik `"mulai sesi belajar [topik]"`.

**Catatan pembaruan berkas di jalur ini:** aplikasi chat web tidak bisa langsung menimpa berkas di dalam folder komputer Anda. Setiap selesai sesi (atau saat Anda mengetik `"catat log"`), mentor akan memberikan berkas `learning-log.md` siap unduh (atau blok teks siap salin) untuk Anda unggah ulang ke ruang belajar agar fitur `"kuis ulang"` tetap akurat.

### Daftar Berkas yang Diunggah per Topik

**Selalu unggah:** `docs/stem-pedagogy.md`, `templates/template-learner.md`, dan `LEARNER.md` (setelah dibuat).

| Ingin belajar | Unggah juga |
|---|---|
| Matematika | `mathematics/foundations/` → `README.md`, `roadmap.md`, `rules.md`, `rules-misconceptions-and-assessment.md` |
| Fisika | `science/physics/` → `README.md`, `roadmap.md`, `rules.md`, `rules-misconceptions-and-experiments.md` |
| Computer Science | `technology/computer-science/` → `README.md`, `roadmap.md`, `tutor/SKILL.md` |
| Backend Go | `engineering/software/go/` → `README.md`, `rules.md`, `rules-concepts-and-antipatterns.md` |
| Frontend React | `engineering/software/react/` → `README.md`, `rules.md`, `rules-patterns-and-architecture.md` |
| UI/UX Mobile | `engineering/software/ui-ux-mobile/` → `README.md`, `rules.md` |
| Bahasa Inggris / Jepang | `languages/english/` atau `languages/japanese/` → `README.md`, `roadmap.md`, `notes/glossary.md` |
| Guru yang merancang materi ajar | Cukup berkas "selalu unggah" di atas. Topik khusus tidak wajib. |
| Topik yang belum tersedia (mis. kimia, biologi) | Cukup berkas "selalu unggah", lalu ketik `"buat topik baru [nama]"`. |

Untuk fitur `"kuis ulang"`, unggah juga `notes/learning-log.md` topik tersebut.

---

## Jalur B — AI IDE / Agent

Cocok untuk mahasiswa dan *engineer* yang memakai Claude Code, Cursor, GitHub Copilot, OpenAI Codex, Windsurf, Antigravity, atau Gemini CLI.

1. Di GitHub, klik **Use this template → Create a new repository**. Pilih publik (sebagai portofolio) atau privat.
2. *Clone* repositori baru Anda, lalu buka **folder root**-nya di AI IDE. Membuka dari *root* memastikan mentor dapat membaca `AGENTS.md`, `templates/`, dan semua topik.
3. Ketik `"atur profil saya"` (atau langsung tanyakan topik—mentor akan menanyakan **3 konteks mini** dulu sebelum masuk ke materi). Mentor akan menyusun draf dan membuat `LEARNER.md` setelah Anda setujui, lalu melengkapinya bertahap selama sesi.
4. Ketik `"mulai sesi belajar [topik]"` atau `"buat topik baru [nama topik]"`.

Cara tiap platform memuat aturan berbeda-beda. Periksa [platform-compatibility.md](platform-compatibility.md), terutama bila memakai Gemini CLI atau GitHub Copilot.

**Proyek nyata dan portofolio:** buat atau *clone* proyek di `<topik>/projects/<nama-proyek>/`. Folder ini **diabaikan Git** repositori belajar Anda, sehingga isinya tidak ikut ter-*push*. Agar karya tampil sebagai portofolio:
1. Jadikan proyek besar repositori GitHub tersendiri, lalu tautkan di tabel *Project Showcase* pada `README.md` topik.
2. Untuk eksperimen kecil yang ingin ikut disimpan di repositori belajar, tambahkan secara eksplisit dengan `git add -f <path>`.

---

## Jalur C — Developer yang Ingin Mengikuti Pembaruan

Gunakan jalur ini jika Anda ingin menarik perbaikan *framework* di masa depan dengan riwayat Git yang tersambung. Langkah lengkapnya ada di [updating.md](updating.md).

---

## Tips per Peran

| Peran | Mulai dari | Perintah yang paling berguna |
|---|---|---|
| **Pelajar sekolah** | Isi jenjang kelas, mata pelajaran, dan target (ujian, UTBK, olimpiade) di profil. Mentor akan memakai bahasa sederhana dan eksperimen sehari-hari. | `"mulai sesi belajar [bab]"`, `"turunkan [rumus]"`, `"kuis ulang"` |
| **Mahasiswa** | Sebutkan mata kuliah, buku teks rujukan, dan kuliah terbuka yang diikuti. | `"dampingi kuliah [judul/URL]"`, `"uji lisan [topik]"`, `"bantu lab [nama lab]"` |
| **Engineer** | Isi *stack* dan tingkat matematika Anda agar mentor menjembatani dari sana. | `"review kode ini"`, `"uji lisan [sistem]"`, `"baca bersama [paper]"` |
| **Guru / Dosen** | Isi mata pelajaran, jenjang peserta didik, dan alat peraga yang tersedia. | `"rancang materi ajar [topik]"`, `"buat bank soal [topik]"`, `"jelajah frontier [bidang]"` |
| **Pembelajar umum** | Isi bidang yang Anda kuasai (mis. memasak, perbengkelan, olahraga) agar sains di baliknya terasa dekat. | `"mulai sesi belajar [topik]"`, `"jelajah frontier [bidang]"` |

> **Tentang integritas akademik:** untuk PR, kuis bernilai, ujian, atau skripsi, mentor tidak akan menuliskan jawaban akhirnya. Mentor membantu Anda memahami konsep dengan contoh soal yang berbeda, lalu meminta Anda mengerjakan sendiri.

Contoh profil untuk berbagai peran ada di [examples/](examples/).
