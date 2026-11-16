# Roadmap Matematika — Dari Bilangan ke Metode Numerik

> **Navigasi:** ⬅️ [README topik](README.md) · [rules.md (Bagian 1)](rules.md) · [rules-misconceptions-and-assessment.md (Bagian 2)](rules-misconceptions-and-assessment.md)
>
> *Instruksi AI: Gunakan roadmap ini untuk menentukan titik awal (lewat diagnosis singkat), urutan materi, dan "tanda sudah menguasai" sebelum pindah fase. Jangan memaksa urutan bila pelajar sedang fokus pada target tertentu (ujian, mata kuliah, proyek); catat celah prasyarat sebagai `[PARKIR]` atau sisipkan sebagai pengulangan singkat.*

---

## Cara Memakai Roadmap

- **Urutan berdasar prasyarat**, bukan berdasar kelas. Fase 4 (statistika & peluang) dan Fase 9 (matematika diskrit) relatif mandiri dan bisa dipelajari paralel setelah Fase 1.
- **Diagnosis dulu:** sebelum memulai fase, ajukan 1–2 soal "tanda sudah menguasai" dari fase sebelumnya. Jika goyah, ulang secukupnya.
- **Tanda sudah menguasai** berupa soal penalaran singkat. Ukurannya adalah penjelasan pelajar, bukan sekadar angka akhir.
- **Kesetaraan jenjang** di bawah ini bersifat kasar dan disusun menurut prasyarat konsep, bukan menurut kurikulum negara tertentu. Pembagian materi per kelas berbeda antar negara dan berubah antar tahun, jadi **cocokkan dengan kurikulum yang dipakai pelajar** (lihat `LEARNER.md`).
- Setiap fase mengikuti **konkret → gambar → abstrak** dan **banyak representasi** (lihat [Protokol STEM](../../docs/stem-pedagogy.md)).

```text
F0 Bilangan → F1 Aljabar → F2 Geometri & Trig → F3 Fungsi & Grafik → F5 Kalkulus Diferensial → F6 Kalkulus Integral → F8 Persamaan Diferensial
                  │                                     │                                                 │
                  ├→ F4 Statistika & Peluang            └→ F7 Aljabar Linier ─────────────────────────────┴→ F10 Metode Numerik
                  └→ F9 Matematika Diskrit
```

---

## Fase 0 — Bilangan & Aritmetika (pecahan, rasio, persen)

*Jenjang kasar: SD akhir–SMP awal; juga titik ulang untuk pembelajar dewasa.*

- **Konsep inti:** nilai tempat, bilangan bulat dan negatif, faktor dan kelipatan, pecahan (sebagai bagian, sebagai pembagian, sebagai titik di garis bilangan), desimal, rasio dan proporsi, persen, pembulatan dan estimasi, urutan operasi.
- **Intuisi/representasi:** potongan kue atau pita kertas → diagram batang pecahan → garis bilangan → simbol. Rasio sebagai "resep yang bisa diperbesar". Bilangan negatif sebagai utang atau suhu di bawah nol.
- **Kaitan rekayasa:** skala gambar teknik dan peta, konsentrasi campuran (semen, larutan), efisiensi dalam persen, estimasi orde besaran sebelum menghitung.
- **Eksplorasi/proyek:** skalakan resep untuk jumlah orang berbeda; bandingkan harga per gram di toko; ukur denah kamar dan gambar ulang dengan skala 1:50.
- **Tanda sudah menguasai:**
  - Jelaskan dengan gambar mengapa $\frac{3}{4} \div \frac{1}{8} = 6$.
  - Harga naik 20% lalu turun 20%. Apakah kembali ke harga awal? Mengapa?
- **Sumber:** OpenStax *Prealgebra 2e*; Khan Academy (aritmetika, pra-aljabar).

## Fase 1 — Aljabar

*Jenjang kasar: SMP–SMA awal.*

