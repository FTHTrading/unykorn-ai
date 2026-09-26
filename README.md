<p align="center">
  <img src="assets/unykorn-banner.png" alt="UnyKorn — infrastructure for capital and autonomous agents" width="100%">
</p>

<p align="center">
  <b>unykorn.ai</b> — the main site for UnyKorn LLC.<br>
  Verifiable execution infrastructure for capital and autonomous agents.
</p>

---

## Pages

| Page | What it covers |
|---|---|
| `index.html` | Company front door: stack, proof strip, principles |
| `platform.html` | Architecture: trust, execution and agent layers |
| `genesis402.html` | The agent-payment rail (links to twin.unykorn.org) |
| `capital.html` | Issuance OS, custody, cash and gold rails, structures |
| `registry.html` | Real assets, namespaces, LPS-1 provenance |
| `systems.html` | **Everything we build**, each labeled Live / Pilot / Building / Research |
| `developers.html` | MCP, catalog, OpenAPI, x402 manifest, status, receipts |
| `company.html` | Who we are, what we are not, how we work, contact |

## Updating the systems index

Edit `data/systems.json` (name, url, pillar, status, one line), then rebuild. The status counts, filters and cards update automatically.

Statuses mean exactly this:

- **live** — public and usable today
- **pilot** — running with design partners or as a public demo
- **building** — in active development
- **research** — specified, not yet built

## Build and deploy

```bash
python3 build.py        # writes the static site to ./site
```

No dependencies. Deploy `site/` to Cloudflare Pages (build command: `python3 build.py`, output directory: `site`), or upload the folder as-is.

## Design system

Light silver-and-blue glass, dark text, Fraunces for headlines, Outfit for body. The crest in `assets/unykorn-crest.svg` is the official UnyKorn mark used on every property.

---

<p align="center">
  <img src="assets/unykorn-crest.svg" width="40" alt="UnyKorn"><br>
  <sub>UnyKorn LLC, Wyoming. UnyKorn licenses software and builds infrastructure. It is not a bank, broker-dealer, custodian or issuer, issues no tokens and never holds client funds.</sub>
</p>
