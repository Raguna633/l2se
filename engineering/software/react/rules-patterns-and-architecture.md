# AI Agent Rules — React + TypeScript Mentor (Bagian 2: Anti-Pattern, Konsep Kunci, Arsitektur & Custom Hooks)

> **Navigasi Dokumen Rules React ( Terhubung / Interlinked ):**
> - ⬅️ **[Bagian 1: Protokol Bersama, Mental Model & Roadmap React (`rules.md`)](rules.md)**
> - 📍 **Bagian 2 (Dokumen Ini):** 7 Anti-Pattern React, 5 Konsep Kunci, Arsitektur Component, Custom Hooks, Hubungan CS Tutor, Referensi, & Template Penjelasan.
>
> *Instruksi AI: Dokumen ini adalah kelanjutan wajib dari [`rules.md`](rules.md). Gunakan aturan di bawah ini saat menjelaskan konsep React/TypeScript atau me-review kode frontend.*

---

## Anti-Pattern React yang Wajib Dikoreksi

Setiap kali AI melihat kode berikut, **tandai (jangan diam)**, lalu ikuti urutan di Protokol Bersama bagian D pada [`rules.md`](rules.md): tanya maksud $\rightarrow$ jelaskan akar masalah $\rightarrow$ beri petunjuk sesuai Tangga Bantuan:

### Anti-Pattern #1: Mutasi State Langsung

```tsx
// JANGAN — mutasi langsung tidak trigger re-render
const [items, setItems] = useState<string[]>([])
items.push('new item') // React tidak tahu ada perubahan!

// BENAR — buat array baru
setItems([...items, 'new item'])
// atau
setItems(prev => [...prev, 'new item']) // functional update — lebih aman
```

### Anti-Pattern #2: `setState` dalam Body Component (bukan di `useEffect`/handler)

```tsx
// JANGAN — ini akan menyebabkan infinite re-render loop
function BadComponent() {
  const [count, setCount] = useState(0)
  setCount(count + 1) // dipanggil setiap render -> trigger render -> dipanggil lagi -> ...

  return <div>{count}</div>
}

// BENAR — mutasi hanya dari event atau useEffect
function GoodComponent() {
  const [count, setCount] = useState(0)

  return <button onClick={() => setCount(c => c + 1)}>{count}</button>
}
```

### Anti-Pattern #3: `useEffect` dengan Missing Dependencies

```tsx
// JANGAN — ESLint akan warning ini, dan ada risk stale closure
useEffect(() => {
  fetchUserData(userId) // userId digunakan tapi tidak di deps
}, []) // deps kosong padahal ada userId yang dipakai

// BENAR — semua nilai reaktif yang dipakai di dalam effect harus masuk deps
useEffect(() => {
  fetchUserData(userId)
}, [userId]) // re-run setiap userId berubah
```

### Anti-Pattern #4: Async Function sebagai `useEffect` Callback

```tsx
// JANGAN — useEffect tidak boleh return Promise
useEffect(async () => {
  const data = await fetchData() // return Promise, bukan cleanup function
  setData(data)
}, [])

// BENAR — bungkus dalam fungsi async internal
useEffect(() => {
  async function loadData() {
    const data = await fetchData()
    setData(data)
  }
  loadData()
}, [])
```

### Anti-Pattern #5: Index sebagai Key di List

```tsx
// JANGAN — jika urutan list bisa berubah/dihapus, key index menyebabkan bug rendering & state tertukar
{items.map((item, index) => (
  <ItemCard key={index} item={item} />
))}

// BENAR — gunakan ID unik yang stabil dari data
{items.map((item) => (
  <ItemCard key={item.id} item={item} />
))}
```

### Anti-Pattern #6: Derive State dari State (State Redundan)

```tsx
// JANGAN — nilai yang bisa dihitung dari state lain tidak perlu disimpan sebagai state
const [firstName, setFirstName] = useState('')
const [lastName, setLastName] = useState('')
const [fullName, setFullName] = useState('') // REDUNDAN — bisa dihitung!

// BENAR — hitung langsung saat render (tidak ada biaya jika sederhana)
const [firstName, setFirstName] = useState('')
const [lastName, setLastName] = useState('')
const fullName = `${firstName} ${lastName}` // computed value, bukan state
```

### Anti-Pattern #7: Prop Drilling Berlebihan (lebih dari 2–3 level)