- **Konsep inti:** variabel, ekspresi vs persamaan, tanda "=" sebagai relasi kesamaan, sifat distributif, persamaan dan pertidaksamaan linier, sistem persamaan linier dua variabel, eksponen dan akar, faktorisasi, persamaan kuadrat, barisan dan deret aritmetika/geometri.
- **Intuisi/representasi:** timbangan seimbang untuk persamaan; model luas persegi panjang untuk $(a+b)^2$ dan faktorisasi; tabel nilai → pola → rumus.
- **Kaitan rekayasa:** menyusun rumus dari kebutuhan ("biaya = tetap + per unit × jumlah"), mengatur ulang rumus untuk mencari variabel yang dicari, rumus bunga majemuk.
- **Eksplorasi/proyek:** tabel biaya dua paket langganan di spreadsheet, cari titik impas secara aljabar dan grafik; susun pola batang korek api lalu tebak rumus suku ke-$n$.
- **Tanda sudah menguasai:**
  - Tunjukkan dengan gambar luas mengapa $(a+b)^2 \neq a^2 + b^2$.
  - Turunkan rumus jumlah $1 + 2 + \dots + n$ tanpa menghafal.
- **Sumber:** OpenStax *Algebra and Trigonometry 2e*; Khan Academy (aljabar).

## Fase 2 — Geometri & Trigonometri

*Jenjang kasar: SMP–SMA (Fase D–F).*

- **Konsep inti:** sudut, kesebangunan dan kekongruenan, luas dan volume, teorema Pythagoras, koordinat Kartesius, perbandingan trigonometri pada segitiga siku-siku, lingkaran satuan dan radian, aturan sinus dan kosinus, identitas dasar.
- **Intuisi/representasi:** bukti Pythagoras dengan potongan kertas; kesebangunan sebagai "zoom"; sinus/kosinus sebagai koordinat titik yang berputar di lingkaran satuan.
- **Kaitan rekayasa:** survei lahan dan tinggi bangunan, gaya pada bidang miring (bersama Fisika), gelombang dan sinyal bolak-balik, grafika 2D.
- **Eksplorasi/proyek:** ukur tinggi pohon dengan bayangan atau klinometer buatan; animasikan titik pada lingkaran satuan di GeoGebra/Desmos dan amati grafik $\sin\theta$.
- **Tanda sudah menguasai:**
  - Mengapa luas lingkaran sebanding dengan $r^2$, bukan $r$? Jelaskan dengan skala.
  - Tanpa kalkulator, apakah $\sin 100^\circ$ positif atau negatif? Jelaskan dengan lingkaran satuan.
- **Sumber:** OpenStax *Algebra and Trigonometry 2e*; GeoGebra.

## Fase 3 — Fungsi & Grafik

*Jenjang kasar: SMA (Fase E–F).*

- **Konsep inti:** fungsi sebagai aturan masukan→keluaran, domain dan *range* (daerah hasil), fungsi linier, kuadrat, polinomial, eksponensial, logaritma, rasional, trigonometri; transformasi grafik; komposisi dan invers.
- **Intuisi/representasi:** mesin masukan–keluaran; empat representasi yang selalu diterjemahkan: kata ↔ tabel ↔ grafik ↔ rumus. Eksponensial sebagai "bertambah dengan **faktor** tetap", linier sebagai "bertambah dengan **selisih** tetap".
- **Kaitan rekayasa:** kalibrasi sensor (linier), peluruhan dan pertumbuhan, skala desibel dan pH (logaritma), pemodelan data.
- **Eksplorasi/proyek:** di Desmos, geser parameter $a, b, c$ dan prediksi dulu efeknya; cocokkan data (mis. suhu air mendingin) dengan model linier vs eksponensial.
- **Tanda sudah menguasai:**
  - Diberi tabel dengan selisih berurutan tetap vs rasio berurutan tetap: mana linier, mana eksponensial, dan mengapa?
  - Mengapa $\log$ mengubah perkalian menjadi penjumlahan? Apa gunanya bagi skala desibel?
- **Sumber:** OpenStax *Algebra and Trigonometry 2e*; Desmos.

## Fase 4 — Statistika & Peluang

*Jenjang kasar: SMP–SMA untuk deskriptif dan peluang dasar; universitas untuk inferensial.*

- **Konsep inti:** jenis data, ukuran pemusatan dan sebaran, visualisasi data, peluang sebagai frekuensi relatif jangka panjang, kaidah pencacahan, peluang bersyarat, kejadian saling bebas, distribusi (binomial, normal), sampel vs populasi, korelasi vs kausalitas, pengantar inferensi.
- **Intuisi/representasi:** simulasi lempar koin/dadu nyata lalu di komputer; diagram pohon; tabel dua arah untuk peluang bersyarat; histogram.
- **Kaitan rekayasa:** kendali mutu produksi, keandalan komponen, pengujian A/B, ketidakpastian pengukuran.
- **Eksplorasi/proyek:** lempar koin 50 kali dan catat urutan "beruntun"; simulasikan 10.000 lemparan di Python atau spreadsheet dan bandingkan dengan prediksi; survei kecil di kelas dengan laporan keterbatasan.
- **Tanda sudah menguasai:**
  - Dua kelas punya rata-rata nilai sama. Apakah kemampuannya sama? Apa yang perlu dilihat lagi?
  - Tes penyakit 99% akurat, positif. Mengapa peluang benar-benar sakit bisa jauh di bawah 99%?
