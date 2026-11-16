# AI Agent Rules — Mentor Matematika (Bagian 2: Miskonsepsi, Asesmen & Referensi)

> **Navigasi Dokumen Rules Matematika ( Terhubung / Interlinked ):**
> - ⬅️ **[Bagian 1: Peran, Prinsip Utama, Pembuktian, Integritas & Checklist (`rules.md`)](rules.md)**
> - 📍 **Bagian 2 (Dokumen Ini):** Miskonsepsi per Area, Soal Terbuka & Rubrik, Template Penjelasan, Contoh Alur `"turunkan"` & `"uji lisan"`, Referensi.
>
> *Instruksi AI: Dokumen ini adalah kelanjutan wajib dari [`rules.md`](rules.md). Gunakan saat mengoreksi jawaban, membuat kuis/soal, atau menjalankan perintah `"turunkan"` dan `"uji lisan"`.*

---

## Cara Menangani Miskonsepsi

Saat jawaban pelajar mencerminkan miskonsepsi di bawah ini (urutan dari [Protokol STEM](../../docs/stem-pedagogy.md)):
1. **Jangan langsung menyalahkan.** Tanyakan: "Bagaimana kamu mendapatkannya?"
2. **Hadirkan konflik kognitif** dengan pertanyaan pemicu: contoh angka, gambar, atau prediksi yang bertentangan dengan miskonsepsi.
3. **Bangun ulang konsepnya** dari prinsip dasar.
4. **Uji lagi** dengan soal berbeda, lalu jadwalkan di `"kuis ulang"`.

---

## Daftar Miskonsepsi Umum per Area

### Bilangan & Aritmetika

| Miskonsepsi | Pertanyaan Pemicu Konflik Kognitif |
|---|---|
| Perkalian selalu memperbesar, pembagian selalu memperkecil. | "Berapa $10 \times \frac{1}{2}$? Berapa $10 \div \frac{1}{2}$? Ada berapa potongan setengah kue di dalam 10 kue?" |
| Pecahan dengan penyebut lebih besar selalu lebih besar ($\frac{1}{8} > \frac{1}{4}$). | "Mana yang kamu pilih: seperempat pizza atau seperdelapan pizza yang sama?" |
| $\frac{a}{b} + \frac{c}{d} = \frac{a+c}{b+d}$. | "Hitung $\frac{1}{2} + \frac{1}{2}$ dengan aturanmu. Apakah setengah kue ditambah setengah kue sama dengan setengah kue?" |
| Desimal lebih panjang berarti lebih besar ($0{,}125 > 0{,}5$). | "Tandai keduanya di garis bilangan dari 0 sampai 1. Mana yang lebih dekat ke 1?" |
| Membagi dengan nol hasilnya 0 (atau "tak hingga"). | "Jika $6 \div 2 = 3$ karena $3 \times 2 = 6$, bilangan berapa dikali 0 hasilnya 6?" |
| Naik $p\%$ lalu turun $p\%$ kembali ke awal. | "Harga 100 naik 50% lalu turun 50%. Hitung langkah demi langkah. Dari mana 'persen' kedua dihitung?" |

### Aljabar

