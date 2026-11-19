# L2SE — Learner to Systems Engineer

[![Check docs](https://github.com/Raguna633/l2se/actions/workflows/check-docs.yml/badge.svg)](https://github.com/Raguna633/l2se/actions/workflows/check-docs.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) ![Status: beta](https://img.shields.io/badge/status-beta%20v0.2.0-orange)

🇮🇩 **Dokumentasi Utama (Bahasa Indonesia):** [README.md](README.md)

**An open-source, Markdown + Git framework that turns your favorite AI agent into a personalized, first-principles STEM mentor.**

> **Language Support:** Although the repository documentation is written in Indonesian (with technical and engineering terms preserved in English), **L2SE works in any language**. Simply set your preferred language (e.g., `English`) during onboarding or in `LEARNER.md`, and the AI Mentor will conduct all sessions, explanations, and quizzes in your language.

---

## 🎯 Why L2SE?

Standard AI chatbots tend to act as instant answer machines—encouraging passive copying (*"vibe learning"*) while ignoring the learner's background, mathematical maturity, and academic integrity.

**L2SE** implements the **TPACK (*Technological Pedagogical Content Knowledge*)** framework (Mishra & Koehler, 2006) and **George Pólya's problem-solving method** (1945) directly inside an agent-native workspace ([AGENTS.md](AGENTS.md)):

| Pillar | How L2SE Implements It |
|---|---|
| **First Principles Over Memorization** | Guides you to derive formulas, predict outcomes before running experiments/code, and perform dimensional & Fermi sanity checks ([docs/stem-pedagogy.md](docs/stem-pedagogy.md)). |
| **Mandatory Context & Progressive Profiling** | Never teaches blindly. Requires a 3-question mini-profile (~30s) or full onboarding (`"atur profil saya"`) stored in `LEARNER.md`, enriched proactively across sessions. |
| **4-Level Scaffolding Ladder (L1–L4)** | **L1** Guiding Question → **L2** Concept Hint → **L3** Separate Example → **L4** Solution Draft (unlocked only after you show an attempt and explicitly request it). |
| **Canonical Academic Integrity & Safety** | Never solves graded homework, live exams, or active competitions; enforces lab and experiment safety rules. |
| **Proactive Memory & Mistake Taxonomy** | Automatically tracks mastered concepts, spaced-repetition schedules (1, 3, 7, 14, 30 days), and classifies misconceptions into `[KONSEP]` (conceptual), `[MODEL]` (modeling), and `[EKSEKUSI]` (execution) in `notes/learning-log.md`. |
| **Built for 5 Personas** | Adapts tone and depth for **School Students**, **University Students**, **Engineers**, **Teachers/Lecturers** (lesson plans & rubric-based question banks), and **General Learners**. |
| **Cross-Platform & Zero Infrastructure** | Pure Markdown + Git. Works with **Claude Code, Antigravity, Cursor, Windsurf, GitHub Copilot, OpenAI Codex, Gemini CLI**, and web chat apps (**Claude Projects, ChatGPT Projects, Gemini Gems**). |

---

## 🚀 Quick Start in 3 Steps

### Path A — No Coding Required (Claude / ChatGPT Projects / Gemini Gems)
1. Click **Code → Download ZIP** on GitHub and extract it.
2. Create a *Project* (Claude/ChatGPT) or *Gem* (Gemini), paste [AGENTS.md](AGENTS.md) as the custom instructions, and upload [docs/stem-pedagogy.md](docs/stem-pedagogy.md), [templates/template-learner.md](templates/template-learner.md), plus the files for your chosen topic.
3. Start chatting! Ask to learn any topic (or type `"atur profil saya"` in Indonesian / *"set up my learner profile — I prefer English"*).

### Path B — AI IDE / Coding Agents (Antigravity, Claude Code, Cursor, Copilot, Codex)
1. Click **Use this template → Create a new repository** on GitHub (public for portfolio showcase, or private), then clone it locally.
2. Open the **repository root folder** in your AI IDE (or invoke `/l2se-mentor` / `/cs-tutor` in IDEs that support `.agents/skills/`).
3. Start learning! The mentor will ask 3 quick context questions (or run full onboarding), create `LEARNER.md`, and tailor every session to your background.

---

## 📚 Included Topic Packs

| Domain | Topic | Files & Mentor Rules |
|---|---|---|
| **M — Mathematics** | Foundations (School → University → Engineering/CS, 11 phases) | [README](mathematics/foundations/README.md) · [Roadmap](mathematics/foundations/roadmap.md) · [Rules Part 1](mathematics/foundations/rules.md) · [Part 2 (±35 Misconceptions & Rubrics)](mathematics/foundations/rules-misconceptions-and-assessment.md) |
| **S — Science** | Physics (Phenomena → High School → University → Engineering, 12 phases) | [README](science/physics/README.md) · [Roadmap](science/physics/roadmap.md) · [Rules Part 1](science/physics/rules.md) · [Part 2 (Experiments, PhET & Misconceptions)](science/physics/rules-misconceptions-and-experiments.md) |
| **T — Technology** | Computer Science (9 Core Subjects & Low-Level Systems) | [README](technology/computer-science/README.md) · [Roadmap](technology/computer-science/roadmap.md) · [CS Tutor Skill](technology/computer-science/tutor/SKILL.md) |
| **E — Engineering** | Software Engineering: Backend (Go), Frontend (React & TS), Mobile Web UI/UX | [Go](engineering/software/go/README.md) · [React](engineering/software/react/README.md) · [Mobile UI/UX](engineering/software/ui-ux-mobile/README.md) |
| **Languages for STEM** | English for STEM & Japanese for STEM (e.g., MEXT Scholarship prep) | [English](languages/english/README.md) ([Roadmap](languages/english/roadmap.md)) · [Japanese](languages/japanese/README.md) ([Roadmap](languages/japanese/roadmap.md)) |

---

## 🤝 Contributing & License

- Run `python scripts/check_docs.py` (Python 3.8+, zero external dependencies) to validate links, anchors, rule file sizes (< 24,000 bytes), and shared protocol synchronization.
- Released under the [MIT License](LICENSE). See [CITATION.cff](CITATION.cff) to cite L2SE in academic work or educational materials.