- **Sumber:** OpenStax *Introductory Statistics 2e*; Khan Academy (statistika & peluang).

## Fase 5 — Kalkulus Diferensial

*Jenjang kasar: pengantar di SMA kelas akhir; mendalam di universitas tahun 1.*

- **Konsep inti:** laju perubahan rata-rata → sesaat, limit (intuitif lalu formal sesuai jenjang), turunan sebagai kemiringan garis singgung dan laju, aturan turunan (diturunkan dari definisi), aturan rantai, maksimum/minimum, laju terkait, aproksimasi linier.
- **Intuisi/representasi:** spidometer vs jarak tempuh; *zoom in* pada grafik sampai kurva tampak lurus; tabel selisih dengan $h$ yang makin kecil.
- **Kaitan rekayasa:** kecepatan dan percepatan, optimasi bentuk kemasan, sensitivitas sistem, *gradient descent* dalam *machine learning*.
- **Eksplorasi/proyek:** hitung $\frac{f(x+h)-f(x)}{h}$ untuk $h = 0{,}1;\ 0{,}01;\ 0{,}001$ di spreadsheet; rancang kaleng bervolume tetap dengan bahan minimum.
- **Tanda sudah menguasai:**
  - Turunkan $\frac{d}{dx}x^2 = 2x$ dari definisi dan jelaskan arti geometrisnya.
  - Grafik $f'$ diberikan. Di mana $f$ naik, dan di mana $f$ mencapai maksimum?
- **Sumber:** OpenStax *Calculus Volume 1*; MIT OCW 18.01SC; 3Blue1Brown *Essence of Calculus*.

## Fase 6 — Kalkulus Integral

*Jenjang kasar: pengantar di SMA kelas akhir; mendalam di universitas tahun 1.*

- **Konsep inti:** akumulasi, jumlah Riemann, integral tentu sebagai luas bertanda, Teorema Dasar Kalkulus, antiturunan, substitusi, integral parsial, aplikasi (luas, volume, kerja, nilai rata-rata), deret (tingkat universitas).
- **Intuisi/representasi:** air yang mengisi tangki dari laju aliran; persegi panjang tipis yang makin banyak; hubungan "laju ↔ akumulasi" sebagai dua sisi satu koin.
- **Kaitan rekayasa:** jarak dari grafik kecepatan, energi dari daya, momen dan pusat massa, total muatan.
- **Eksplorasi/proyek:** hampiri luas di bawah $y = x^2$ dari 0 sampai 1 dengan 4, 10, 100 persegi panjang (spreadsheet/Python) dan bandingkan dengan $\frac{1}{3}$.
- **Tanda sudah menguasai:**
  - Jelaskan dengan kata-kata mengapa turunan dari "luas di bawah kurva sampai $x$" adalah tinggi kurva di $x$.
  - Turunkan rumus luas lingkaran dari keliling dengan mengiris menjadi cincin tipis.
- **Sumber:** OpenStax *Calculus Volume 1–2*; MIT OCW 18.01SC.

## Fase 7 — Aljabar Linier

*Jenjang kasar: dasar matriks dapat dikenalkan di SMA; inti di universitas tahun 1–2.*

- **Konsep inti:** vektor (geometris dan sebagai daftar bilangan), kombinasi linier, sistem persamaan linier dan eliminasi, matriks sebagai transformasi, perkalian matriks sebagai komposisi, determinan sebagai faktor skala luas/volume, invers, ruang vektor dan basis, *eigenvalue* dan *eigenvector*.
- **Intuisi/representasi:** panah di bidang; matriks 2×2 yang "membengkokkan grid"; tabel data sebagai matriks.
- **Kaitan rekayasa:** grafika komputer dan *game*, analisis rangka dan rangkaian (sistem persamaan besar), kompresi gambar, *machine learning*, PageRank.
- **Eksplorasi/proyek:** di GeoGebra atau Python, terapkan matriks rotasi, skala, dan geser ke sebuah gambar; prediksi dulu hasilnya.
- **Tanda sudah menguasai:**
  - Mengapa umumnya $AB \neq BA$? Beri contoh dua transformasi geometris yang urutannya penting.
  - Determinan matriks 0. Apa yang terjadi pada grid, dan mengapa matriks itu tidak punya invers?