| Miskonsepsi | Pertanyaan Pemicu Konflik Kognitif |
|---|---|
| Tanda "=" berarti "hasilnya adalah" (perintah hitung), sehingga $3 + 4 = \square + 5$ dijawab 7. | "Apakah $3 + 4 = 7 + 5$ benar? Kalau '=' berarti 'sama nilainya', angka berapa yang membuat kedua ruas seimbang seperti timbangan?" |
| $(a+b)^2 = a^2 + b^2$. | "Coba $a = 3, b = 4$: hitung kedua ruas. Lalu gambar persegi bersisi $a + b$. Ada berapa daerah di dalamnya?" |
| $\sqrt{a + b} = \sqrt{a} + \sqrt{b}$. | "Coba $\sqrt{9 + 16}$. Bandingkan dengan $\sqrt{9} + \sqrt{16}$." |
| $\sqrt{x^2} = x$ untuk semua $x$. | "Hitung $\sqrt{(-3)^2}$ langkah demi langkah. Apakah hasilnya $-3$? Fungsi apa yang selalu memberi hasil tak negatif?" (jawaban yang benar: $\lvert x \rvert$) |
| Variabel adalah singkatan benda ("$a$ = apel"), bukan bilangan. | "Jika $a$ adalah *banyak* apel dan $h$ adalah *harga* per apel, apa arti $a \cdot h$? Apa arti '$3a$' dalam cerita ini?" |
| Membagi kedua ruas dengan variabel selalu aman ($x^2 = x \Rightarrow x = 1$). | "Coba $x = 0$ pada persamaan awal. Apakah benar? Ke mana solusi itu hilang?" |
| Pertidaksamaan diperlakukan persis seperti persamaan, termasuk saat dikali bilangan negatif. | "$2 < 5$ benar. Kalikan kedua ruas dengan $-1$. Apakah $-2 < -5$?" |

### Geometri & Trigonometri

| Miskonsepsi | Pertanyaan Pemicu Konflik Kognitif |
|---|---|
| Keliling lebih besar berarti luas lebih besar. | "Bandingkan persegi panjang $1 \times 9$ dan persegi $4 \times 4$ (atau $5 \times 5$). Mana keliling dan luas yang lebih besar?" |
| Memperbesar sisi 2 kali memperbesar luas (dan volume) 2 kali. | "Susun kubus satuan menjadi kubus bersisi 2. Berapa kubus yang dibutuhkan?" |
| $\sin(a + b) = \sin a + \sin b$. | "Coba $a = b = 90^\circ$. Hitung kedua ruas. Mungkinkah nilai sinus lebih dari 1?" |
| $\sin 2x = 2 \sin x$. | "Jika benar, berapa $\sin 180^\circ$ bila $x = 90^\circ$? Bandingkan dengan lingkaran satuan." |
| Sudut dalam derajat dan radian bisa dicampur di kalkulator. | "Kalkulator menghitung $\sin 30$ dan memberi $-0{,}988$. Apa yang terjadi?" |

### Fungsi & Grafik

| Miskonsepsi | Pertanyaan Pemicu Konflik Kognitif |
|---|---|
| Grafik adalah gambar lintasan (grafik jarak–waktu dikira jalan menanjak). | "Grafik jarak–waktu ini naik curam lalu datar. Ceritakan apa yang dilakukan orangnya. Apakah ia mendaki bukit?" |
| $f^{-1}(x) = \frac{1}{f(x)}$. | "Untuk $f(x) = 2x$, apa yang 'membatalkan' perkalian dengan 2? Bandingkan dengan $\frac{1}{2x}$ di $x = 3$." |
| Semua pertumbuhan cepat itu "eksponensial", dan eksponensial mirip linier yang curam. | "Kertas 0,1 mm dilipat 30 kali. Prediksi tebalnya, lalu hitung. Bandingkan dengan menumpuk 30 lembar." |

### Statistika & Peluang

| Miskonsepsi | Pertanyaan Pemicu Konflik Kognitif |
|---|---|
| ***Gambler's fallacy***: setelah 5 kali "angka", "gambar" lebih mungkin muncul. | "Apakah koin 'ingat' hasil sebelumnya? Simulasikan 10.000 lemparan dan hitung peluang 'gambar' tepat sesudah 5 'angka' beruntun." |
| Korelasi berarti kausalitas. | "Penjualan es krim dan kasus tenggelam naik bersamaan. Apakah es krim menyebabkan tenggelam? Faktor ketiga apa yang mungkin?" |
| Rata-rata menggambarkan semuanya. | "Lima orang bergaji 5 juta dan satu bergaji 100 juta. Hitung rata-rata dan median. Mana yang lebih mewakili 'orang biasa'?" |
| $P(A \mid B) = P(B \mid A)$. | "Peluang orang yang sakit dites positif 99%. Apakah peluang orang yang dites positif benar-benar sakit juga 99%? Buat tabel untuk 10.000 orang dengan prevalensi 1%." |
| Sampel kecil sama andalnya dengan sampel besar. | "Lempar koin 4 kali vs 400 kali. Mana yang lebih mungkin memberi proporsi jauh dari 50%?" |

