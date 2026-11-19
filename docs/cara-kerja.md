# Cara Kerja L2SE

Halaman ini menjelaskan **masalah apa yang diselesaikan L2SE** dan **bagaimana alur pemakaiannya**, dari memasang sampai belajar jangka panjang.

![Infografis L2SE: masalah yang diselesaikan, cara menjawabnya, tiga langkah memulai, dan alur satu sesi belajar](img/l2se-infografis.svg)

---

## 1. Masalah yang Diselesaikan

| # | Masalah | Akibatnya | Cara L2SE menjawab | Fitur / perintah |
|---|---|---|---|---|
| 1 | AI biasa memberi **jawaban instan** | Pemahaman dangkal dan ketergantungan ("vibe learning") | Mentor bertanya dulu dan memberi bantuan bertahap; tugas bernilai tidak dikerjakan | **Tangga Bantuan L1–L4**, Integritas Akademik, `"uji saya tanpa bantuan"` |
| 2 | Penjelasan **tidak mengenal pelajar** | Terlalu sulit atau terlalu mudah; analogi tidak nyambung | Profil pelajar dibaca sebelum menjelaskan | `LEARNER.md`, `"atur profil saya"`, `"sesuaikan topik"` |
| 3 | Rumus **dihafal, bukan dipahami** | Tidak mampu memecahkan masalah yang belum pernah dilihat | Penurunan dari prinsip dasar, prediksi sebelum eksperimen, cek kewajaran, ujian papan tulis | **Protokol STEM**, `"turunkan"`, `"uji lisan"` |
| 4 | Ilmu **cepat lupa dan tercecer** | Progres tidak terlihat, tidak ada bukti kompetensi | Log belajar, pengulangan berjarak, glosarium, dan tabel karya | `"catat log"`, `"kuis ulang"`, `glossary.md`, *Project Showcase* |
| 5 | **Guru kewalahan** menyiapkan materi dan umpan balik | Waktu habis untuk administrasi, bukan mengajar | Mentor sebagai rekan perancang: rencana pembelajaran, soal bertingkat, rubrik | `"rancang materi ajar"`, `"buat bank soal"` |
| 6 | **Sumber terbaik dunia sulit diakses** | Buku, paper, dan kuliah terbuka berbahasa asing tanpa pendamping | Pendamping membaca dan menonton, glosarium istilah, topik bahasa sebagai gerbang STEM | `"dampingi kuliah"`, `"baca bersama"`, topik *English/Japanese for STEM* |

**Yang bukan tujuan L2SE:** menggantikan guru, memberi jawaban ujian, atau menjadi sumber informasi resmi (syarat beasiswa, jadwal ujian, kebijakan). Untuk informasi seperti itu, mentor mengarahkan ke sumber resmi.

---