- **Sumber:** MIT OCW 18.06 (Gilbert Strang); Strang, *Introduction to Linear Algebra*; 3Blue1Brown *Essence of Linear Algebra*.

## Fase 8 — Persamaan Diferensial

*Jenjang kasar: universitas tahun 1–2.*

- **Konsep inti:** memodelkan "laju perubahan bergantung pada keadaan", PD orde satu (terpisah, linier), medan arah, PD linier orde dua (osilasi, redaman), sistem PD, kestabilan titik setimbang, pengantar transformasi Laplace (sesuai kebutuhan jurusan).
- **Intuisi/representasi:** medan arah sebagai "peta arus"; tabel langkah demi langkah; perbandingan grafik solusi dengan data.
- **Kaitan rekayasa:** pendinginan Newton, rangkaian RC/RLC, pegas-redaman (suspensi), pertumbuhan populasi dan epidemi, sistem kendali.
- **Eksplorasi/proyek:** ukur suhu kopi tiap 2 menit, cocokkan dengan model $\frac{dT}{dt} = -k(T - T_{\text{ruang}})$, dan perkirakan $k$.
- **Tanda sudah menguasai:**
  - Tanpa menyelesaikan, gambarkan bentuk solusi $\frac{dy}{dt} = y(1 - y)$ untuk $y(0) = 0{,}1$ dan jelaskan alasannya.
  - Mengapa solusi PD orde dua butuh dua syarat awal?
- **Sumber:** MIT OCW 18.03SC; Paul's Online Notes (Differential Equations).

## Fase 9 — Matematika Diskrit

*Jenjang kasar: dasar logika & pencacahan di SMA; inti di universitas (terutama CS).*

- **Konsep inti:** logika proposisional, himpunan, fungsi dan relasi, teknik pembuktian (langsung, kontradiksi, induksi), kombinatorika, teori graf, aritmetika modular, rekursi.
- **Intuisi/representasi:** tabel kebenaran; domino jatuh untuk induksi; graf sebagai peta kota.
- **Kaitan rekayasa:** algoritma dan kompleksitas, jaringan, basis data, kriptografi (bersama CS Tutor).
- **Eksplorasi/proyek:** buktikan dengan induksi lalu cek dengan program kecil; pecahkan sandi Caesar dengan aritmetika modular.
- **Tanda sudah menguasai:**
  - Di mana letak kesalahan "bukti" induksi bahwa semua kuda berwarna sama?
  - Mengapa jumlah jabat tangan di sebuah pesta selalu genap bila dihitung per orang lalu dijumlahkan?
- **Sumber:** MIT OCW 6.042J *Mathematics for Computer Science*.

## Fase 10 — Metode Numerik

*Jenjang kasar: universitas tahun 2 ke atas; praktisi rekayasa/CS.*

- **Konsep inti:** representasi bilangan *floating point* dan galat pembulatan, galat pemotongan, metode bagi dua dan Newton–Raphson, interpolasi, integrasi numerik (trapesium, Simpson), metode Euler dan Runge–Kutta untuk PD, kestabilan dan konvergensi.
- **Intuisi/representasi:** "mendekati jawaban selangkah demi selangkah"; grafik galat vs ukuran langkah (skala log–log).
- **Kaitan rekayasa:** simulasi struktur dan fluida, prediksi cuaca, *game physics*, solver di perangkat lunak rekayasa.
- **Eksplorasi/proyek:** selesaikan PD pendinginan dengan metode Euler untuk beberapa ukuran langkah, bandingkan dengan solusi eksak, lalu plot galatnya.
- **Tanda sudah menguasai:**
  - Ukuran langkah Euler dibagi dua, kira-kira bagaimana galatnya berubah? Prediksi dulu, lalu uji.
  - Mengapa membandingkan dua bilangan *floating point* dengan `==` berisiko?
- **Sumber:** Paul's Online Notes; dokumentasi NumPy/SciPy (verifikasi versi sebelum merujuk fungsi tertentu).

---

*⬅️ Kembali ke [README topik](README.md) · Aturan mentor: [rules.md](rules.md)*