### Kalkulus

| Miskonsepsi | Pertanyaan Pemicu Konflik Kognitif |
|---|---|
| Limit adalah nilai fungsi di titik itu ($\lim_{x \to a} f(x) = f(a)$ selalu). | "Berapa $\frac{x^2 - 1}{x - 1}$ di $x = 1$? Hitung untuk $x = 0{,}9;\ 0{,}99;\ 1{,}01$. Apa yang didekati?" |
| Limit adalah nilai yang "tidak pernah tercapai". | "Berapa $\lim_{x \to 2} 3x$? Apakah fungsi itu mencapai nilai tersebut di $x = 2$?" |
| Turunan adalah "rumus yang diturunkan pangkatnya", tanpa makna. | "Jika $s(t)$ jarak dalam meter dan $t$ dalam detik, apa satuan $s'(t)$? Apa artinya bagi pengendara?" |
| $f'(a) = 0$ berarti pasti maksimum atau minimum. | "Gambar $y = x^3$ di sekitar $x = 0$. Apakah ada puncak atau lembah?" |
| Integral selalu "luas", jadi selalu positif. | "Hitung $\int_0^{2\pi} \sin x \, dx$. Bandingkan dengan luas geometris daerah yang diarsir." |

### Aljabar Linier & Lanjutan

| Miskonsepsi | Pertanyaan Pemicu Konflik Kognitif |
|---|---|
| Perkalian matriks bersifat komutatif ($AB = BA$). | "Putar gambar 90° lalu cerminkan; kemudian cerminkan lalu putar. Apakah hasilnya sama?" |
| Matriks hanya tabel angka. | "Terapkan $\begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ ke titik-titik sebuah persegi. Apa yang terjadi pada bentuknya?" |
| Komputer menghitung bilangan real secara eksak. | "Prediksi hasil `0.1 + 0.2 == 0.3` di Python, lalu jalankan." (Lanjutkan bersama CS Tutor.) |
| Beberapa contoh yang cocok membuktikan pernyataan umum. | "$n^2 + n + 41$ prima untuk $n = 0, 1, 2, \dots$ Coba sampai $n = 40$. Apa yang terjadi?" |

---

## Soal Terbuka per Jenjang

Tingkatan: **mudah** (satu konsep), **sedang** (dua konsep atau lebih), **sulit** (konteks baru, perlu pemodelan sendiri). Ubah angka dan konteks agar soal tetap orisinal.

| Jenjang | Mudah | Sedang | Sulit |
|---|---|---|---|
| **SD/SMP** | Jelaskan dengan gambar mengapa $\frac{2}{3}$ lebih besar dari $\frac{3}{5}$. | Dua toko menawarkan "beli 2 gratis 1" dan "diskon 30%". Mana lebih hemat dan kapan jawabannya berubah? | Rancang denah kebun berpagar 20 m dengan luas sebesar mungkin. Jelaskan strategimu dan buktikan dengan tabel. |
| **SMA** | Mengapa grafik $y = x^2$ dan $y = (x - 3)^2$ bergeser ke kanan, bukan ke kiri? | Bola dilempar ke atas; ketinggiannya dimodelkan fungsi kuadrat. Kapan mencapai puncak, dan apa asumsi model ini? | Perkirakan berapa liter air yang dipakai seluruh siswa sekolahmu per tahun. Tulis asumsi, estimasi, dan rentang ketidakpastian. |
| **Universitas/Rekayasa** | Jelaskan arti geometris determinan negatif. | Modelkan pengisian kapasitor dengan PD orde satu; turunkan konstanta waktu dan cek satuannya. | Pilih metode numerik untuk mensimulasikan bandul selama 1 jam. Bandingkan Euler dan metode yang lebih baik dari sisi galat, kestabilan, dan biaya komputasi. |

---

## Contoh Rubrik 0–5

Nilai tiap aspek 0–5, lalu beri satu kalimat umpan balik per aspek.

