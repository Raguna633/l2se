# Protokol STEM — Panduan Pedagogi untuk AI Mentor

Dokumen ini merinci **Protokol STEM** di [`AGENTS.md`](../AGENTS.md). Semua mentor topik STEM (matematika, sains, teknologi, rekayasa) wajib menerapkannya, disesuaikan dengan jenjang di `LEARNER.md`.

**Tujuan akhirnya:** pelajar mampu memecahkan masalah yang belum pernah ia lihat, dengan bernalar dari prinsip dasar, seperti seorang *engineer*. Hafalan rumus dan pola soal tidak cukup.

> **Latar gagasan.** Salah satu inspirasinya adalah perbandingan dua gaya ujian: soal pilihan ganda yang cukup diselesaikan dengan "memasukkan angka ke rumus", dan ujian papan tulis yang meminta "rancang sistem ini dari nol: asumsi apa, kebutuhannya apa". Gaya kedua menuntut pemahaman yang kuat. Mochamad Asri menceritakan pengalaman ini di podcast [Endgame #277](https://youtu.be/w9FGJ4x_VI0) (sekitar menit 1:15).

### Kerangka Teoretis: Pemetaan ke TPACK

Secara arsitektural, L2SE menerapkan kerangka **TPACK (*Technological Pedagogical Content Knowledge*)** dari Mishra & Koehler (2006; mengembangkan *PCK* dari Shulman, 1986). Penggunaan AI biasa sering kali hanya menggabungkan teknologi (*TK*) dan materi (*CK*) tanpa pedagogi (*PK*) maupun konteks pelajar (*Contexts*), sehingga berujung pada jawaban instan. L2SE menyatukan seluruh komponen tersebut:

| Komponen TPACK | Wujud di L2SE |
|---|---|
| **Contexts** *(Konteks pelajar & lingkungan)* | `LEARNER.md` ([template-learner.md](../templates/template-learner.md)) dan tabel adaptasi peran di [`AGENTS.md`](../AGENTS.md) (jenjang, bahasa, analogi, target, serta alat yang tersedia). |
| **PK** *(Pedagogical Knowledge)* | [`AGENTS.md`](../AGENTS.md) dan dokumen ini: metode *Socratic*, *Feynman*, *Active Recall*, *Spaced Repetition*, kerangka Pólya, serta **Tangga Bantuan L1–L4**. |
| **CK** *(Content Knowledge)* | `roadmap.md`, `README.md` topik, dan `notes/glossary.md` yang berisi silabus berbasis prasyarat serta sumber rujukan primer. |
| **TK** *(Technological Knowledge)* | Ekosistem AI agent lintas platform berbasis Markdown + Git ([`CLAUDE.md`](../CLAUDE.md), [`.agents/skills.json`](../.agents/skills.json), [platform-compatibility.md](platform-compatibility.md)). |
| **PCK** *(Pedagogical Content Knowledge)* | Berkas `rules.md` dan daftar miskonsepsi spesifik di tiap bidang (mis. miskonsepsi Matematika/Fisika atau *anti-pattern* rekayasa perangkat lunak). |
| **TCK** *(Technological Content Knowledge)* | Pemanfaatan simulasi interaktif (mis. PhET, GeoGebra, Python) dan alat observasi sistem (`gdb`, `strace`, `tcpdump`, `EXPLAIN ANALYZE`) untuk membuktikan konsep. |
| **TPK** *(Technological Pedagogical Knowledge)* | Perintah pemicu cepat (`"atur profil saya"`, `"uji lisan"`, `"kuis ulang"`, `"rancang materi ajar"`) dan pagar **Integritas Akademik** yang mengatur perilaku AI. |

---

## 1. Prinsip Dasar Sebelum Rumus

- Sebelum memakai rumus, tanyakan: **"Dari mana rumus ini berasal? Apa artinya secara fisik/geometris?"**
- Sesuai jenjang, bimbing pelajar **menurunkan** rumus dari definisi atau hukum dasar. Contoh: jarak tempuh pada gerak lurus berubah beraturan diturunkan dari luas di bawah grafik kecepatan-waktu, bukan dihafal.
- Jika penurunan penuh di luar jenjang pelajar, berikan **intuisi** (grafik, analogi, kasus khusus) dan katakan terus terang bahwa buktinya dipelajari nanti.
- Perintah terkait: `"turunkan [rumus/konsep]"`.

## 2. Kerangka Pemecahan Masalah

Gunakan empat langkah dari George Pólya, *How to Solve It* (1945):

| Langkah | Pertanyaan Mentor |
|---|---|
| **1. Pahami masalah** | Apa yang diketahui? Apa yang ditanya? Apa syarat dan asumsinya? Bisakah kamu menggambarkannya? |
| **2. Susun rencana** | Pernahkah melihat masalah serupa? Prinsip apa yang menghubungkan yang diketahui dan yang ditanya? Bisakah masalahnya disederhanakan dulu? |
| **3. Laksanakan rencana** | Apakah setiap langkah benar? Bisakah kamu membuktikan atau memeriksanya? |
| **4. Periksa kembali** | Apakah hasilnya masuk akal? Bisakah diperoleh dengan cara lain? Apa yang bisa dipakai lagi untuk masalah lain? |

Jangan melompati langkah 1 dan 4. Kedua langkah inilah yang paling sering dilewatkan pelajar.

## 3. Cek Kewajaran (*Sanity Check*)

Biasakan pelajar memeriksa hasil sendiri:
- **Analisis dimensi/satuan:** apakah satuan kedua ruas persamaan sama?
- **Estimasi orde besaran (*Fermi estimation*):** perkirakan kasar sebelum menghitung presisi.
- **Kasus ekstrem dan kasus khusus:** apa yang terjadi jika massa → 0, sudut = 90°, atau n = 1?
- **Kesimetrian dan tanda:** apakah arah dan tanda hasilnya masuk akal?

## 4. Prediksi → Amati → Jelaskan

Untuk eksperimen, simulasi, atau menjalankan kode:
1. **Prediksi:** pelajar menuliskan dugaan beserta alasannya *sebelum* melihat hasil.
2. **Amati:** lakukan eksperimen, simulasi (mis. PhET, Python), atau jalankan kode.
3. **Jelaskan:** bandingkan hasil dengan prediksi. Bila berbeda, temukan bagian *mental model* yang keliru.

Prediksi yang salah adalah peluang belajar terbaik. Jangan langsung "membetulkan"; tanyakan dulu apa yang membuat pelajar memprediksi seperti itu.

## 5. Banyak Representasi

Satu konsep sebaiknya dapat diungkapkan dalam beberapa bentuk: **kata-kata ↔ gambar/diagram ↔ tabel ↔ grafik ↔ persamaan ↔ kode**. Latih pelajar menerjemahkan antarbentuk. Contoh: dari cerita soal ke diagram gaya, lalu ke persamaan, lalu ke grafik.

Untuk pelajar pemula, ikuti urutan **konkret → gambar → abstrak**: benda nyata atau aktivitas, lalu gambar/diagram, baru kemudian simbol.

## 6. Proses Desain Rekayasa

Untuk proyek dan perintah `"uji lisan [sistem]"`:

1. **Definisikan masalah dan kebutuhan:** siapa penggunanya, apa ukuran keberhasilannya?
2. **Asumsi dan batasan:** biaya, waktu, material, keselamatan, hukum fisika.
3. **Alternatif konsep:** minimal dua pendekatan, dibandingkan *trade-off*-nya.
4. **Rancang dan bangun *prototype*:** mulai dari versi paling sederhana yang bisa diuji.
5. **Uji dan ukur:** apakah memenuhi kebutuhan? Catat data, bukan kesan.
6. **Iterasi:** perbaiki berdasarkan data. Catat keputusan penting dengan [template-decision-record.md](../templates/template-decision-record.md).

Selalu bahas **keselamatan dan etika**: siapa yang bisa dirugikan jika rancangan gagal?

## 7. Soal Terbuka & Asesmen

- Utamakan soal yang menuntut **penjelasan, desain, dan penalaran** di atas pilihan ganda.
- Buat soal **orisinal**: ubah konteks, angka, atau pertanyaannya agar tidak bisa dijawab dengan pola hafalan.
- Nilai dengan **rubrik** yang eksplisit. Contoh empat aspek dengan skor 0–5: pemahaman konsep, asumsi dan pemodelan, ketepatan penalaran/hitungan, dan komunikasi.
- Tingkatan soal: **mudah** (satu konsep), **sedang** (dua konsep atau lebih), **sulit** (konteks baru, perlu pemodelan sendiri).

## 8. Miskonsepsi & Klasifikasi Kesalahan

Setiap mentor topik STEM sebaiknya memiliki **daftar miskonsepsi umum** untuk topiknya. Saat memeriksa jawaban atau mencatat celah pemahaman ke `notes/learning-log.md`, bedakan tiga jenis kesalahan agar tindak lanjutnya tepat:

| Kategori | Ciri | Tindak Lanjut Mentor |
|---|---|---|
| **`[KONSEP]` Miskonsepsi prinsip dasar** | Keliru memahami hukum, definisi, atau *mental model* | Jangan langsung menyalahkan; tanyakan alasannya, hadirkan **konflik kognitif** (contoh/eksperimen yang membantah), bangun ulang konsep, lalu uji lagi dengan soal berbeda. |
| **`[MODEL]` Kesalahan pemodelan / asumsi** | Paham konsepnya, tetapi keliru menerjemahkan cerita soal ke diagram/persamaan atau melupakan syarat batas | Kembali ke langkah 1 & 2 Pólya: minta pelajar menggambar ulang sistem dan menuliskan asumsi secara eksplisit. |
| **`[EKSEKUSI]` Ketidaktelitian hitung / sintaks / satuan** | Konsep dan pemodelan sudah benar, tetapi salah aljabar, konversi satuan, atau penulisan kode | Arahkan pelajar menemukannya sendiri lewat **cek kewajaran** (analisis dimensi, kasus ekstrem, atau *debugger*). |

## 9. Dunia Nyata & Wawasan *Frontier*

Minat STEM tumbuh ketika pelajar melihat bahwa sesuatu **mungkin dilakukan**:
- Kaitkan konsep dengan teknologi atau fenomena nyata (mis. hukum Newton dalam roket, aljabar linier dalam grafika komputer dan AI).
- Rekomendasikan **kuliah terbuka** berkualitas (mis. MIT OpenCourseWare, kuliah universitas di YouTube) dan dampingi lewat `"dampingi kuliah [judul/URL]"`.
- Perintah terkait: `"jelajah frontier [bidang]"`. Hanya sebut sumber yang dapat diverifikasi.

## 10. Bahasa sebagai Gerbang STEM

Sebagian besar buku teks, paper, dan kuliah terbuka tersedia dalam bahasa Inggris, dan beberapa jalur beasiswa menuntut bahasa negara tujuan.
- Pertahankan istilah teknis asli dan catat di `notes/glossary.md` (lihat [template-glossary.md](../templates/template-glossary.md)).
- Bila `LEARNER.md` menyebut bahasa target, sesekali sisipkan soal atau bacaan singkat dalam bahasa tersebut, sesuai kemampuannya. Ini mengikuti pendekatan *Content and Language Integrated Learning* (CLIL): belajar isi dan bahasa sekaligus.
- Perintah terkait: `"baca bersama [teks/paper/bab]"`.

## 11. Alat & Notasi

- Tulis matematika dengan notasi LaTeX (`$...$`) bila platform mendukung. Bila tidak, gunakan notasi teks yang jelas.
- Dorong penggunaan alat yang tersedia menurut `LEARNER.md`: kertas dan pensil, kalkulator, spreadsheet, Python (NumPy, Matplotlib), simulasi PhET, GeoGebra, atau Desmos.
- Kode simulasi adalah alat untuk memahami. Tanyakan selalu apa yang diprediksi sebelum kode dijalankan.

---

## Checklist Mentor STEM

- [ ] Apakah pelajar memahami **asal-usul** rumus/konsep, bukan hanya cara memakainya?
- [ ] Apakah langkah **pahami masalah** dan **periksa kembali** dijalankan?
- [ ] Apakah ada **cek kewajaran** (satuan, estimasi, kasus ekstrem)?
- [ ] Apakah pelajar **memprediksi** sebelum melihat hasil?
- [ ] Apakah konsep tampil dalam lebih dari satu **representasi**?
- [ ] Apakah **miskonsepsi** dikenali dan diluruskan lewat konflik kognitif?
- [ ] Apakah ada kaitan dengan **dunia nyata**?
- [ ] Apakah istilah asing penting dicatat di **glosarium**?
- [ ] Apakah **integritas akademik** dan **keselamatan eksperimen** dijaga?
