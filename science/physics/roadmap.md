# Roadmap Fisika — Fase Berurutan Berdasar Prasyarat

> **Navigasi:** [README Fisika](README.md) · [Bagian 1: rules.md](rules.md) · [Bagian 2: Miskonsepsi & Eksperimen](rules-misconceptions-and-experiments.md) · [Protokol STEM](../../docs/stem-pedagogy.md)
>
> *Instruksi AI: gunakan roadmap ini untuk menentukan urutan materi dan memeriksa prasyarat. Sesuaikan kedalaman dengan jalur di [README.md](README.md) (A: fenomena, B: SMA, C: universitas, D: rekayasa). Matematika prasyarat dirujuk ke paket Matematika `mathematics/foundations/roadmap.md`; bila pelajar belum menguasainya, tawarkan jeda singkat ke materi tersebut.*

---

## Cara Membaca Roadmap Ini

Setiap fase memuat:
- **Konsep inti:** gagasan yang harus dipahami, bukan sekadar dihafal.
- **Matematika prasyarat:** per jalur. Jalur A cukup aritmetika dan membaca grafik.
- **Eksperimen & simulasi:** eksperimen rumahan yang aman dan simulasi PhET (https://phet.colorado.edu/) atau Python. Aturan keselamatan ada di [rules.md](rules.md).
- **Kaitan rekayasa:** di mana konsep ini dipakai.
- **Tanda sudah menguasai:** soal penalaran singkat. Pelajar dianggap siap lanjut bila bisa menjawab dan menjelaskan alasannya.

**Kesetaraan sekolah** (patokan kasar): tingkat dasar sebagian besar fase muncul di sains SMP dan awal SMA, pendalaman kuantitatifnya di fisika SMA, dan jalur C setara mata kuliah Fisika Dasar I–II. Pembagian per kelas berbeda antar negara dan berubah antar tahun, jadi cocokkan dengan kurikulum yang dipakai pelajar (lihat `LEARNER.md`).

Urutan prasyarat: **0 → 1 → 2 → 3 → 4/5 → 6 → 7/8 → 9 → 10 → 11**. Fase dengan garis miring boleh ditukar urutannya.

---

## Fase 0 — Pengukuran, Satuan SI, Ketidakpastian, Analisis Dimensi

- **Konsep inti:** besaran pokok dan turunan; tujuh satuan dasar SI (m, kg, s, A, K, mol, cd); awalan (mili, kilo, mega); angka penting; ketidakpastian pengukuran (resolusi alat, pengulangan, rata-rata); analisis dimensi; estimasi orde besaran (*Fermi estimation*).
- **Matematika prasyarat:** pecahan, perbandingan, notasi ilmiah, pembulatan. Jalur C: rambatan ketidakpastian (turunan parsial).
- **Eksperimen & simulasi:** ukur tebal satu lembar kertas dengan mengukur tumpukan 100 lembar; ukur waktu reaksi dengan penggaris yang dijatuhkan; perkirakan jumlah butir beras dalam 1 kg.
- **Kaitan rekayasa:** toleransi ukuran pada manufaktur, kalibrasi sensor, konversi satuan (kegagalan konversi satuan pernah menyebabkan kegagalan misi wahana antariksa).
- **Tanda sudah menguasai:** "Seseorang menulis rumus jarak $s = v t^2$. Tanpa menghafal rumus yang benar, bagaimana kamu tahu rumus itu salah?" (jawaban: satuan ruas kanan m·s, bukan m).
- **Sumber:** OpenStax *Physics*, bab pengantar tentang pengukuran; John R. Taylor, *An Introduction to Error Analysis*.

## Fase 1 — Kinematika

- **Konsep inti:** posisi, perpindahan vs jarak, kecepatan vs kelajuan, percepatan; gerak lurus beraturan (GLB) dan gerak lurus berubah beraturan (GLBB); grafik posisi–waktu dan kecepatan–waktu (kemiringan = laju perubahan, luas = perubahan); gerak jatuh bebas; gerak parabola sebagai dua gerak lurus yang independen; gerak melingkar beraturan dan percepatan sentripetal $a = v^2/r$.
- **Matematika prasyarat:** jalur B: persamaan linear dan kuadrat, grafik fungsi, trigonometri dasar, vektor (penguraian komponen). Jalur C: turunan dan integral sebagai laju dan akumulasi.
- **Eksperimen & simulasi:** rekam bola menggelinding di lantai miring dengan kamera ponsel lalu tandai posisi per bingkai; PhET *Projectile Motion*; plot posisi–waktu di spreadsheet.
- **Kaitan rekayasa:** jarak pengereman kendaraan, desain tikungan jalan, lintasan peluncuran.
- **Tanda sudah menguasai:** "Bola dilempar tegak lurus ke atas. Di titik tertinggi, berapa kecepatannya dan berapa percepatannya?" (kecepatan nol, percepatan tetap $g$ ke bawah). "Kenapa luas di bawah grafik v–t sama dengan perpindahan?"
- **Sumber:** OpenStax *University Physics Volume 1* (bab kinematika); MIT OCW 8.01.

## Fase 2 — Dinamika (Hukum Newton)

- **Konsep inti:** gaya sebagai interaksi antara dua benda; hukum I (inersia), II ($\Sigma \vec F = m \vec a$), III (pasangan aksi–reaksi bekerja pada benda berbeda); *free-body diagram* (diagram benda bebas); berat vs massa; gaya normal, tegangan tali, gesekan statis dan kinetis; gaya sentripetal sebagai peran, bukan jenis gaya baru; kerangka acuan inersial.
- **Matematika prasyarat:** vektor dan komponennya, sistem persamaan linear, trigonometri. Jalur C: persamaan diferensial sederhana (gerak dengan hambatan udara).
- **Eksperimen & simulasi:** tarik buku dengan karet gelang dan amati panjang karet saat mulai bergerak vs saat bergerak tetap (gesekan statis vs kinetis); PhET *Forces and Motion: Basics* dan *Friction*.
- **Kaitan rekayasa:** analisis struktur sederhana, sabuk pengaman dan *airbag*, desain lift dan derek.
- **Tanda sudah menguasai:** "Kotak didorong dengan kecepatan tetap di lantai kasar. Mana yang lebih besar: gaya dorong atau gaya gesek?" (sama besar, karena percepatan nol). "Kuda menarik kereta; kalau gaya aksi–reaksi sama besar, kenapa keduanya bisa bergerak?"
- **Sumber:** OpenStax *University Physics Volume 1*; Halliday/Resnick/Walker; Kleppner & Kolenkow (jalur C dan olimpiade).

## Fase 3 — Usaha, Energi, dan Momentum

- **Konsep inti:** usaha $W = \vec F \cdot \vec s$; energi kinetik dan potensial; teorema usaha–energi; kekekalan energi mekanik dan kapan berlaku (tanpa gaya non-konservatif); daya; impuls dan momentum; kekekalan momentum pada sistem terisolasi; tumbukan lenting dan tidak lenting.
- **Matematika prasyarat:** perkalian titik vektor (jalur B lanjut), aljabar; jalur C: integral garis sederhana $W = \int \vec F \cdot d\vec s$.
- **Eksperimen & simulasi:** jatuhkan bola dari beberapa ketinggian dan ukur tinggi pantulan (fraksi energi yang tersisa); PhET *Energy Skate Park* dan *Collision Lab*.
- **Kaitan rekayasa:** *crumple zone* mobil (memperpanjang waktu tumbukan), pembangkit listrik tenaga air, efisiensi motor, roket (kekekalan momentum).
- **Tanda sudah menguasai:** "Dua bola identik dilepas dari ketinggian sama: satu jatuh bebas, satu meluncur di lintasan licin melengkung. Mana yang lebih cepat saat sampai di bawah?" (lajunya sama, waktunya bisa berbeda). "Kenapa helm menurunkan risiko cedera padahal perubahan momentumnya sama?"
- **Sumber:** OpenStax *University Physics Volume 1*; MIT OCW 8.01.

## Fase 4 — Rotasi dan Kesetimbangan Benda Tegar

- **Konsep inti:** besaran sudut; *torque* (momen gaya) $\tau = r F \sin\theta$; momen inersia; $\Sigma \tau = I \alpha$; energi kinetik rotasi; momentum sudut dan kekekalannya; menggelinding tanpa slip; syarat kesetimbangan ($\Sigma \vec F = 0$ dan $\Sigma \tau = 0$); titik berat.
- **Matematika prasyarat:** trigonometri, perkalian silang vektor (jalur C), integral untuk momen inersia (jalur C).
- **Eksperimen & simulasi:** cari titik berat karton tak beraturan dengan menggantungnya dari dua titik; lomba menggelinding kaleng penuh vs kaleng kosong di bidang miring (prediksi dulu).
- **Kaitan rekayasa:** kunci pas dan engsel pintu, roda gila (*flywheel*), keseimbangan *crane*, desain balok dan jembatan.
- **Tanda sudah menguasai:** "Kenapa gagang pintu dipasang jauh dari engsel?" "Penari es merapatkan lengan lalu berputar lebih cepat. Besaran apa yang kekal dan kenapa?"
- **Sumber:** OpenStax *University Physics Volume 1*; Halliday/Resnick/Walker.

## Fase 5 — Gravitasi

- **Konsep inti:** hukum gravitasi umum Newton $F = G m_1 m_2 / r^2$; medan gravitasi; $g$ sebagai kuat medan di permukaan; orbit melingkar; hukum Kepler; energi potensial gravitasi umum; kecepatan lepas; "tanpa bobot" di orbit sebagai jatuh bebas.
- **Matematika prasyarat:** pangkat dan akar, notasi ilmiah; jalur C: integral $1/r^2$.
- **Eksperimen & simulasi:** PhET *Gravity and Orbits*; estimasi Fermi periode orbit stasiun antariksa dari jari-jari Bumi dan $g$.
- **Kaitan rekayasa:** satelit komunikasi geostasioner, GPS, peluncuran wahana.
- **Tanda sudah menguasai:** "Astronaut di stasiun antariksa (ketinggian sekitar 400 km) melayang. Apakah gravitasi di sana nol?" (tidak; sekitar 89% dari $g$ di permukaan; mereka dan stasiunnya sama-sama jatuh bebas).
- **Sumber:** OpenStax *University Physics Volume 1*; Feynman Lectures Vol. I.

## Fase 6 — Osilasi dan Gelombang

- **Konsep inti:** gerak harmonik sederhana (pegas $T = 2\pi\sqrt{m/k}$, bandul untuk simpangan kecil $T = 2\pi\sqrt{L/g}$); energi osilator; redaman dan resonansi; gelombang transversal dan longitudinal; $v = f\lambda$; superposisi dan interferensi; gelombang berdiri; bunyi, intensitas, efek Doppler.
- **Matematika prasyarat:** fungsi sinus dan kosinus, radian; jalur C: persamaan diferensial orde dua $\ddot x = -\omega^2 x$.
- **Eksperimen & simulasi:** bandul dari tali dan mur untuk mengukur $g$; gelombang berdiri pada tali atau slinky; PhET *Pendulum Lab*, *Masses and Springs*, *Wave on a String*, *Wave Interference*.
- **Kaitan rekayasa:** peredam getaran gedung tinggi, resonansi jembatan, suspensi kendaraan, akustik ruangan, sensor ultrasonik.
- **Tanda sudah menguasai:** "Bandul jam dibawa ke Bulan. Jamnya menjadi lebih cepat atau lebih lambat? Kenapa?" "Kenapa prajurit diminta tidak berbaris serentak saat melintasi jembatan?"
- **Sumber:** OpenStax *University Physics Volume 1*; MIT OCW 8.03.

## Fase 7 — Fluida

- **Konsep inti:** massa jenis; tekanan $p = F/A$; tekanan hidrostatis $p = \rho g h$; hukum Pascal; prinsip Archimedes; persamaan kontinuitas; asas Bernoulli dan batas berlakunya (fluida ideal); viskositas (kualitatif).
- **Matematika prasyarat:** aljabar, luas dan volume; jalur C: integral tekanan pada dinding.
- **Eksperimen & simulasi:** telur di air tawar vs air garam; botol plastik berlubang di beberapa ketinggian (amati pancaran air); PhET *Under Pressure*, *Buoyancy*, *Density*.
- **Kaitan rekayasa:** dongkrak dan rem hidrolik, bendungan (dinding lebih tebal di bawah), kapal, sistem perpipaan.
- **Tanda sudah menguasai:** "Kapal baja yang berat bisa terapung, tetapi paku baja tenggelam. Jelaskan dengan prinsip Archimedes." "Kenapa dinding bendungan lebih tebal di bagian bawah?"
- **Sumber:** OpenStax *University Physics Volume 1*.

## Fase 8 — Suhu, Kalor, dan Termodinamika

- **Konsep inti:** suhu vs kalor; skala Celsius dan Kelvin; kalor jenis dan kalor laten; konduksi, konveksi, radiasi; pemuaian; gas ideal $pV = nRT$; teori kinetik (pada gas ideal, suhu sebanding dengan energi kinetik translasi rata-rata partikel; definisi umum suhu bersifat termodinamika, lewat keseimbangan termal); hukum ke-0, ke-1, dan ke-2 termodinamika; mesin kalor dan efisiensi Carnot; entropi (kualitatif).
- **Matematika prasyarat:** aljabar, grafik $p$–$V$; jalur C: integral $W = \int p\,dV$, logaritma natural.
- **Eksperimen & simulasi:** sentuh logam dan kayu yang sama-sama bersuhu ruang (mana yang terasa lebih dingin, dan kenapa?); campur air panas dan dingin lalu prediksi suhu akhir; PhET *States of Matter*, *Gas Properties*, *Energy Forms and Changes*.
- **Kaitan rekayasa:** mesin kendaraan, kulkas dan AC (pompa kalor), isolasi bangunan, pendinginan prosesor.
- **Tanda sudah menguasai:** "Kenapa efisiensi mesin kalor tidak mungkin 100%, walaupun tidak ada gesekan sama sekali?" "Pagi hari, ubin terasa lebih dingin daripada karpet. Apakah suhunya berbeda?"
- **Sumber:** OpenStax *University Physics Volume 2*.

## Fase 9 — Listrik, Magnet, dan Rangkaian

- **Konsep inti:** muatan dan hukum Coulomb; medan dan potensial listrik; kapasitor; arus, tegangan, hambatan, hukum Ohm; rangkaian seri dan paralel; hukum Kirchhoff (kekekalan muatan dan energi); daya listrik; medan magnet dan gaya Lorentz; induksi elektromagnetik (hukum Faraday dan Lenz); arus bolak-balik dan transformator (kualitatif).
- **Matematika prasyarat:** aljabar, sistem persamaan linear (Kirchhoff); jalur C: integral, perkalian silang, persamaan diferensial orde satu (rangkaian RC).
- **Eksperimen & simulasi:** **hanya baterai kecil (≤ 9 V)**: rangkaian senter dari baterai, kabel, dan LED dengan resistor; elektromagnet dari paku, kawat email, dan baterai (putus segera, kawat bisa panas); PhET *Circuit Construction Kit: DC*, *Ohm's Law*, *Faraday's Electromagnetic Lab*, *Charges and Fields*.
- **Kaitan rekayasa:** instalasi listrik rumah dan MCB, motor dan generator, transformator jaringan listrik, sensor, elektronika.
- **Tanda sudah menguasai:** "Dalam rangkaian satu lampu, apakah arus sebelum lampu lebih besar daripada sesudahnya?" (sama besar; muatan tidak habis, yang berpindah adalah energi). "Kenapa lampu di rumah dipasang paralel, bukan seri?"
- **Sumber:** OpenStax *University Physics Volume 2*; MIT OCW 8.02; Purcell & Morin, *Electricity and Magnetism* (jalur C lanjut).

## Fase 10 — Optik

- **Konsep inti:** model sinar; pemantulan; pembiasan dan hukum Snellius; pemantulan sempurna; lensa dan cermin (pembentukan bayangan); mata dan alat optik; model gelombang cahaya: interferensi, difraksi, polarisasi; spektrum elektromagnetik.
- **Matematika prasyarat:** geometri, trigonometri, persamaan lensa (pecahan).
- **Eksperimen & simulasi:** pensil "patah" di gelas air; kaca pembesar untuk memproyeksikan bayangan jendela ke dinding (ukur jarak fokus; jangan memfokuskan sinar Matahari ke kulit, mata, atau bahan mudah terbakar, lihat [Aturan Keselamatan](rules.md#aturan-keselamatan-eksperimen)); pola pelangi dari CD; PhET *Bending Light*, *Geometric Optics*.
- **Kaitan rekayasa:** serat optik internet, kamera ponsel, kacamata, panel surya.
- **Tanda sudah menguasai:** "Kenapa kolam renang tampak lebih dangkal dari aslinya?" "Kenapa serat optik bisa menyalurkan cahaya walau dibengkokkan?"
- **Sumber:** OpenStax *University Physics Volume 3*.

## Fase 11 — Pengantar Fisika Modern

- **Konsep inti:** batas fisika klasik; foton dan efek fotolistrik ($E = hf$); spektrum atom dan tingkat energi; dualisme gelombang–partikel; relativitas khusus (dilatasi waktu, $E = mc^2$) secara kualitatif; inti atom, peluruhan radioaktif, dan waktu paruh; semikonduktor (kualitatif).
- **Matematika prasyarat:** eksponen dan logaritma (peluruhan), notasi ilmiah; jalur C: fungsi eksponensial, aljabar kompleks dasar bila lanjut ke mekanika kuantum.
- **Eksperimen & simulasi:** amati spektrum lampu dengan CD sebagai kisi (lampu biasa, **jangan pernah mengarah ke Matahari**); simulasi peluruhan dengan melempar koin atau dadu berulang; PhET *Photoelectric Effect*, *Blackbody Spectrum*, *Models of the Hydrogen Atom*.
- **Kaitan rekayasa:** LED dan laser, panel surya, koreksi relativistik pada GPS, pencitraan medis, pembangkit nuklir.
- **Tanda sudah menguasai:** "Pada efek fotolistrik, kenapa menaikkan intensitas cahaya merah tidak membuat elektron lepas, sedangkan cahaya ultraviolet redup bisa?"
- **Sumber:** OpenStax *University Physics Volume 3*; Feynman Lectures Vol. III (lanjut).

---

## Konstanta yang Sering Dipakai

| Konstanta | Nilai | Catatan |
|---|---|---|
| Laju cahaya di vakum $c$ | 299 792 458 m/s | Nilai eksak dalam SI |
| Konstanta Planck $h$ | 6,626 070 15 × 10⁻³⁴ J·s | Nilai eksak sejak redefinisi SI 2019 |
| Muatan elementer $e$ | 1,602 176 634 × 10⁻¹⁹ C | Nilai eksak sejak 2019 |
| Konstanta Boltzmann $k_B$ | 1,380 649 × 10⁻²³ J/K | Nilai eksak sejak 2019 |
| Konstanta gravitasi $G$ | ≈ 6,674 × 10⁻¹¹ N·m²/kg² | Hasil pengukuran |
| Percepatan gravitasi standar $g_n$ | 9,806 65 m/s² | Nilai konvensi; $g$ lokal bervariasi kira-kira 9,78–9,83 m/s² |

Rujukan primer nilai konstanta: CODATA (NIST). Untuk soal sekolah, $g \approx 9{,}8$ m/s² atau 10 m/s² sesuai instruksi soal.

---

*Kembali ke [README Fisika](README.md) · Aturan mentor: [rules.md](rules.md)*
