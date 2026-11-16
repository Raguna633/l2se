# Go (Golang) Backend Engineering

Pusat pembelajaran bahasa Go untuk pengembangan backend yang andal, berkinerja tinggi, dan konkurensi aman. AI Mentor menjembatani materi dari latar belakang yang tertulis di `LEARNER.md` (mis. bahasa pemrograman lain yang sudah dikuasai), atau mengajarkannya dari nol bila Go adalah bahasa pertama Anda.

---

## 1. Fokus & Mental Model Go
* **Simplicity & Explicit**: Tanpa exception tersembunyi; error diperlakukan sebagai nilai biasa (*value*).
* **Composition over Inheritance**: Struct embedding dan implementasi interface secara implisit.
* **Concurrency**: Goroutine dan channel yang dijadwalkan oleh Go runtime di atas thread OS.
* **Memory & Performance**: Pointer terprediksi, stack vs heap (*escape analysis*), dan garbage collection berlatensi rendah.

---

## 2. AI Mentor Rules (Terhubung / Interlinked)
Panduan operasional untuk AI Agent sebagai *Go Mentor* (Senior Backend Developer) dibagi ke dalam dua dokumen yang saling terhubung agar konten tetap utuh dan optimal:
1. 👉 **[Bagian 1: `rules.md`](rules.md)** — Protokol Bersama, Peran, Prinsip Utama, Idiom & Arsitektur Go, serta Urutan Belajar (Tahap 1–5).
2. 👉 **[Bagian 2: `rules-concepts-and-antipatterns.md`](rules-concepts-and-antipatterns.md)** — Anti-Pattern Go, 5 Konsep Kunci, Tabel Hubungan Lapisan Bawah (CS Tutor), Referensi, & Template Penjelasan.

---

## 3. Silabus & Rujukan
* **Dasar**: [A Tour of Go](https://go.dev/tour/), [Effective Go](https://go.dev/doc/effective_go)
* **Web & Routing**: `net/http`, router idiomatik (seperti `chi`)
* **Database**: `database/sql` & driver modern (seperti `pgx`)
* **Testing & Tools**: Table-driven tests, `log/slog`, `pprof`, `go vet`, race detector (`-race`)

---

## 4. Project Showcase (*Multi-Repo*)
Proyek nyata Go dikelola di repositori GitHub mandiri agar repositori pembelajaran ini tetap ringan, dan ditautkan di tabel ini sebagai etalase portofolio:

| Nama Proyek | Deskripsi Singkat | Stack | Repositori | Status |
|---|---|---|---|---|
| *(Belum ada)* | — | — | — | — |

---

## 5. Struktur Direktori
```text
go/
├── README.md                            # Dokumen ini
├── rules.md                             # Aturan AI Go Mentor (Bagian 1)
├── rules-concepts-and-antipatterns.md   # Aturan AI Go Mentor (Bagian 2)
├── notes/                               # learning-log.md, glossary.md, catatan konsep
└── projects/                            # Proyek latihan nyata Go (CLI tools, REST API, concurrency playground)
```

Catatan belajar: [learning-log](notes/learning-log.md) · [glosarium](notes/glossary.md)
