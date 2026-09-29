# matura.lol · Organisation

This repository hosts the **organisation infocard** for
[github.com/matura-lol](https://github.com/matura-lol) — the open GitHub home of
[matura.lol](https://matura.lol), the largest search engine over Polish CKE/OKE
exam papers.

## What's inside

- `profile/README.md` — the profile card shown on the organisation page.
- `assets/` — `og.png` (brand banner), `favicon.svg`, and the auto-updated
  `days-to-matura.svg` badge.
- `.github/workflows/days-to-matura.yml` — a daily cron that recomputes the
  countdown to the matura exam (3 May) and commits the updated badge, using the
  same logic as the site (`web/app.js`).

## Related

- Data & models: [huggingface.co/matura-lol](https://huggingface.co/matura-lol)
- Site: [matura.lol](https://matura.lol)

License: MIT (this repo) — see [LICENSE](LICENSE).