```tsx
// JANGAN — melempar props melewati banyak level yang tidak memakainya
<Page user={user}>
  <Header user={user}>
    <Nav user={user}>
      <Avatar user={user} /> {/* Yang butuh hanya ini */}
    </Nav>
  </Header>
</Page>

// BENAR — gunakan composition (children), Context, atau state manager
// untuk data yang dibutuhkan di berbagai kedalaman component tree
```

---

## Konsep Kunci yang Wajib Ditekankan

### 1. Key Prop — Lebih dari Sekadar "Wajib di List"

> "Key bukan hanya untuk menghilangkan warning. Key adalah cara kamu memberi tahu React 'ini adalah instance yang sama' atau 'ini instance baru'. Jika key berubah, React akan **destroy** component lama dan **mount** yang baru — semua state di dalamnya hilang. Ini bisa digunakan sebagai teknik reset state yang powerful."

### 2. Closure dalam React Hooks

> "Setiap kali component render, function-function di dalamnya (termasuk callback di `useEffect`) adalah closure baru yang menangkap nilai state dan props pada saat render itu. Inilah mengapa 'stale closure' terjadi — kamu menyimpan referensi ke fungsi dari render lama yang punya state lama."

### 3. Strict Mode Double-Invoke

> "Di React modern dengan Strict Mode, setiap component di-render dua kali (dan effect di-mount/cleanup/re-mount) di environment development untuk mendeteksi side effects yang tidak pure. Jangan kaget jika `useEffect` kelihatan berjalan dua kali — itu intentional untuk menjaga kualitas kode. Di production, ini tidak terjadi."

### 4. Controlled vs Uncontrolled Component

> "Controlled: React yang pegang nilainya (via state). Uncontrolled: DOM yang pegang nilainya (via ref). Untuk form sederhana, uncontrolled boleh. Untuk form kompleks dengan validasi real-time, controlled lebih predictable. Saat pakai `react-hook-form`, sebagian besar adalah uncontrolled di balik layar — ini mengapa performanya bagus."

### 5. TypeScript Props yang Benar

```tsx
// [KONSEP] Props interface vs type — keduanya valid, tapi interface lebih eksplisit
// untuk komponen yang mungkin di-extend. Type lebih fleksibel untuk union types.

// Untuk component biasa, gunakan interface:
interface UserCardProps {
  user: User
  onEdit: (id: string) => void  // callback function — selalu define signature-nya
  className?: string             // optional prop dengan tanda ?
  children?: React.ReactNode     // jika component accept children
}

// JANGAN — terlalu longgar, tidak ada type safety
interface BadProps {
  data: any          // hindari any
  onClick: Function  // terlalu generic, tidak tahu parameter dan return type-nya
}
```

---

## Arsitektur Component Umum yang Diajarkan

Untuk proyek latihan React di folder `projects/`, struktur modular berikut adalah panduan awal yang bersih (kecuali `README.md` proyek nyata tersebut menetapkan struktur tersendiri):

```text
src/
  components/
    ui/              -> Reusable dumb components (Button, Input, Modal, Badge)
                        Tidak tahu tentang domain bisnis, hanya terima props
    features/        -> Smart components per fitur bisnis (mis. auth/, users/, products/)
  pages/             -> Top-level route components, minimal logic
  hooks/             -> Custom hooks untuk logic yang reusable
  lib/               -> API client (axios/fetch wrapper) & utilities umum
  stores/            -> Global state stores (mis. Zustand)
  types/             -> TypeScript types/interfaces bersama
```

**Prinsip yang diajarkan:**

1. **UI components** — tidak tahu data dari mana, hanya render props yang diterima. Mudah di-reuse dan di-test.
2. **Feature components** — tahu tentang domain bisnis, lakukan fetch data, kelola state. Gunakan custom hooks untuk pisahkan logic dari JSX.
3. **Pages** — sangat tipis. Hanya compose feature components dan handle routing params. Tidak ada business logic berat di sini.

---

## Custom Hooks — Kapan dan Bagaimana

Custom hook adalah cara utama untuk reuse logic di React. Wajib diajarkan dengan benar:

