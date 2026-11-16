# Roadmap Pembelajaran Computer Science (9 Subjek Fundamental)

Roadmap ini dirancang untuk membangun fondasi ilmu komputer yang kokoh dan menyentuh level rendah (*low-level systems*), mengacu pada kurikulum [TeachYourselfCS](https://teachyourselfcs.com/) yang disesuaikan dengan fokus menuju *Senior Backend Engineer* dan *DevOps / System Administration*.

> **Prinsip Inti:** Kurikulum = peta teori; folder `projects/` = laboratorium eksperimen nyata. Setiap topik penting dibuktikan melalui kode, pengukuran alat (*profiling/debugging*), dan pembangunan komponen dari nol sebelum mengandalkan abstraksi tinggi.

---

## 1. Dua Mode Belajar

| Mode | Kapan Digunakan | Prinsip |
|---|---|---|
| **Mode Kurikulum Penuh** (Default) | Belajar bertahap tanpa tenggat proyek ketat | Ikuti urutan fase prasyarat di bawah dengan kedalaman penuh dan kerjakan lab/proyek mini di `projects/`. |
| **Mode Fokus Proyek** | Saat sedang membangun proyek nyata di `projects/` | Pelajari konsep CS secara *just-in-time* sesuai kebutuhan proyek saat itu. Topik mendalam di luar fokus saat ini dicatat ke `[PARKIR]` untuk dipelajari setelah proyek selesai. |

---

## 2. Peta Urutan Fase & Prasyarat

> **Aturan Prasyarat:** Hormati ketergantungan antar subjek. Pahami *Computer Architecture* sebelum *Operating Systems* dan *Databases*; pahami *Networking* dan *Operating Systems* sebelum *Distributed Systems*.

| Fase | Subjek | Fokus Materi & Alat | Rujukan Utama | Ide Proyek / Lab Mandiri (`projects/`) |
|---|---|---|---|---|
| **0** | **Persiapan: C, Linux & Debugger** | Pointer, manajemen memori manual, *toolchain* kompilasi, `gdb`, `valgrind`, `strace`, perintah dasar Linux | Dokumentasi GNU/Linux, `man` pages, *The C Programming Language* (K&R) | Program kecil manipulasi memori di C; melacak *system call* dengan `strace` |
| **1** | **Programming** | Abstraksi fungsi, rekursi, *higher-order functions*, evaluasi ekspresi, paradigma pemrograman | *Structure and Interpretation of Computer Programs* (SICP) / *Composing Programs* | Implementasi *evaluator* ekspresi sederhana atau struktur data fungsional |
| **2** | **Computer Architecture** | Gerbang logika, representasi bilangan (IEEE 754, two's complement), *assembly*, hierarki memori & *CPU cache*, *layout struct* | *Nand2Tetris*, *Computer Systems: A Programmer's Perspective* (CS:APP) | Lab representasi bit & *profiling* performa *cache-friendly* vs *cache-miss* |
| **3** | **Algoritma & Struktur Data** | Kompleksitas waktu & ruang (Big-O), struktur data (hash table, tree, graph, heap), teknik desain algoritma | *The Algorithm Design Manual* (Skiena), *How to Solve It* | Mengimplementasikan struktur data inti (hash map, B-tree, graph traversal) dari nol |
| **4** | **Math for CS** | Logika diskrit, teori graf, kombinatorika, probabilitas, aritmatika modular, dasar aljabar linier | *Mathematics for Computer Science* (MIT 6.042J), seri video *Essence of Linear Algebra* (3Blue1Brown/Grant Sanderson); pendalaman opsional: *Introduction to Linear Algebra* (Gilbert Strang) / MIT 18.06 | Eksperimen algoritma kriptografi/hashing dasar dan pembuktian entropi |
| **5** | **Operating Systems** | Proses vs *thread* vs *goroutine*, *context switch*, *scheduling*, memori virtual & *paging*, *concurrency & locks*, *file descriptors*, *I/O* | *Operating Systems: Three Easy Pieces* (OSTEP), *xv6*, *Linux Kernel Development* | Membangun *mini shell* UNIX atau *custom memory allocator* sederhana di C |
| **6** | **Computer Networking** | Model TCP/IP, HTTP, DNS, TLS *handshake*, *socket programming*, *reverse proxy*, CORS, *wireshark/tcpdump* | *Computer Networking: A Top-Down Approach* (Kurose & Ross), Stanford CS 144 | Membangun *HTTP server* sederhana dari *raw TCP socket* |
| **7** | **Databases** | Arsitektur penyimpanan (*page & buffer pool*), indeks B-Tree, transaksi & ACID, *isolation levels*, MVCC, WAL, *query planner* (`EXPLAIN ANALYZE`) | Berkeley CS 186, *Architecture of a Database System*, PostgreSQL Docs, *Use The Index, Luke* | Membangun *mini key-value store* berbasis *append-only log* dan indeks |
| **8** | **Languages & Compilers** | *Lexing*, *parsing* (AST), *type checking*, *bytecode VM*, *garbage collection* | *Crafting Interpreters* (Robert Nystrom) | Membangun interpreter/parser kecil (misal *jlox* di Java atau interpreter Go) |
| **9** | **Distributed Systems & DevOps** | *Replication*, *partitioning*, konsensus (Raft/Paxos), *fault tolerance*, *observability* (metrics, logs, tracing), *systemd*, *backup & restore drill* | *Designing Data-Intensive Applications* (DDIA), MIT 6.5840 | Simulasi *leader election* sederhana atau *capstone* sistem terobservasi dengan *backup/DR* |

---

## 3. Pendekatan Level Rendah (*One Layer Below*)

Setiap kali menggunakan fitur tingkat tinggi di bahasa pemrograman atau infrastruktur, biasakan turun satu lapisan di bawahnya:
1. **Prediksi dulu, ukur kemudian:** Tulis hipotesis (output, penggunaan memori, jumlah *system call*, rencana eksekusi SQL) sebelum menjalankan program atau query.
2. **Alat Pengamat Wajib:** Biasakan memakai `gdb`, `objdump`, `strace`, `ltrace`, `perf`, `valgrind`, `tcpdump`/Wireshark, `ss`, `journalctl`, dan `EXPLAIN ANALYZE`.
3. **Bangun versi mini:** Membuat versi sederhana dari nol (*allocator*, *shell*, *HTTP server*, *key-value store*) jauh lebih efektif menanamkan mental model daripada sekadar memakai library jadi.

---

## 4. Ritme Belajar & Evaluasi Mandiri

### Pola Belajar Mingguan yang Disarankan
* **Eksplorasi Teori (Baca / Video):** Memahami konsep baru dari sumber rujukan utama.
* **Sesi Tutor Socratic:** Diskusi aktif untuk menguji pemahaman, mencari analogi, dan menelusuri lapisan di bawahnya (maksimal ~45 menit per sesi aktif).
* **Praktik & Lab (`projects/`):** Membangun kode eksperimen atau menguji hipotesis dengan alat observasi.
* **Uji Tanpa Bantuan AI (Mingguan / Akhir Fase):** Menjawab soal campuran konsep, prediksi perilaku sistem, dan skenario nyata tanpa bantuan AI, dinilai dengan skala **0–5**.
* **Spaced Repetition:** Mengulang kembali topik yang pernah salah pada interval **1 hari, 3 hari, 7 hari, 14 hari, dan 30 hari**.

### Uji Masuk & Uji Akhir Fase
* **Uji Masuk Fase:** Sebelum memulai fase baru, kerjakan 10 soal tanpa AI. Jika skor $\ge 4$ dari 5, fase tersebut dapat dipadatkan agar fokus pada celah yang tersisa saja.
* **Uji Akhir Fase:** Setelah menyelesaikan satu fase, kerjakan minimal 10 soal campuran konsep, prediksi perilaku, dan skenario implementasi sebelum melangkah ke fase berikutnya.

---

## 5. Pencatatan Progres & Keputusan
* Simpan ringkasan bab, hasil kuis, dan log sesi di `notes/` menggunakan template [../../templates/template-learning-log.md](../../templates/template-learning-log.md).
* Simpan catatan keputusan desain saat bereksperimen di proyek menggunakan [../../templates/template-decision-record.md](../../templates/template-decision-record.md).