## 2. Alur 1 — Dari Nol Sampai Siap Belajar

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 24, "rankSpacing": 30}}}%%
flowchart TD
    A([Mulai]) --> B{"Pakai alat apa?"}
    B -->|"Aplikasi chat: Claude, ChatGPT, Gemini"| C["Jalur A<br/>unduh ZIP, buat Project atau Gem<br/>tempel AGENTS.md<br/>unggah berkas pendukung"]
    B -->|"AI IDE atau agent: Claude Code, Cursor, dan sejenisnya"| D["Jalur B<br/>Use this template, clone repositori<br/>buka folder root di AI IDE"]
    B -->|"Developer yang ingin ikut pembaruan"| E["Jalur C<br/>clone, tambah remote upstream<br/>lihat docs/updating.md"]
    C --> F
    D --> F
    E --> F
    F["AI memuat AGENTS.md<br/>Claude Code lewat CLAUDE.md"] --> G{"LEARNER.md sudah ada?"}

    G -->|"Belum"| H["Mentor menyapa atau menyambut topik<br/>tawarkan 'atur profil saya' atau 3 konteks mini:<br/>peran & jenjang, hal yang dikuasai, target"]
    H --> I{"Pilih jalur profil"}
    I -->|"Wawancara lengkap ('atur profil saya')"| J["Wawancara lengkap satu per pesan<br/>semua pertanyaan boleh dilewati"]
    I -->|"3 konteks mini (~30 detik)"| M0["Klarifikasi maks 1 kali jika ambigu,<br/>susun draf awal LEARNER.md,<br/>lalu langsung masuk ke materi"]
    J --> K["Mentor menampilkan draf profil"]
    K --> L{"Draf sudah sesuai?"}
    L -->|"Perlu diubah"| J
    L -->|"Ya"| M["Simpan sebagai LEARNER.md<br/>Jalur A: unduh berkas dari chat<br/>atau simpan lewat Notepad, lalu unggah"]
    M0 --> O["Mentor membaca profil dan memperbarui<br/>Catatan Pengamatan Mentor secara proaktif"]

    G -->|"Sudah"| O
    M --> O
    O --> P

    P{"Topik yang ingin dipelajari?"}
    P -->|"Belum ada"| Q["'buat topik baru [nama]'<br/>README, notes/learning-log.md,<br/>notes/glossary.md, projects/"]
    P -->|"Ada, tetapi tidak sesuai jenjang"| R["'sesuaikan topik [nama]'<br/>usulan target dan silabus,<br/>diterapkan setelah Anda setuju"]
    P -->|"Ada dan sesuai"| S
    Q --> S
    R --> S
    S["Mentor membaca aturan topik<br/>contoh Fisika: rules.md dan roadmap.md"] --> T([Siap belajar: lanjut ke Alur 2])
```

---

## 3. Alur 2 — Satu Sesi Belajar

Pertama, ke mana sebuah permintaan diarahkan:

| Yang diketik pelajar | Yang terjadi |
|---|---|
| `mulai sesi belajar [topik]` | Sesi terstruktur (diagram di bawah) |
| `turunkan`, `uji lisan`, `dampingi kuliah`, `baca bersama`, `jelajah frontier` | Mode khusus sesuai [AGENTS.md](../AGENTS.md) bagian 8 |
| `catat log`, `kuis ulang` | Mentor menulis atau membaca `notes/learning-log.md` (lihat Alur 4) |
| `ulasan mingguan`, `tinjau parkir`, `uji saya tanpa bantuan` | Evaluasi berkala dan naik fase (lihat Alur 5) |
| Buntu atau meminta jawaban soal atau tugas | Keputusan bantuan (lihat Alur 3) |
| Bertanya syarat beasiswa, jadwal, biaya, atau kebijakan | Tidak dijawab dari ingatan; diarahkan ke sumber resmi topik |

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 24, "rankSpacing": 30}}}%%
flowchart TD
    A(["mulai sesi belajar [topik]"]) --> B["Tahap 1: Pemanasan<br/>2-3 pertanyaan prasyarat,<br/>satu per pesan"]
    B --> C["Tahap 2: Penjelasan inti<br/>analogi dan contoh,<br/>prinsip dasar sebelum rumus"]
    C --> D["Tahap 3: Cek paham<br/>pelajar menjelaskan ulang<br/>dengan kata sendiri"]
    D --> E{"Pemahaman cukup?"}
    E -->|"Belum"| F["Mentor bertanya kenapa,<br/>menghadirkan konflik kognitif,<br/>menjelaskan dengan cara lain"]
    F --> D
    E -->|"Ya"| G["Tahap 4: Kuis 3 soal<br/>satu per satu: konsep,<br/>prediksi, skenario"]
    G --> H["Tahap 5: Tugas penerapan kecil"]
    H -.->|"Pelajar buntu atau meminta jawaban"| H2[["Keputusan bantuan: lihat Alur 3"]]
    H --> I{"Melibatkan eksperimen?"}
    I -->|"Ya"| J["Sebut risiko dan alat pelindung,<br/>pendampingan untuk pelajar sekolah,<br/>tolak instruksi berbahaya"]
    I -->|"Tidak"| K
    J --> K["Tahap 6: Penutup<br/>ringkasan, miskonsepsi, sumber,<br/>tawaran catat log"]
    K --> L(["Lanjut ke Alur 4"])
```

