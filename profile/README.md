<p align="center">
  <img src="assets/og.png" alt="matura.lol" width="720"/>
</p>

<h1 align="center">matura.lol</h1>

<p align="center">
  <b>Największa wyszukiwarka zadań egzaminacyjnych CKE/OKE.</b><br/>
  Matura, egzamin ósmoklasisty i gimnazjalny, próbne, informatory — z OCR,
  kluczami odpowiedzi, rozwiązaniami i tagowaniem Jev.
</p>

<p align="center">
  <a href="https://matura.lol"><img src="https://img.shields.io/badge/site-matura.lol-3b82f6?logo=googlechrome&logoColor=white" alt="Site"/></a>
  <a href="https://huggingface.co/matura-lol"><img src="https://img.shields.io/badge/HuggingFace-matura--lol-FFD21E?logo=huggingface&logoColor=black" alt="HuggingFace"/></a>
  <img src="assets/days-to-matura.svg" alt="Dni do matury"/>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT--%2B--AGPL-blue" alt="License"/></a>
</p>

---

## Co tu znajdziesz

| Repozytorium | Opis |
| --- | --- |
| [**datasets**](https://github.com/matura-lol/datasets) | Dane otwarte: polskie arkusze egzaminacyjne, odpowiedzi, rozwiązania i źródła używane na matura.lol (zstd). |
| [**Jev-categorise**](https://github.com/matura-lol/Jev-categorise) | Tagowanie arkuszy i zadań przez TypeSafe Jev (dział, trudność, sposób, forma, bloom, czas). |

## Dane i modele

Pełne, **nieskompresowane** dane oraz wytrenowane modele publikujemy na
Hugging Face w organizacji [**matura-lol**](https://huggingface.co/matura-lol):

- [matura.lol-datasets](https://huggingface.co/datasets/matura-lol/matura.lol-datasets) — korpus, importy, tagi Jev, dump bazy (AGPL-3.0)
- [GLiNER2.5-multi-Decide-finetune](https://huggingface.co/matura-lol/GLiNER2.5-multi-Decide-finetune) — model klasyfikacji zadań (AGPL-3.0)

## Licencje

- Kod projektu — **MIT**.
- Dane i modele — **AGPL-3.0** (poszczególne fragmenty tekstu mogą mieć własne
  licencje; arkusze CKE/OKE pozostają własnością CKE/OKE).

---

<p align="center">
  Wzór na maturę — <a href="https://matura.lol">matura.lol</a> ·
  <a href="https://discord.gg/UBMVWXDJwU">Discord</a> · Polska 🇵🇱
</p>