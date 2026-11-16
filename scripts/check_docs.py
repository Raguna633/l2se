#!/usr/bin/env python3
"""Pemeriksa kualitas dokumen framework.

Memeriksa:
1. Tautan relatif Markdown (termasuk anchor dan tautan gaya referensi) mengarah ke berkas/heading yang ada.
2. Berkas aturan AI (AGENTS.md, rules*.md, SKILL.md) tidak melebihi batas ukuran.
3. Blok PROTOKOL-BERSAMA identik di semua berkas mentor.

Jalankan dari root repositori:  python scripts/check_docs.py
Tidak memerlukan dependensi di luar Python standar (3.8+).
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SIZE_LIMIT = 24_000  # byte; batas berkas aturan di beberapa platform (mis. Antigravity)
SKIP_DIRS = {".git", "node_modules", "projects"}
# Berkas Zona Pengguna yang boleh belum ada di repositori framework.
OPTIONAL_TARGETS = {"LEARNER.md"}
PROTOCOL_FILES = [
    "engineering/software/go/rules.md",
    "engineering/software/react/rules.md",
    "technology/computer-science/tutor/SKILL.md",
]
LINK_RE = re.compile(r"\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
REF_USE_RE = re.compile(r"\[[^\]]+\]\[([^\]]*)\]")
REF_DEF_RE = re.compile(r"^\s{0,3}\[([^\]]+)\]:\s*<?(\S+?)>?(?:\s+\"[^\"]*\")?\s*$", re.M)
FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$", re.M)
# Tautan relatif khusus GitHub (mis. ../../issues) yang sengaja keluar dari root.
GITHUB_RELATIVE_RE = re.compile(r"^(\.\./)+(issues|pulls|discussions|wiki|releases|actions)(/|$)")


def markdown_files():
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        yield path


def strip_code(text):
    return INLINE_CODE_RE.sub("", FENCE_RE.sub("", text))


def github_slug(heading):
    """Perkiraan aturan anchor GitHub: huruf kecil, buang tanda baca, spasi -> '-'."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)  # teks tautan saja
    text = text.replace("`", "").lower()
    text = "".join(c for c in text if c.isalnum() or c in " -_")
    return text.replace(" ", "-")


_anchor_cache = {}


def anchors_of(path):
    if path not in _anchor_cache:
        text = FENCE_RE.sub("", path.read_text(encoding="utf-8"))
        seen, slugs = {}, set()
        for heading in HEADING_RE.findall(text):
            base = github_slug(heading)
            n = seen.get(base, 0)
            slugs.add(base if n == 0 else f"{base}-{n}")
            seen[base] = n + 1
        _anchor_cache[path] = slugs
    return _anchor_cache[path]


def check_target(path, target, errors):
    where = path.relative_to(ROOT)
    if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
        return  # URL eksternal atau mailto:
    if GITHUB_RELATIVE_RE.match(target):
        return
    file_part, _, anchor = target.partition("#")
    resolved = (path.parent / file_part).resolve() if file_part else path
    try:
        inside = resolved.relative_to(ROOT)
    except ValueError:
        errors.append(f"Tautan keluar dari repositori: {where} -> {target}")
        return
    if inside.name in OPTIONAL_TARGETS:
        return
    if not resolved.exists():
        errors.append(f"Tautan rusak: {where} -> {target}")
        return
    if anchor and resolved.suffix == ".md" and anchor.lower() not in anchors_of(resolved):
        errors.append(f"Anchor tidak ditemukan: {where} -> {target}")


def check_links(errors):
    for path in markdown_files():
        text = strip_code(path.read_text(encoding="utf-8"))
        for target in LINK_RE.findall(text):
            check_target(path, target, errors)
        definitions = {k.lower(): v for k, v in REF_DEF_RE.findall(text)}
        for ref, target in definitions.items():
            check_target(path, target, errors)
        for ref in REF_USE_RE.findall(text):
            if ref and ref.lower() not in definitions:
                errors.append(f"Referensi tautan tanpa definisi: {path.relative_to(ROOT)} -> [{ref}]")


def check_sizes(errors):
    for path in markdown_files():
        name = path.name
        if name == "AGENTS.md" or name == "SKILL.md" or name.startswith("rules"):
            size = path.stat().st_size
            if size > SIZE_LIMIT:
                errors.append(
                    f"Terlalu besar: {path.relative_to(ROOT)} ({size} byte > {SIZE_LIMIT}). "
                    "Pecah menjadi beberapa bagian yang saling menaut."
                )


def check_protocol(errors):
    blocks = {}
    for rel in PROTOCOL_FILES:
        text = (ROOT / rel).read_text(encoding="utf-8")
        match = re.search(r"<!-- PROTOKOL-BERSAMA:BEGIN.*?<!-- PROTOKOL-BERSAMA:END -->", text, re.S)
        if not match:
            errors.append(f"Blok PROTOKOL-BERSAMA tidak ditemukan di {rel}")
            continue
        blocks[rel] = match.group(0)
    if len(set(blocks.values())) > 1:
        errors.append("Blok PROTOKOL-BERSAMA tidak identik di: " + ", ".join(blocks))


def main():
    errors = []
    check_links(errors)
    check_sizes(errors)
    check_protocol(errors)
    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} masalah ditemukan.")
        return 1
    count = sum(1 for _ in markdown_files())
    print(f"OK: {count} berkas Markdown, tautan valid, ukuran aman, protokol sinkron.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