---

## 4. Alur 3 — Keputusan Bantuan

### 3a. Batas bantuan menurut jenis soal

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 24, "rankSpacing": 30}}}%%
flowchart TD
    A(["Pelajar buntu atau meminta bantuan<br/>pada soal atau tugas"]) --> B{"Jelas jenis soalnya?"}
    B -->|"Tidak"| B1["Mentor bertanya dulu<br/>bila ragu, pakai aturan<br/>yang lebih ketat"]
    B1 --> B
    B -->|"Ya"| C{"Ujian atau kuis<br/>berlangsung?"}
    C -->|"Ya"| C1["Ditolak dengan sopan<br/>tawarkan belajar<br/>sesudahnya"]
    C -->|"Tidak"| D{"Kompetisi<br/>berlangsung?"}
    D -->|"Ya"| D1["Tidak dibantu<br/>sama sekali"]
    D -->|"Tidak"| E{"Tugas bernilai?<br/>PR, kuis dinilai,<br/>praktikum, skripsi"}
    E -->|"Ya"| E1["Maksimal L3<br/>mentor boleh memeriksa<br/>jawaban pelajar"]
    E -->|"Tidak"| T(["Masuk Tangga Bantuan: 3b"])
    E1 --> T
```

### 3b. Tangga Bantuan L1–L4

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 24, "rankSpacing": 30}}}%%
flowchart TD
    A(["Bantuan diizinkan dari 3a"]) --> L1["L1 Pertanyaan penuntun"]
    L1 --> H1{"Cukup?"}
    H1 -->|"Ya"| OK(["Pelajar lanjut sendiri"])
    H1 -->|"Belum"| L2["L2 Hint<br/>arah, dokumentasi,<br/>pseudocode"]
    L2 --> H2{"Cukup?"}
    H2 -->|"Ya"| OK
    H2 -->|"Belum"| L3["L3 Contoh terpisah<br/>soal atau data berbeda"]
    L3 --> H3{"Cukup?"}
    H3 -->|"Ya"| OK
    H3 -->|"Belum"| Q4{"Tugas bernilai?"}
    Q4 -->|"Ya"| M1["Tetap L3<br/>pecah jadi langkah kecil,<br/>pelajar mencoba lagi"]
    M1 --> L1
    Q4 -->|"Tidak"| Q5{"Sudah mencoba<br/>dan meminta L4?"}
    Q5 -->|"Belum"| M2["Minta pelajar menempel<br/>upaya atau menjelaskan<br/>buntunya"]
    M2 --> L2
    Q5 -->|"Ya"| L4["L4 Draf solusi<br/>dijelaskan per bagian,<br/>lalu satu pertanyaan cek"]
```

---

## 5. Alur 4 — Rekam dan Ulang

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 24, "rankSpacing": 30}}}%%
flowchart TD
    A(["Sesi selesai atau subtopik tuntas"]) --> B["Mentor secara proaktif menyusun log<br/>atau pelajar mengetik 'catat log'"]
    B --> C["Draf entri log + Catatan Pengamatan Mentor"]
    C --> D{"Platform bisa menulis<br/>ke folder lokal?"}
    D -->|"Ya, AI IDE"| E["Simpan ke notes/learning-log.md,<br/>glossary.md, dan LEARNER.md<br/>(plus backup .l2se-backup/ dengan notifikasi)"]
    D -->|"Aplikasi chat web"| F["Mentor membuatkan berkas siap unduh<br/>atau blok siap salin untuk diunggah ulang"]
    E --> G
    F --> G
    G["Jadwal ulang:<br/>hari ke-1, 3, 7, 14, 30"] --> H["Saat jatuh tempo: 'kuis ulang'<br/>uji konsep tanpa hint"]
    H --> I{"Konsep dikuasai?"}
    I -->|"Ya"| J["Jadwal diperpanjang<br/>ke interval berikutnya"]
    I -->|"Belum"| K["Celah dicatat,<br/>kembali ke sesi belajar<br/>lihat Alur 2"]
    J --> L(["Lanjut belajar;<br/>evaluasi berkala di Alur 5"])
