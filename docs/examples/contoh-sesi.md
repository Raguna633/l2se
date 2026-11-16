# Contoh Sesi Belajar (ilustrasi)

Cuplikan berikut menunjukkan perilaku yang diharapkan dari AI Mentor. Ini ilustrasi yang ditulis tangan, bukan transkrip asli, sehingga hasil nyata dapat berbeda antar platform.

---

## 1. Pelajar SMA — Tangga Bantuan & Integritas Akademik

> **Pelajar:** Tolong kerjakan PR fisika saya: balok 2 kg ditarik gaya 10 N di lantai licin, berapa percepatannya?
>
> **Mentor:** Karena ini PR, aku tidak akan menuliskan jawaban akhirnya, tapi aku bantu kamu sampai bisa mengerjakannya sendiri. Pertanyaan pertama: menurutmu, kalau kamu mendorong troli belanja kosong lalu troli yang penuh dengan tenaga yang sama, mana yang lebih cepat bertambah lajunya? *(L1: pertanyaan penuntun)*
>
> **Pelajar:** Yang kosong.
>
> **Mentor:** Tepat. Jadi percepatan bergantung pada gaya dan massa. Hukum Newton mana yang menghubungkan ketiganya? *(L2: hint konsep)*
>
> **Pelajar:** F = m × a?
>
> **Mentor:** Betul. Coba latihan dengan angka lain dulu: troli 5 kg didorong 20 N di lantai licin. Berapa percepatannya, dan apa satuannya? *(L3: contoh terpisah dengan data berbeda)* Setelah itu, kerjakan PR-mu sendiri dengan cara yang sama, lalu kirim jawabanmu kalau ingin aku cek alurnya.

---

## 2. Engineer — Jembatan Konsep dari Profil

> **Pelajar:** Goroutine itu sama dengan `asyncio` di Python, kan?
>
> **Mentor:** Sebelum aku jawab: menurutmu, di `asyncio`, siapa yang memutuskan kapan sebuah *coroutine* berhenti dan memberi giliran ke yang lain?
>
> **Pelajar:** *Coroutine*-nya sendiri, saat ketemu `await`.
>
> **Mentor:** Benar, itu *cooperative scheduling*. Di sinilah analoginya berhenti berlaku: goroutine dijadwalkan oleh Go *runtime*, yang bisa memindahkan goroutine antar *thread* OS dan dapat menghentikannya sementara tanpa kata kunci seperti `await`. Akibatnya, kode Go tidak perlu ditandai `async` sama sekali. Mau kita buktikan dengan eksperimen kecil memakai `runtime.NumGoroutine()`?

---

## 3. Mahasiswa — Ujian Lisan

> **Pelajar:** uji lisan rangkaian pembagi tegangan
>
> **Mentor:** Bayangkan kamu harus menurunkan tegangan baterai 9 V menjadi sekitar 3 V untuk sebuah sensor. Rancang rangkaiannya dari nol. Apa saja yang perlu kamu ketahui dulu sebelum memilih komponen?
>
> **Pelajar:** Pakai dua resistor seri, R1 dan R2, lalu ambil tegangan di R2. Perbandingannya 2:1.
>
> **Mentor:** Dari mana perbandingan 2:1 itu? Turunkan dari hukum Ohm. Lalu, asumsi apa yang kamu pakai tentang arus yang ditarik sensor? Apa yang terjadi pada tegangan keluaran jika sensor menarik arus cukup besar?
>
> *(Setelah beberapa putaran tanya jawab, mentor memberi skor 0–5 untuk pemahaman konsep, asumsi, penalaran, dan komunikasi, lalu menyebut satu celah: efek beban pada pembagi tegangan.)*

---

## 4. Guru — Rancang Materi Ajar

> **Guru:** rancang materi ajar hukum Archimedes untuk kelas 8
>
> **Mentor:** Baik. Sebelum menyusun, dua pertanyaan: berapa menit alokasi waktunya, dan alat apa yang tersedia di kelas (gelas ukur, timbangan, wadah air)? Apakah Bapak memakai format Modul Ajar Kurikulum Merdeka?
>
> **Guru:** 2 × 40 menit, ada gelas ukur dan baskom. Ya, Modul Ajar.
>
> **Mentor:** Ini kerangkanya. Mohon cocokkan CP dan TP dengan dokumen kurikulum resmi sekolah Bapak:
> 1. **Tujuan Pembelajaran:** peserta didik dapat memprediksi lalu menjelaskan mengapa benda terapung, melayang, atau tenggelam.
> 2. **Asesmen diagnostik (5 menit):** "Kapal baja yang berat bisa terapung, tetapi paku kecil tenggelam. Kenapa?" Catat jawaban awal untuk mengungkap miskonsepsi "benda berat pasti tenggelam".
> 3. **Kegiatan inti (prediksi → amati → jelaskan):** kelompok memprediksi, lalu mencelupkan plastisin bulat vs berbentuk perahu dan mengukur air yang dipindahkan dengan gelas ukur.
> 4. **Asesmen formatif:** satu soal terbuka: "Rancang perahu dari selembar aluminium foil yang bisa membawa koin paling banyak. Jelaskan alasannya."
> 5. **Asesmen sumatif dan rubrik:** rubrik 0–5 untuk konsep, prediksi, penalaran, dan komunikasi.
>
> Mau saya lanjutkan dengan lembar kerja peserta didik atau bank soal bertingkat?

---

## 5. Akhir Sesi — Catat Log

> **Pelajar:** catat log
>
> **Mentor:** Ini draf entri untuk `science/physics/notes/learning-log.md`:
>
> ```markdown
> ### Log Belajar — 2026-11-20
> * Topik: Hukum II Newton
> * Yang sudah dikuasai: hubungan F, m, a lewat contoh troli
> * Yang masih membingungkan: membedakan massa dan berat
> * Jadwal kuis ulang: 2026-11-21, 2026-11-23
> ```
>
> Simpan ke berkas tersebut?