```tsx
// [KONSEP] Custom hook adalah fungsi biasa yang namanya dimulai dengan "use"
// dan memanggil hooks lain di dalamnya. Dia bisa return apapun.
// BUKAN untuk reuse JSX — untuk reuse LOGIC.

// Contoh: mengekstrak fetch logic dari component
function useUser(userId: string) {
  // [KONSEP] Semua state yang berkaitan dikumpulkan dalam satu hook
  const [user, setUser] = useState<User | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<Error | null>(null)

  useEffect(() => {
    let cancelled = false  // [KONSEP] Flag untuk handle race condition dan unmount

    async function fetchUser() {
      // [KONSEP] Reset state dari userId sebelumnya, agar error/data lama
      // tidak ikut tampil saat userId berganti.
      setError(null)
      setUser(null)
      try {
        setIsLoading(true)
        const data = await api.getUser(userId)
        if (!cancelled) setUser(data)  // Jangan set state jika sudah unmount / request usang
      } catch (err) {
        if (!cancelled) setError(err instanceof Error ? err : new Error('Unknown error'))
      } finally {
        if (!cancelled) setIsLoading(false)
      }
    }

    fetchUser()

    return () => { cancelled = true }  // Cleanup: tandai sebagai cancelled saat unmount/re-run
  }, [userId])

  return { user, isLoading, error }  // Return object, bukan array (lebih readable)
}

// Penggunaan di component — bersih, tanpa boilerplate
function UserProfile({ userId }: { userId: string }) {
  const { user, isLoading, error } = useUser(userId)

  if (isLoading) return <Spinner />
  if (error) return <ErrorMessage message={error.message} />
  if (!user) return null

  return <div>{user.name}</div>
}
```

---

## Satu Lapisan di Bawah dan Jembatan Konsep (Hubungan ke CS Tutor)

Saat topik berikut muncul, beri 1–2 kalimat tentang lapisan bawahnya atau jembatannya, lalu arahkan ke CS Tutor ([`technology/computer-science/tutor/SKILL.md`](../../../technology/computer-science/tutor/SKILL.md)) untuk pendalaman:

| Topik React | Lapisan di bawah / jembatan | Fase CS Tutor ([`roadmap.md`](../../../technology/computer-science/roadmap.md)) |
|---|---|---|
| closure, stale closure | Closure menangkap binding variabel. Jembatani dari bahasa yang dikuasai pelajar bila ada (mis. di Java, lambda hanya boleh menangkap variabel *effectively final*); di React, setiap render membuat binding (`const`) baru untuk state/props, sehingga closure dari render lama tetap memegang nilai render lama — itulah *stale closure* (lihat react.dev "State as a Snapshot") | Fase 1 (SICP: environment model) |
| axios/fetch, CORS, header | HTTP protocol, *same-origin policy*, dan *preflight request* | Fase 6 (Networking) |
| penyimpanan token (cookie vs `localStorage`) | Model ancaman XSS dan CSRF di browser | Fase 6 & Keamanan Web |
| zona waktu, angka desimal | Representasi waktu UTC dan standar *floating point* IEEE 754 | Fase 2 (Architecture) |

---

## Referensi Dokumentasi & Sumber Belajar

- **React Docs (react.dev):** https://react.dev/ — dokumentasi resmi yang sangat bagus, pakai ini sebagai referensi utama
- **React Learn:** https://react.dev/learn — tutorial interaktif dari tim React, mulai dari sini
- **Dan Abramov - "A Complete Guide to useEffect":** https://overreacted.io/a-complete-guide-to-useeffect/ — wajib baca untuk memahami `useEffect` dengan benar
- **Dan Abramov - "Making setInterval Declarative":** https://overreacted.io/making-setinterval-declarative-with-react-hooks/ — artikel klasik tentang *stale closure*
- **TkDodo's React Query Blog:** https://tkdodo.eu/blog/ — artikel mendalam tentang *data fetching* di React
- **TypeScript Handbook:** https://www.typescriptlang.org/docs/handbook/intro.html — referensi TypeScript

---

## Template Penjelasan yang Baik

Gunakan format ini saat menjelaskan konsep baru (versi ringkas 1–3 kalimat per poin, kecuali diminta mendalam):

```
**[Nama Konsep]**

**Apa itu?**
[1–2 kalimat definisi yang jelas]

**Mental Model:**
[Bagaimana cara berpikir tentang ini — analoginya apa]

**Kapan digunakan:**
[Konteks penggunaan yang tepat]

**Kapan TIDAK digunakan:**
[Anti-pattern dan over-engineering yang umum]

**Contoh:**
[Kode dengan komentar pedagogis — selalu handle loading/error/empty state]

**Kesalahan umum:**
[Apa yang sering salah dilakukan pemula terkait ini]
```

---

*⬅️ Kembali ke [Bagian 1: `rules.md`](rules.md)*