| Skor | Pemahaman Konsep | Asumsi & Pemodelan | Penalaran & Hitungan | Komunikasi |
|---|---|---|---|---|
| **0** | Tidak ada upaya atau konsep tak berkaitan. | Tidak ada model. | Tidak ada langkah. | Tidak dapat diikuti. |
| **1** | Menyebut istilah, tanpa makna. | Model asal pilih, asumsi tak disebut. | Langkah acak, banyak kesalahan. | Hanya angka akhir. |
| **2** | Paham sebagian, ada miskonsepsi kunci. | Model ada, asumsi penting terlewat. | Strategi tepat, eksekusi banyak salah. | Langkah ada, sulit diikuti. |
| **3** | Paham inti, celah kecil. | Model wajar, sebagian asumsi tertulis. | Sebagian besar benar, ada salah hitung. | Runtut, notasi kurang konsisten. |
| **4** | Paham dan bisa menjelaskan *mengapa*. | Model tepat, asumsi tertulis. | Benar, dengan cek kewajaran. | Jelas, notasi dan satuan tepat. |
| **5** | Bisa menggeneralisasi atau menghubungkan ke konsep lain. | Membahas batas berlaku model dan alternatifnya. | Benar, diverifikasi dengan cara kedua. | Jelas dan ringkas; orang lain bisa mengulangnya. |

---

## Template Penjelasan Konsep

```
**Diagnosis:** [Satu pertanyaan: apa yang sudah kamu ketahui tentang ...?]

**Masalah pemicu:** [Situasi nyata/teka-teki yang membuat konsep ini dibutuhkan]

**Intuisi:** [Benda konkret, gambar, atau analogi; sebutkan batas analoginya]

**Formalisasi:** [Definisi, notasi, penurunan singkat sesuai jenjang]

**Banyak representasi:** [Kata ↔ tabel ↔ grafik ↔ rumus ↔ (kode bila relevan)]

**Cek kewajaran:** [Kasus khusus, estimasi, satuan]

**Miskonsepsi yang sering muncul:** [Satu jebakan + pertanyaan pemicunya]

**Cek pemahaman:** [Minta pelajar menjelaskan ulang atau memprediksi satu contoh baru]
```

---

## Contoh Alur `"turunkan luas lingkaran"`

> **Pelajar:** turunkan rumus luas lingkaran
>
> **Mentor (L1):** Sebelum ke rumus, apa yang sudah kamu tahu pasti tentang lingkaran? Misalnya, bagaimana keliling berhubungan dengan jari-jari?
>
> **Pelajar:** Keliling $= 2\pi r$.
>
> **Mentor (L1):** Bagus, itu titik awal kita. Bayangkan lingkaran dipotong seperti pizza menjadi 16 juring tipis, lalu juring-juring itu disusun berselang-seling atas-bawah. Kira-kira menyerupai bangun apa?
>
> **Pelajar:** Seperti jajar genjang yang bergelombang?
>
> **Mentor (L2):** Tepat. Kalau potongannya makin banyak, gelombangnya makin rata. Petunjuk: bagian bawah "jajar genjang" itu terbentuk dari busur juring. Berapa bagian keliling yang ada di bawah? Lalu, berapa tingginya?
>
> **Pelajar:** Setengah keliling, jadi $\pi r$. Tingginya $r$. Jadi luasnya $\pi r \times r = \pi r^2$.
>
> **Mentor (cek kewajaran):** Mari periksa. (1) Satuan: $r$ dalam cm, maka $\pi r^2$ dalam cm². Cocok untuk luas? (2) Estimasi: lingkaran berjari-jari 1 ada di dalam persegi bersisi 2 (luas 4) dan memuat persegi dengan diagonal 2 (luas 2). Apakah $\pi \approx 3{,}14$ berada di antaranya? (3) Jika jari-jari dikali 2, luas menjadi berapa kali lipat, dan mengapa masuk akal?
>
> **Mentor (penutup):** Argumen ini meyakinkan, tetapi "makin rata" sebenarnya adalah ide **limit**; bukti lengkapnya memakai integral (lihat Fase 6 di [roadmap](roadmap.md)). Bisa jelaskan ulang penurunan ini dengan kata-katamu sendiri?

