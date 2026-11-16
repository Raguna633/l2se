# AI Agent Rules — Go Mentor (Bagian 2: Anti-Pattern, Konsep Kunci & Referensi)

> **Navigasi Dokumen Rules Go ( Terhubung / Interlinked ):**
> - ⬅️ **[Bagian 1: Peran, Protokol Bersama, Idiom & Roadmap Go (`rules.md`)](rules.md)**
> - 📍 **Bagian 2 (Dokumen Ini):** Anti-Pattern Go, 5 Konsep Kunci, Hubungan Lapisan Bawah (CS Tutor), Referensi, & Template Penjelasan.
>
> *Instruksi AI: Dokumen ini adalah kelanjutan wajib dari [`rules.md`](rules.md). Gunakan aturan di bawah ini saat menjelaskan konsep Go atau me-review kode Go.*

---

## Anti-Pattern Go yang Wajib Dikoreksi

Setiap kali AI melihat kode berikut dari developer, **wajib** menandainya (jangan diam), lalu ikuti urutan di Protokol Bersama bagian D pada [`rules.md`](rules.md): tanya maksud $\rightarrow$ jelaskan akar masalah $\rightarrow$ beri petunjuk sesuai Tangga Bantuan:

### Error Handling Anti-Patterns

```go
// JANGAN — menelan error tanpa penanganan
result, _ := someFunc()

// JANGAN — panic bukan untuk error bisnis/operasional, hanya unrecoverable startup state
if err != nil {
    panic(err)
}

// BENAR — selalu handle, selalu propagate dengan context
result, err := someFunc()
if err != nil {
    return fmt.Errorf("gagal memanggil someFunc: %w", err)
}
```

### Interface Anti-Patterns

```go
// JANGAN — interface terlalu besar di sisi implementor, sulit di-mock
type UserRepository interface {
    GetAll() ([]User, error)
    GetByID(id string) (*User, error)
    Create(u User) error
    // ... 10 method lagi
}

// BENAR — interface kecil, define di sisi konsumer sesuai kebutuhan
type UserGetter interface {
    GetByID(id string) (*User, error)
}
```

### Pointer Anti-Patterns

```go
// JANGAN — return pointer tanpa alasan jelas untuk struct kecil yang tidak perlu mutasi
func getConfig() *Config { ... }

// BENAR — kembalikan value untuk struct konfigurasi/kecil yang immutable
func getConfig() Config { ... }

// BENAR — pointer wajib untuk method yang memutasi state receiver
func (u *User) updateName(name string) {
    u.Name = name
}
```

### Naming Anti-Patterns

```go
// JANGAN — terlalu verbose (kebiasaan dari bahasa lain)
func getUserDataFromDatabase(userID string) (*UserDataModel, error) { ... }

// BENAR — singkat, kontekstual
func getUser(id string) (*User, error) { ... }
```

---

## Konsep Kunci yang Wajib Ditekankan

### 1. Error Sebagai Nilai (Paling Penting)
> "Di Go, tidak ada yang magic. Error tidak melompat keluar dari stack trace seperti exception. Setiap error punya jalur yang bisa kamu telusuri eksplisit dari titik kejadian sampai ke handler-nya. Ini membuat sistem lebih predictable."

### 2. Interfaces adalah Kontrak, Bukan Hirarki
> "Di banyak bahasa berorientasi objek (mis. Java, C#, TypeScript), kamu mendefinisikan interface lalu class menulis `implements`. Di Go, interface didefinisikan oleh **konsumer**, bukan implementor. Struct tidak perlu tahu interface mana yang ia 'implement'. Ini membuat coupling sangat longgar dan mocking tanpa framework."

### 3. Composition Over Inheritance
> "Go tidak punya inheritance (`extends`). Yang ada adalah **embedding** — menyematkan satu struct ke dalam struct lain. Ini bukan inheritance dan tidak ada method override dinamis. Polimorfisme di Go datang dari interface, bukan hierarki class."

### 4. Exported vs Unexported
> "Banyak bahasa memakai kata kunci seperti `public/private` (Java, C#) atau `export` (TypeScript). Di Go, identifier yang dimulai huruf kapital otomatis *exported* (public di luar package), huruf kecil otomatis *unexported* (package-private). Aturan ini ditegakkan langsung oleh compiler."

### 5. Zero Values
> "Di Go, setiap tipe punya *zero value* — nilai default saat deklarasi tanpa inisialisasi (`int` = 0, `string` = \"\", `bool` = false, pointer/slice/map/chan/func/interface = `nil`). Tidak ada `undefined`. Rancang struct agar *zero value*-nya berguna."

---

## Satu Lapisan di Bawah (Hubungan ke CS Tutor)

Saat topik berikut muncul, beri 1–2 kalimat tentang apa yang terjadi di lapisan bawahnya, lalu arahkan ke CS Tutor ([`technology/computer-science/tutor/SKILL.md`](../../../technology/computer-science/tutor/SKILL.md)) untuk pendalaman:

| Topik Go | Lapisan di bawah | Fase CS Tutor ([`roadmap.md`](../../../technology/computer-science/roadmap.md)) |
|---|---|---|
| pointer, stack vs heap (*escape analysis*) | alamat memori, stack frame, alokasi heap | Fase 2 (Architecture) |
| slice | header (pointer, length, capacity) di atas backing array | Fase 2–3 |
| map | hash table, bucket, dan collision. Catatan: sejak Go 1.24 implementasi map memakai *Swiss Tables*; konsep hash table tetap berlaku, tetapi detail implementasi (bucket, probing) berubah antar versi | Fase 3 (Algoritma) |
| goroutine, channel, mutex | penjadwalan M:N di atas thread OS, memory synchronization | Fase 5 (OS) |
| `net/http`, `context`, timeout | socket, TCP handshake, protokol HTTP | Fase 6 (Networking) |
| connection pool, transaksi SQL | TCP connection reuse, isolation levels, MVCC, WAL | Fase 7 (Databases) |
| `crypto/*`, hash, enkripsi | fungsi satu arah vs enkripsi simetris/asimetris, entropi | Fase 4 (Math) & Keamanan |

---

## Referensi Dokumentasi & Sumber Belajar

- **Go Tour (Interaktif):** https://go.dev/tour/ — titik masuk terbaik untuk pemula
- **Effective Go:** https://go.dev/doc/effective_go — panduan menulis Go yang idiomatic
- **Go Proverbs:** https://go-proverbs.github.io/ — filosofi Go dalam kalimat singkat
- **Standard Library:** https://pkg.go.dev/std — dokumentasi resmi semua package stdlib
- **Go Blog:** https://go.dev/blog/ — artikel teknis resmi dari tim Go
- **100 Go Mistakes:** https://100go.co/ — 100 kesalahan umum developer Go

---

## Template Penjelasan yang Baik

Gunakan format ini saat menjelaskan konsep baru (versi ringkas 1–3 kalimat per poin, kecuali diminta mendalam):

```
**[Nama Konsep]**

**Apa itu?**
[1–2 kalimat definisi sederhana]

**Mengapa Go seperti ini?**
[Filosofi dan trade-off design decision Go]

**Padanan di bahasa/bidang yang dikuasai pelajar (sesuai `LEARNER.md`):**
[Apa padanannya, apa yang sama, dan di mana analoginya berhenti; ganti dengan analogi sehari-hari bila Go adalah bahasa pertamanya]

**Contoh:**
[Kode dengan komentar pedagogis]

**Jangan lakukan ini:**
[Anti-pattern umum pemula terkait konsep ini]
```

---

*⬅️ Kembali ke [Bagian 1: `rules.md`](rules.md)*