```

---

## 6. Alur 5 — Evaluasi Berkala, Naik Fase, dan Karya Nyata

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 24, "rankSpacing": 30}}}%%
flowchart TD
    A(["Belajar berlanjut<br/>beberapa sesi"]) --> B["Akhir minggu: 'ulasan mingguan'<br/>rangkum materi, kesalahan berulang,<br/>tiga prioritas berikutnya"]
    B --> C{"Ada topik<br/>yang diparkir?"}
    C -->|"Ya"| D["'tinjau parkir'<br/>kelompokkan per fase,<br/>usulkan urutan belajar"]
    C -->|"Tidak"| E
    D --> E["Akhir fase roadmap:<br/>'uji saya tanpa bantuan' atau 'uji lisan'<br/>skor 0 sampai 5 dan analisis celah"]
    E --> F{"Skor cukup?"}
    F -->|"Belum"| G["Perkuat materi yang lemah<br/>lihat Alur 2"]
    F -->|"Ya"| H["Naik ke fase berikutnya<br/>di roadmap"]
    H --> I{"Ingin membangun<br/>karya nyata?"}
    I -->|"Tidak"| J(["Lanjut belajar: Alur 2"])
    I -->|"Ya"| K["Kerjakan di topik/projects/nama-proyek/<br/>mentor mendampingi lewat<br/>'bantu lab' dan 'review kode ini'"]
    K --> L{"Ukuran karya?"}
    L -->|"Proyek besar"| M["Buat repositori Git sendiri<br/>folder projects/ diabaikan Git<br/>repositori belajar<br/>tautkan di Project Showcase"]
    L -->|"Mini-lab kecil"| N["Simpan dengan git add -f path<br/>bila ingin ikut disimpan<br/>di repositori belajar"]
```

---

## 7. Alur 6 — Memperbarui Framework

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 24, "rankSpacing": 30}}}%%
flowchart TD
    A(["Versi baru L2SE dirilis"]) --> B["Baca CHANGELOG.md<br/>untuk melihat apa yang berubah"]
    B --> C{"Cara memasang?"}
    C -->|"Repositori dengan Git"| D["git fetch upstream<br/>lalu git merge upstream/main"]
    C -->|"Unduh ZIP"| E["Salin hanya berkas<br/>Zona Framework"]
    D --> F["LEARNER.md dan isi notes/ tidak disentuh<br/>konflik di README topik yang sudah<br/>disesuaikan itu wajar"]
    E --> F
```

---

## 8. Cara Membaca Diagram

- **Belah ketupat** (`{ }`) adalah pertanyaan atau keputusan, dan **kotak** adalah tindakan mentor atau pelajar.
- Teks dalam tanda kutip tunggal, seperti `'atur profil saya'`, adalah perintah yang diketik pelajar.
- Diagram menggambarkan **perilaku yang diharapkan**. Hasil nyata dapat berbeda antar platform AI; lihat [platform-compatibility.md](platform-compatibility.md).
- Aturan lengkapnya ada di [AGENTS.md](../AGENTS.md) (khususnya bagian 4 Integritas Akademik & Keselamatan dan bagian 8 Perintah Pemicu) dan [stem-pedagogy.md](stem-pedagogy.md).

Panduan langkah demi langkah ada di [getting-started.md](getting-started.md).
