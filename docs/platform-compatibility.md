# Kompatibilitas Platform

Semua aturan mentor bersumber dari satu berkas: [`AGENTS.md`](../AGENTS.md). Platform berbeda memuat berkas itu dengan cara berbeda. Tabel ini memisahkan dengan jujur antara yang **sudah diuji** dan yang **baru berdasarkan dokumentasi platform**.

| Platform | Cara memuat aturan | Status |
|---|---|---|
| **Antigravity** | Membaca `AGENTS.md` dan skill di `.agents/skills.json` secara otomatis. | ✅ Diuji oleh pembuat |
| **Claude Code** | Membaca `CLAUDE.md`, yang mengimpor `AGENTS.md` lewat baris `@AGENTS.md`. | ✅ Diuji oleh pembuat |
| **OpenAI Codex** | Membaca `AGENTS.md` di *root* secara otomatis. | ⚠️ Menurut dokumentasi, belum diuji |
| **Cursor** | Mendukung `AGENTS.md` di *root* sebagai aturan proyek. | ⚠️ Menurut dokumentasi, belum diuji |
| **GitHub Copilot** | Mendukung `AGENTS.md` (Copilot *coding agent*; di VS Code dapat memerlukan pengaturan agar `AGENTS.md` dipakai di chat). | ⚠️ Menurut dokumentasi, belum diuji |
| **Windsurf** | Mendukung `AGENTS.md` sebagai aturan proyek. | ⚠️ Menurut dokumentasi, belum diuji |
| **Gemini CLI** | Secara bawaan membaca `GEMINI.md`. Arahkan ke `AGENTS.md` lewat konfigurasi (lihat di bawah). | ⚠️ Perlu konfigurasi, belum diuji |
| **Claude / ChatGPT Projects, Gemini Gems** | Tempel `AGENTS.md` sebagai instruksi dan unggah berkas pendukung (lihat [getting-started.md](getting-started.md), Jalur A). Tidak dapat menulis berkas. | ⚠️ Manual, belum diuji |

> Platform AI berubah cepat. Bila suatu cara tidak lagi berlaku, mohon laporkan lewat *issue* agar tabel ini diperbarui.

---

## Catatan per Platform

### Gemini CLI
Tambahkan berkas `.gemini/settings.json` di *root* repositori Anda:

```json
{
  "context": {
    "fileName": ["AGENTS.md"]
  }
}
```

Periksa dokumentasi resmi Gemini CLI untuk format terbaru karena nama kunci konfigurasinya pernah berubah.

### Mengapa tidak ada `GEMINI.md` atau `.cursorrules`?
Menyalin aturan ke banyak berkas membuat isinya mudah tidak sinkron. Selama platform dapat diarahkan ke `AGENTS.md`, *framework* ini mempertahankan satu sumber kebenaran.

---

## Batas Ukuran Berkas

Beberapa platform memotong berkas aturan yang terlalu besar (Antigravity membatasi sekitar 24.000 byte per berkas aturan). Karena itu berkas panduan besar dipecah menjadi beberapa bagian yang saling menaut, dan CI memeriksa agar setiap berkas aturan tetap di bawah batas tersebut.

## Cara Menguji Platform Baru

1. Buka repositori di platform tersebut tanpa `LEARNER.md`.
2. Kirim pesan "halo". Mentor yang memuat aturan dengan benar akan menyapa dan menawarkan `"atur profil saya"`.
3. Ketik `"mulai sesi belajar [topik]"`. Mentor seharusnya memulai dengan pertanyaan pemanasan, satu per pesan.
4. Laporkan hasilnya lewat *issue* dengan template **Laporan Uji Platform**.
