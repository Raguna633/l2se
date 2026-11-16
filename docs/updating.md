# Memperbarui Framework

*Framework* ini terus diperbaiki. Panduan ini menjelaskan cara menarik pembaruan ke repositori belajar Anda tanpa menimpa catatan pribadi.

## Prinsip: Zona Framework vs Zona Pengguna

| Zona | Berkas | Saat memperbarui |
|---|---|---|
| **Framework** | `AGENTS.md`, `CLAUDE.md`, `templates/`, `docs/`, `rules*.md`, `SKILL.md`, `.github/`, `scripts/` | Ambil versi terbaru dari *upstream*. |
| **Paket topik bawaan** | `rules*.md`, `SKILL.md`, dan `roadmap.md` pada topik bawaan | Ikut diperbarui seperti Zona Framework. |
| **README topik bawaan** | `README.md` pada topik bawaan | Diperbarui *upstream*, tetapi boleh Anda sesuaikan (`"sesuaikan topik"`). Bila sudah disesuaikan, konflik saat pembaruan wajar; pertahankan bagian milik Anda (mis. *Project Showcase*). |
| **Pengguna** | `LEARNER.md`, isi `notes/` (*upstream* hanya mengirim templat kosong awal), `projects/`, topik buatan Anda | Tidak pernah disentuh *upstream*. |

Jika Anda mengubah berkas di Zona Framework, konflik saat pembaruan menjadi wajar. Sebaiknya usulkan perubahan itu ke *upstream* lewat *pull request*.

Baca [CHANGELOG.md](../CHANGELOG.md) sebelum memperbarui untuk melihat apa yang berubah.

---

## Cara 1 — Repositori dari "Use this template"

Repositori hasil *template* tidak berbagi riwayat Git dengan *upstream*. Pembaruan pertama memerlukan satu opsi tambahan:

```bash
git remote add upstream https://github.com/Raguna633/l2se.git
git fetch upstream
git merge upstream/main --allow-unrelated-histories
```

Selesaikan konflik (umumnya hanya di Zona Framework), lalu *commit*. Pembaruan berikutnya cukup:

```bash
git fetch upstream
git merge upstream/main
```

## Cara 2 — Repositori hasil *clone* (Jalur C)

Riwayatnya sudah tersambung, jadi cukup:

```bash
git fetch upstream
git merge upstream/main
```

## Cara 3 — Tanpa Git (Jalur A)

Unduh ZIP versi terbaru, lalu salin hanya berkas Zona Framework ke folder Anda. Jangan menimpa `LEARNER.md` dan folder `notes/` milik Anda.

## Berkas yang Boleh Dihapus di Repositori Pribadi

Berkas berikut berguna untuk pengembangan *framework*, tetapi tidak wajib di repositori belajar pribadi: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `.github/ISSUE_TEMPLATE/`, dan `.github/PULL_REQUEST_TEMPLATE.md`. Workflow `.github/workflows/check-docs.yml` hanya berjalan di repositori utama L2SE, jadi aman dibiarkan. Menghapus berkas-berkas ini dapat menimbulkan konflik kecil saat menarik pembaruan; pilih "hapus" saat menyelesaikannya.
