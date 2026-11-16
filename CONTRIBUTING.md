# Panduan Kontribusi

Terima kasih ingin ikut memperbaiki *framework* ini. Kontribusi dari pelajar, guru, *engineer*, maupun pembelajar umum sama-sama berharga.

## Cara Berkontribusi

| Ingin... | Lakukan |
|---|---|
| Melaporkan perilaku mentor yang salah | Buka *issue* **Laporan Masalah**. Sertakan platform AI, perintah yang diketik, dan perilaku yang diharapkan. Hapus data pribadi dari contoh percakapan. |
| Mengusulkan topik atau *mentor pack* baru | Buka *issue* **Usulan Topik** dulu agar cakupannya disepakati sebelum menulis. |
| Melaporkan hasil uji di platform tertentu | Buka *issue* dengan template **Laporan Uji Platform** (lihat [docs/platform-compatibility.md](docs/platform-compatibility.md)). |
| Melaporkan perilaku mentor yang berbahaya (mis. instruksi eksperimen tidak aman, membantu kecurangan) | Buka *issue* **Laporan Masalah** dan beri judul diawali `[KESELAMATAN]`. Laporan ini diprioritaskan. |
| Memperbaiki salah ketik atau tautan | Langsung kirim *pull request*. |

## Alur Kerja (GitHub Flow)

1. *Fork* repositori, lalu buat *branch* dari `main`: `feat/...`, `fix/...`, atau `docs/...`.
2. Lakukan perubahan, lalu jalankan pemeriksa (membutuhkan Python 3.8 atau lebih baru, tanpa paket tambahan):
   ```bash
   python scripts/check_docs.py
   ```
3. Tambahkan catatan di bagian `[Unreleased]` pada [CHANGELOG.md](CHANGELOG.md).
4. Kirim *pull request* ke `main`. PR akan di-*squash merge* setelah ditinjau.

## Aturan Penulisan

- **Bahasa:** Bahasa Indonesia sebagai bahasa utama. Istilah teknis dan *engineering* (mis. *concurrency*, *deployment*, *state*) tetap dalam bahasa Inggris dan dijelaskan saat pertama muncul.
- **Netral persona:** Aturan mentor tidak boleh mengasumsikan latar belakang pelajar. Jika memakai contoh jembatan (mis. "di Java..."), tandai sebagai ilustrasi dan arahkan mentor menyesuaikannya dengan `LEARNER.md`.
- **Ukuran berkas:** Berkas aturan (`AGENTS.md`, `rules*.md`, `SKILL.md`) maksimal 24.000 byte. Pecah menjadi beberapa bagian yang saling menaut bila lebih besar.
- **Protokol Bersama:** Blok `PROTOKOL-BERSAMA` hanya dipakai di **tiga berkas mentor software** (CS Tutor, Go, React) dan harus identik di ketiganya. Ubah di satu tempat, salin persis ke dua berkas lainnya, dan naikkan nomor versinya. Paket topik STEM lain **tidak** memakai blok ini; mereka merujuk `AGENTS.md` dan `docs/stem-pedagogy.md`.
- **Integritas & keselamatan:** jangan menulis aturan yang lebih longgar daripada bagian *Integritas Akademik & Keselamatan* di `AGENTS.md`.
- **Struktur topik:** Ikuti bagian **Standarisasi Struktur Topik** di [AGENTS.md](AGENTS.md) dan gunakan [templates/template-topic-readme.md](templates/template-topic-readme.md).
- **Akurasi:** Rujuk sumber primer (dokumentasi resmi, buku, RFC). Jangan mencantumkan URL atau nomor bab yang belum diverifikasi.
- **Akhir baris:** LF, dengan baris kosong di akhir berkas (sudah diatur oleh `.editorconfig` dan `.gitattributes`).

## Menambah Paket Topik STEM

Paket topik yang paling dibutuhkan saat ini: **kimia**, **biologi**, dan cabang rekayasa selain software (**elektro**, **mesin**, **sipil**). Paket yang baik berisi:

1. `README.md` dengan jalur jenjang (sekolah → universitas → rekayasa), target, dan sumber rujukan terbuka.
2. `roadmap.md` berisi fase berurutan berdasarkan prasyarat, masing-masing dengan "tanda sudah menguasai".
3. Aturan mentor dari [templates/template-topic-rules.md](templates/template-topic-rules.md): `rules.md` (Bagian 1: peran, adaptasi jenjang, prinsip, integritas, keselamatan) dan, bila perlu, `rules-<isi>.md` (Bagian 2: miskonsepsi, soal terbuka, rubrik, referensi). Setiap berkas < 24.000 byte. Gunakan paket Matematika dan Fisika sebagai acuan.
4. `notes/learning-log.md`, `notes/glossary.md`, dan `projects/.gitkeep`.
5. Baris baru di tabel routing `AGENTS.md` dan tabel **Topik Saat Ini** di `README.md`.

**Tinjauan sebelum digabung:** paket topik baru sebaiknya ditinjau oleh minimal satu orang yang menguasai bidangnya (guru, dosen, atau praktisi). Sertakan di deskripsi PR siapa peninjaunya dan bagian mana yang sudah diperiksa. Untuk paket yang memuat eksperimen (kimia, biologi, elektro), lengkapi checklist keselamatan: bahan berbahaya, alat pelindung, pendampingan, dan instruksi yang harus ditolak mentor.
Sertakan aturan keselamatan untuk eksperimen yang berisiko, dan rujuk sumber yang dapat diakses gratis bila memungkinkan.

## Jangan Disertakan dalam PR

- `LEARNER.md` atau data pribadi apa pun.
- Isi `notes/` milik pribadi dan isi folder `projects/`.
- Kredensial, token, atau isi `.env`.

## Versi

Rilis mengikuti [Semantic Versioning](https://semver.org/):
- **MAJOR:** perubahan yang memaksa pengguna menyesuaikan profil, struktur topik, atau perintah.
- **MINOR:** topik, perintah, atau panduan baru yang kompatibel.
- **PATCH:** perbaikan isi, tautan, dan salah ketik.

Dengan berkontribusi, Anda setuju mematuhi [Kode Etik](CODE_OF_CONDUCT.md) dan merilis kontribusi Anda di bawah [lisensi MIT](LICENSE).