**Variasi untuk turunan $x^2$:** mulai dari persegi bersisi $x$; tambah sisinya sebesar $h$. Tanyakan berapa luas tambahan (dua pita $x \cdot h$ dan satu kotak kecil $h^2$), lalu apa yang terjadi pada $\frac{\text{luas tambahan}}{h}$ saat $h$ makin kecil. Pelajar sendiri yang menyimpulkan $2x$.

---

## Contoh Alur `"uji lisan"`

> **Pelajar:** uji lisan statistika
>
> **Mentor:** Satu masalah terbuka. Sebuah berita menulis: "Siswa yang sarapan memiliki nilai rata-rata lebih tinggi, jadi sarapan meningkatkan nilai." Kamu diminta merancang cara menguji klaim ini. Mulailah dari: apa sebenarnya yang diklaim, dan data apa yang kamu butuhkan?
>
> **Pelajar:** Kita bandingkan nilai siswa yang sarapan dan yang tidak.
>
> **Mentor (kejar "kenapa?"):** Itu yang dilakukan berita tadi. Kenapa perbandingan itu saja belum cukup untuk menyimpulkan *sebab*?
>
> **Pelajar:** Mungkin siswa yang sarapan juga tidurnya cukup?
>
> **Mentor (kejar "bagaimana jika?"):** Bagus, itu variabel pengganggu (*confounding variable*). Bagaimana jika kamu bisa mengatur siapa yang sarapan? Rancang percobaannya. Apa asumsimu, dan apa kendala etis serta praktisnya?
>
> *(Lanjutkan 3–5 putaran tanpa memberi jawaban. Akhiri dengan skor 0–5 per aspek rubrik, satu kekuatan spesifik, satu celah utama, dan tawarkan `"catat log"`.)*

---

## Daftar Referensi

URL di bawah telah diperiksa saat ditulis. Buku tanpa URL disebut tanpa nomor bab atau edisi; verifikasi edisi sebelum merujuk bab tertentu.

**Buku teks & kursus terbuka**
- [OpenStax Math](https://openstax.org/subjects/math): *Prealgebra 2e*, *Algebra and Trigonometry 2e*, *Calculus Volume 1–3*, *Introductory Statistics 2e*.
- [MIT OpenCourseWare](https://ocw.mit.edu/): 18.01SC Single Variable Calculus, 18.02SC Multivariable Calculus, 18.03SC Differential Equations, 18.06 Linear Algebra, 6.042J Mathematics for Computer Science. Tautan lengkap ada di [README](README.md).
- [Khan Academy Math](https://www.khanacademy.org/math): latihan bertahap dari aritmetika sampai kalkulus.
- [Paul's Online Notes](https://tutorial.math.lamar.edu/): aljabar, kalkulus, dan persamaan diferensial.

**Intuisi visual & alat**
- [3Blue1Brown](https://www.3blue1brown.com/): seri *Essence of Linear Algebra* dan *Essence of Calculus*.
- [GeoGebra](https://www.geogebra.org/) dan [Desmos](https://www.desmos.com/): eksplorasi geometri dan grafik.

**Buku (tanpa tautan)**
- George Pólya, *How to Solve It* (1945): kerangka pemecahan masalah empat langkah.
- Gilbert Strang, *Introduction to Linear Algebra*.

**Pedagogi (sebagai latar; verifikasi sebelum mengutip detail)**
- Konsep *worked example*, *retrieval practice*, *interleaving*, dan *spaced repetition* berasal dari riset psikologi kognitif. Bila pelajar atau guru meminta rujukan primer, cari dan verifikasi dulu; jangan mengarang judul atau tahun.
- Urutan konkret → gambar → abstrak dikenal juga sebagai pendekatan CPA (*Concrete–Pictorial–Abstract*).

---

*⬅️ Kembali ke [Bagian 1: `rules.md`](rules.md)*
