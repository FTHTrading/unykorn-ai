#!/usr/bin/env python3
"""Builds the static unykorn.ai site into ./dist. Run: python3 build.py"""
import json, os, shutil, html

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "site")
CREST = open(os.path.join(ROOT, "assets/unykorn-crest.svg")).read().replace('width="200" height="200"', "")
SYSTEMS = json.load(open(os.path.join(ROOT, "data/systems.json")))

NAV = [
    ("index.html", "Home"),
    ("platform.html", "Platform"),
    ("genesis402.html", "Genesis402"),
    ("capital.html", "Capital"),
    ("registry.html", "Real Assets"),
    ("systems.html", "Systems"),
    ("developers.html", "Developers"),
    ("company.html", "Company"),
]

ICONS = {
    "agent": '<path d="M12 3v3M7 8h10a3 3 0 0 1 3 3v5a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3v-5a3 3 0 0 1 3-3z"/><circle cx="9.5" cy="13" r="1.2"/><circle cx="14.5" cy="13" r="1.2"/>',
    "capital": '<path d="M3 10l9-6 9 6"/><path d="M5 10v8M9.5 10v8M14.5 10v8M19 10v8"/><path d="M3 20h18"/>',
    "registry": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>',
    "services": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18v3h3l6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
    "check": '<path d="M5 12l4 4 10-10"/>',
    "proof": '<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    "bolt": '<path d="M13 3L5 14h6l-1 7 8-11h-6z"/>',
    "code": '<path d="M8 8l-4 4 4 4M16 8l4 4-4 4M13 5l-2 14"/>',
    "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
}

def icon(name, tone=""):
    return f'<div class="icon {tone}"><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg></div>'

def pill(status):
    label = {"live": "Live", "pilot": "Pilot", "building": "Building", "research": "Research"}[status]
    return f'<span class="pill {status}">{label}</span>'

def layout(page, title, desc, body):
    nav = "".join(
        f'<a href="{href}"{" aria-current=page" if href == page else ""}>{label}</a>' for href, label in NAV
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="https://unykorn.ai/assets/og.png">
<meta name="theme-color" content="#eef2f8">
<link rel="icon" href="assets/unykorn-crest.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;1,9..144,500&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<header class="top"><div class="wrap">
  <div class="bar glass hi">
    <a class="brand" href="index.html" aria-label="UnyKorn home">{CREST}<span>UNYKORN</span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav">{nav}</nav>
    <a class="cta" href="company.html#contact">Talk to UnyKorn</a>
  </div>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
  <div class="glass">
    <div class="f">
      <div>
        <a class="brand" href="index.html" style="margin-bottom:12px">{CREST}<span>UNYKORN</span></a>
        <p class="muted small" style="max-width:320px">Verifiable execution infrastructure for capital and autonomous agents.</p>
      </div>
      <div><h4>Products</h4>
        <a href="genesis402.html">Genesis402</a><a href="capital.html">Capital infrastructure</a><a href="registry.html">Real assets &amp; registry</a><a href="https://hire.unykorn.ai">Services</a></div>
      <div><h4>Developers</h4>
        <a href="developers.html">Overview</a><a href="https://twin.unykorn.org/catalog">API catalog</a><a href="https://www.npmjs.com/package/genesis402-mcp">MCP server</a><a href="https://twin.unykorn.org/status">Status</a></div>
      <div><h4>Company</h4>
        <a href="company.html">About</a><a href="systems.html">Everything we build</a><a href="https://network.unykorn.ai">Network</a><a href="company.html#contact">Contact</a></div>
    </div>
    <p class="legal">UnyKorn LLC, a Wyoming limited liability company. UnyKorn licenses software and builds infrastructure. It is not a bank, broker-dealer, exchange, custodian, trustee, transfer agent, investment adviser, money transmitter or issuer, issues no tokens and never holds client funds. Risk and screening outputs are signals from public data, not legal, tax or investment advice.</p>
  </div>
</div></footer>
<script>
  const b=document.querySelector('.menu-btn'),n=document.getElementById('nav');
  b&&b.addEventListener('click',()=>{{const o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)}});
</script>
</body>
</html>"""

# ------------------------------------------------------------------ pages
PAGES = {}

counts = {s: sum(1 for x in SYSTEMS["systems"] if x["status"] == s) for s in ("live", "pilot", "building", "research")}

PAGES["index.html"] = ("UnyKorn — Infrastructure for capital and autonomous agents",
"UnyKorn builds verifiable execution systems for tokenized capital, institutional settlement, and AI agents that discover, buy and use data and compute on their own.", f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <div class="eyebrow rise"><span class="dot"></span>Live · {counts['live']} systems in production</div>
    <h1 class="rise d1" style="margin-top:18px">Infrastructure for capital and <em>autonomous agents.</em></h1>
    <p class="lead rise d2" style="margin-top:20px">We build verifiable execution systems for tokenized capital, institutional settlement, and AI agents that discover, pay for and use data and compute on their own.</p>
    <div class="actions rise d3">
      <a class="cta" href="genesis402.html">Explore Genesis402</a>
      <a class="cta ghost" href="capital.html">Capital infrastructure</a>
      <a class="cta ghost" href="systems.html">See everything we build</a>
    </div>
  </div>
  <div class="crest-big rise d2">{CREST}</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <div class="glass proof">
    <div><b>360</b><span>paid agent endpoints</span></div>
    <div><b>14</b><span>networks stood up</span></div>
    <div><b>434</b><span>contracts on-chain</span></div>
    <div><b>1,654</b><span>names across 78 roots</span></div>
    <div><b>USDC</b><span>x402 settlement, signed receipts</span></div>
  </div>
  <p class="small muted" style="margin-top:10px">Every figure links to a public explorer or a live endpoint. <a href="systems.html">See the evidence</a>.</p>
</div></section>

<section><div class="wrap">
  <div class="sec-head"><h2>The UnyKorn stack</h2><p class="muted">One company, four layers. Each one works on its own and gets stronger with the others.</p></div>
  <div class="grid g4">
    <a class="card glass" href="genesis402.html">{icon('agent','ember')}<div class="k">Agent economy</div><h3>Genesis402</h3><p>AI agents discover, buy and use data and compute with per-call USDC payments.</p><span class="go">Explore →</span></a>
    <a class="card glass" href="capital.html">{icon('capital','blue')}<div class="k">Capital</div><h3>Issuance &amp; settlement</h3><p>Custody, policy, issuance and multi-rail settlement in the issuer's own name.</p><span class="go">Explore →</span></a>
    <a class="card glass" href="registry.html">{icon('registry')}<div class="k">Real assets</div><h3>Registry &amp; proof</h3><p>Register, verify and anchor real-world rights, assets and records.</p><span class="go">Explore →</span></a>
    <a class="card glass" href="https://hire.unykorn.ai">{icon('services')}<div class="k">Services</div><h3>We deploy it for you</h3><p>Private rails, paid APIs, MCP servers and issuance pilots, fixed price.</p><span class="go">Work with us →</span></a>
  </div>
</div></section>

<section><div class="wrap grid g2" style="align-items:center">
  <div>
    <div class="eyebrow plain">How it fits together</div>
    <h2 style="margin-top:12px">From a real asset to a <em>settled, provable</em> transaction.</h2>
    <p class="lead" style="margin-top:14px">The same evidence trail runs through every product: who acted, under which policy, on which rail, with a receipt anyone can check.</p>
    <div class="actions"><a class="cta ghost" href="platform.html">See the architecture</a></div>
  </div>
  <div class="glass card">
    <div class="flow"><span>Asset or right</span><i>→</i><span>Verified identity</span><i>→</i><span>Policy</span><i>→</i><span>Issuance</span><i>→</i><span>Custody</span><i>→</i><span>Settlement</span><i>→</i><span>Evidence</span></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sec-head"><h2>Why UnyKorn</h2></div>
  <div class="grid g3">
    <div class="card glass">{icon('check')}<h3>Deterministic</h3><p>Policies and routing are explicit, testable and reproducible.</p></div>
    <div class="card glass">{icon('proof')}<h3>Verifiable</h3><p>Sources, payments, receipts and audit logs are outputs, not afterthoughts.</p></div>
    <div class="card glass">{icon('link')}<h3>Interoperable</h3><p>Works across the chains, custodians, stablecoin rails and APIs you already use.</p></div>
    <div class="card glass">{icon('bolt','ember')}<h3>Agent-native</h3><p>Software can find a service, pay for it, use it and keep proof of what happened.</p></div>
    <div class="card glass">{icon('capital','blue')}<h3>Institution-ready</h3><p>Compliance and custody are in the architecture from day one.</p></div>
    <div class="card glass">{icon('eye')}<h3>Honest status</h3><p>Every system is labeled live, pilot, building or research. <a href="systems.html">Check it</a>.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="glass hi card band">
    <div><h2>Build on the rails, or have us build yours.</h2><p class="lead" style="margin-top:10px">Start with a five-day scoping sprint and a fixed-price plan.</p></div>
    <div class="actions" style="margin:0"><a class="cta" href="https://hire.unykorn.ai">See packages</a><a class="cta ghost" href="company.html#contact">Contact</a></div>
  </div>
</div></section>
""")

DIAGRAM = """
<svg viewBox="0 0 1000 520" role="img" aria-label="UnyKorn architecture: sources feed a trust layer, an execution layer and an agent layer, used by institutions, builders, agents and operators">
<defs>
  <linearGradient id="lay" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#eef3fb"/></linearGradient>
  <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#8a94a6"/></marker>
</defs>
<g font-size="15" fill="#0b0d12">
  <rect x="20" y="20" width="960" height="70" rx="14" fill="#f7f9fc" stroke="#d6dde8"/>
  <text x="40" y="50" font-weight="600" font-size="13" letter-spacing="2" fill="#4a5363">SOURCES</text>
  <text x="40" y="74">Institutions · real assets · blockchains · custodians · stablecoin rails · public data · APIs</text>

  <rect x="20" y="120" width="960" height="92" rx="14" fill="url(#lay)" stroke="#c9d5e8"/>
  <text x="40" y="150" font-weight="600" font-size="13" letter-spacing="2" fill="#2d6bd8">TRUST LAYER</text>
  <g font-size="14"><rect x="40" y="164" width="130" height="32" rx="8" fill="#fff" stroke="#d6dde8"/><text x="105" y="185" text-anchor="middle">Identity</text>
  <rect x="182" y="164" width="130" height="32" rx="8" fill="#fff" stroke="#d6dde8"/><text x="247" y="185" text-anchor="middle">Policy</text>
  <rect x="324" y="164" width="130" height="32" rx="8" fill="#fff" stroke="#d6dde8"/><text x="389" y="185" text-anchor="middle">Registry</text>
  <rect x="466" y="164" width="130" height="32" rx="8" fill="#fff" stroke="#d6dde8"/><text x="531" y="185" text-anchor="middle">Proof</text>
  <rect x="608" y="164" width="130" height="32" rx="8" fill="#fff" stroke="#d6dde8"/><text x="673" y="185" text-anchor="middle">Receipts</text>
  <rect x="750" y="164" width="210" height="32" rx="8" fill="#fff" stroke="#d6dde8"/><text x="855" y="185" text-anchor="middle">Audit trail</text></g>

  <rect x="20" y="240" width="470" height="120" rx="14" fill="url(#lay)" stroke="#c9d5e8"/>
  <text x="40" y="270" font-weight="600" font-size="13" letter-spacing="2" fill="#2d6bd8">EXECUTION LAYER</text>
  <text x="40" y="298">Issuance OS · series and policy rooms</text>
  <text x="40" y="322">Custody connectors · issuer's own name</text>
  <text x="40" y="346">Settlement · DvP across 14 networks</text>

  <rect x="510" y="240" width="470" height="120" rx="14" fill="#fff7f0" stroke="#f3c9a6"/>
  <text x="530" y="270" font-weight="600" font-size="13" letter-spacing="2" fill="#e2620b">AGENT LAYER · GENESIS402</text>
  <text x="530" y="298">Discovery · catalog, MCP, /.well-known/x402</text>
  <text x="530" y="322">x402 + MPP payment · USDC on Base</text>
  <text x="530" y="346">360 paid data and compute endpoints</text>

  <rect x="20" y="390" width="960" height="70" rx="14" fill="#f7f9fc" stroke="#d6dde8"/>
  <text x="40" y="420" font-weight="600" font-size="13" letter-spacing="2" fill="#4a5363">WHO USES IT</text>
  <text x="40" y="444">Issuers and institutions · developers and builders · AI agents · operators</text>

  <g stroke="#8a94a6" stroke-width="1.6" marker-end="url(#ar)"><path d="M500 92v24"/><path d="M255 214v22"/><path d="M745 214v22"/><path d="M255 362v24"/><path d="M745 362v24"/><path d="M492 300h14"/></g>
</g>
<text x="500" y="500" text-anchor="middle" font-size="13" fill="#4a5363">Every arrow leaves a record: a policy decision, a payment, a receipt or an on-chain anchor.</text>
</svg>"""

PAGES["platform.html"] = ("Platform — UnyKorn",
"How UnyKorn's trust, execution and agent layers connect sources to institutions, builders and AI agents.", f"""
<section class="hero"><div class="wrap">
  <div class="eyebrow plain">Platform</div>
  <h1 style="margin-top:14px">One architecture. <em>Four layers.</em></h1>
  <p class="lead" style="margin-top:18px">UnyKorn is the trust and execution company. Genesis402 is the agent-access rail. The issuance OS is the capital layer. The registry is the real-asset and evidence layer.</p>
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="glass hi diagram">{DIAGRAM}</div></div></section>
<section><div class="wrap grid g3">
  <div class="card glass">{icon('proof','blue')}<div class="k">Trust layer</div><h3>Who, under which rule</h3><p>Identity, policy, registry, proofs and receipts shared by every product.</p></div>
  <div class="card glass">{icon('layers','blue')}<div class="k">Execution layer</div><h3>Issue, hold, settle</h3><p>Series issuance, custody in the client's name, and settlement across the rails they already use.</p></div>
  <div class="card glass">{icon('agent','ember')}<div class="k">Agent layer</div><h3>Pay per call</h3><p>Agents find a service, pay in USDC, get a sourced answer and keep the receipt.</p></div>
</div></section>
<section><div class="wrap"><div class="glass card"><div class="sec-head" style="margin:0"><div><h3>Readiness, labeled honestly</h3><p class="muted" style="margin-top:6px">Live, pilot, building or research. Nothing here is described as more finished than it is.</p></div><a class="cta ghost" href="systems.html">Open the systems index</a></div></div></div></section>
""")

PAGES["genesis402.html"] = ("Genesis402 — Pay-per-call data and compute for AI agents | UnyKorn",
"360 pay-per-call APIs for AI agents over x402 and MPP, settled in USDC on Base. No account or API key. Signed receipts.", f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <div class="eyebrow"><span class="dot"></span>Live on Base · x402 v2 + MPP</div>
    <h1 style="margin-top:16px">Genesis<em>402</em></h1>
    <p class="lead" style="margin-top:18px">Pay-per-call data and compute for AI agents. No account, no API key: an agent pays in USDC and gets a sourced answer with a signed receipt.</p>
    <div class="actions"><a class="cta" href="https://twin.unykorn.org">Open the rail</a><a class="cta ghost" href="https://twin.unykorn.org/catalog">Browse 360 endpoints</a></div>
  </div>
  <div class="glass hi card">
    <div class="k">Connect in one line</div>
    <pre><code>https://twin.unykorn.org/mcp</code></pre>
    <p class="small muted">Streamable HTTP. Works in Claude, Cursor, VS Code and any MCP client. Or run <code>npx genesis402-mcp</code> locally with a spend cap.</p>
  </div>
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="glass proof">
  <div><b>360</b><span>endpoints</span></div><div><b>$0.001</b><span>lowest price per call</span></div><div><b>$0.25</b><span>highest price per call</span></div><div><b>0</b><span>accounts or keys needed</span></div><div><b>48h</b><span>on-chain reconciliation</span></div>
</div></div></section>
<section><div class="wrap">
  <div class="sec-head"><h2>How a call works</h2></div>
  <div class="grid g4">
    <div class="card glass"><div class="k">1 · Ask</div><h3>Request</h3><p>The agent calls an endpoint. Parameters can be checked free first.</p></div>
    <div class="card glass"><div class="k">2 · Quote</div><h3>HTTP 402</h3><p>The rail answers with the exact price in USDC.</p></div>
    <div class="card glass"><div class="k">3 · Pay</div><h3>Sign</h3><p>The agent's wallet signs the payment, within the cap it was given.</p></div>
    <div class="card glass"><div class="k">4 · Receive</div><h3>Result + receipt</h3><p>Sourced answer, evidence hash and a receipt id.</p></div>
  </div>
</div></section>
<section><div class="wrap">
  <div class="sec-head"><h2>What's on the rail</h2><a class="cta ghost" href="https://twin.unykorn.org/catalog">Full catalog</a></div>
  <div class="glass rows">
    <div class="row"><b>Risk &amp; compliance</b><span class="muted">Wallet briefs, token checks, sanctions-list signals, holder concentration</span><span class="chip">$0.008–$0.25</span></div>
    <div class="row"><b>Chain reads</b><span class="muted">10 EVM chains plus Bitcoin, Solana, Stellar and XRPL</span><span class="chip">$0.001–$0.008</span></div>
    <div class="row"><b>Markets &amp; DeFi</b><span class="muted">Prices, yields from 15,000+ pools, stablecoins, fees</span><span class="chip">$0.001–$0.01</span></div>
    <div class="row"><b>Public records</b><span class="muted">SEC financials and filings, FX, Treasury yields</span><span class="chip">$0.001–$0.01</span></div>
    <div class="row"><b>Web &amp; domain</b><span class="muted">WHOIS, DNS, TLS, email checks, clean page extraction</span><span class="chip">$0.001–$0.004</span></div>
    <div class="row"><b>AI on our own GPU</b><span class="muted">OpenAI-compatible chat, embeddings, extraction, text-to-SQL</span><span class="chip">$0.002–$0.01</span></div>
    <div class="row"><b>Proofs &amp; compute</b><span class="muted">Signed Ed25519 receipts, hashing, ABI and EIP-712 tools</span><span class="chip">$0.001–$0.25</span></div>
  </div>
</div></section>
<section><div class="wrap grid g3">
  <div class="card glass">{icon('check')}<h3>Validate before pay</h3><p>Bad input is rejected free. Nothing is charged.</p></div>
  <div class="card glass">{icon('proof')}<h3>Sources on every answer</h3><p>Each result names its upstream and carries an evidence hash.</p></div>
  <div class="card glass">{icon('clock')}<h3>Make-good</h3><p>A paid call that isn't delivered is credited back automatically.</p></div>
</div></section>
""")

PAGES["capital.html"] = ("Capital infrastructure — UnyKorn",
"Issuance software and rails: series, policy rooms, custody in the issuer's own name, and settlement across the rails you already use.", f"""
<section class="hero"><div class="wrap">
  <div class="eyebrow"><span class="dot"></span>Issuance OS · Live</div>
  <h1 style="margin-top:14px">We build the rails. <em>You stay issuer.</em></h1>
  <p class="lead" style="margin-top:18px">Series, labeled policy rooms, freeze and whitelist controls. Custody opens in your own name at a qualified custodian you choose. Every step is recorded on a public ledger.</p>
  <div class="actions"><a class="cta" href="https://order.unykorn.ai">Start an engagement</a><a class="cta ghost" href="https://quant.unykorn.ai">Quant Command</a></div>
</div></section>
<section style="padding-top:0"><div class="wrap grid g2">
  <div class="glass card">
    <div class="k">Who holds what</div>
    <div class="rows">
      <div class="row" style="grid-template-columns:1fr auto"><b>UnyKorn LLC</b><span class="muted">Issuance software</span></div>
      <div class="row" style="grid-template-columns:1fr auto"><b>Qualified custodian (your choice)</b><span class="muted">Keys · 2-of-N policy</span></div>
      <div class="row" style="grid-template-columns:1fr auto"><b>Regulated cash &amp; gold rails</b><span class="muted">USD stablecoin · tokenized gold</span></div>
      <div class="row" style="grid-template-columns:1fr auto"><b>Settlement</b><span class="muted">DvP, off-chain or on-chain</span></div>
      <div class="row" style="grid-template-columns:1fr auto"><b>You</b><span class="muted">Issuer. You approve.</span></div>
    </div>
  </div>
  <div class="grid">
    <div class="card glass">{icon('proof','blue')}<h3>Custody</h3><p>Qualified cold custody in your name. Policy wallets. You never hold a seed.</p></div>
    <div class="card glass">{icon('capital','blue')}<h3>Cash &amp; gold rails</h3><p>Regulated USD stablecoin and tokenized gold, white-labeled to your series.</p></div>
    <div class="card glass">{icon('bolt','ember')}<h3>Mint</h3><p>Series capped to attestation at <a href="https://launch.unykorn.org">launch.unykorn.org</a>.</p></div>
  </div>
</div></section>
<section><div class="wrap">
  <div class="sec-head"><h2>Structures we build</h2><p class="muted">The wrapper a real-world structure needs when the buyer wants a named custodian. Counsel writes the note. We build the rooms.</p></div>
  <div class="grid g3">
    <div class="card glass"><div class="k">Gold series</div><h3>Attested ounces</h3><p>On-chain series capped to vault receipts. <a href="https://g.unykorn.ai">Public demo</a>.</p></div>
    <div class="card glass"><div class="k">Cash sleeve</div><h3>Tokenized T-bill</h3><p>Idle-cash drag, admin fee and haircut shown up front.</p></div>
    <div class="card glass"><div class="k">Fund share</div><h3>LP / NAV</h3><p>Tokenized interests without standing up a transfer-agency stack alone.</p></div>
    <div class="card glass"><div class="k">Policy pack</div><h3>Freeze · velocity · whitelist</h3><p>The constraint is the product.</p></div>
    <div class="card glass"><div class="k">Collateral</div><h3>Weekend-live margin</h3><p>Collateral that stays usable when banks are closed.</p></div>
    <div class="card glass"><div class="k">Private credit</div><h3>XRPL loans</h3><p>Loan rails on XRPL. <span class="pill pilot">Pilot</span></p></div>
  </div>
</div></section>
<section><div class="wrap"><div class="glass note">UnyKorn licenses software. It is not your broker-dealer, ATS, bank, custodian or market maker, issues no tokens and never holds client funds.</div></div></section>
""")

PAGES["registry.html"] = ("Real assets & registry — UnyKorn",
"Infrastructure for registering, verifying and anchoring real-world rights, assets and records, with an evidence trail anyone can check.", f"""
<section class="hero"><div class="wrap">
  <div class="eyebrow plain">Real assets &amp; registry</div>
  <h1 style="margin-top:14px">Real-world rights, <em>on the record.</em></h1>
  <p class="lead" style="margin-top:18px">Register, verify and anchor assets, names and documents, backed by identity, policy and an auditable history. Check any of it yourself.</p>
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="glass card"><div class="flow"><span>Asset or right</span><i>→</i><span>Verified identity</span><i>→</i><span>Policy controls</span><i>→</i><span>Tokenized record</span><i>→</i><span>Custody</span><i>→</i><span>Settlement</span><i>→</i><span>Immutable evidence</span></div></div></div></section>
<section><div class="wrap grid g3">
  <a class="card glass" href="https://network.unykorn.ai">{icon('registry','blue')}<div class="k">Namespaces</div><h3>1,654 names · 78 roots</h3><p>A sovereign namespace registry on Solana and EVM. Verify every anchor from your browser.</p><span class="go">Verify →</span></a>
  <a class="card glass" href="https://xxxiii.io/publish">{icon('proof','ember')}<div class="k">Provenance</div><h3>LPS-1 publishing</h3><p>Anchor a work: SHA-256, IPFS, Polygon anchor, certificate and a public proof page.</p><span class="go">Publish →</span></a>
  <a class="card glass" href="https://powerpunchathletics.com">{icon('capital')}<div class="k">Product RWA</div><h3>Power Punch Athletics</h3><p>A patented product with its unit run and 33-item history anchored on Base.</p><span class="go">See it →</span></a>
</div></section>
<section><div class="wrap">
  <div class="sec-head"><h2>What the registry covers</h2></div>
  <div class="glass rows">
    <div class="row"><b>Identity</b><span class="muted">Wallet-linked names for brands, athletes and agents</span>{pill('live')}</div>
    <div class="row"><b>Documents &amp; IP</b><span class="muted">Hash-anchored works with certificates and proof pages</span>{pill('live')}</div>
    <div class="row"><b>Physical products</b><span class="muted">Unit runs, product history, affiliate attribution</span>{pill('live')}</div>
    <div class="row"><b>Commodities</b><span class="muted">Attested series capped to vault receipts</span>{pill('pilot')}</div>
    <div class="row"><b>Introductions</b><span class="muted">Introducer attribution through every downstream deal</span>{pill('research')}</div>
  </div>
</div></section>
""")

# systems page — rendered from data/systems.json, filterable client-side
cards = []
for s in SYSTEMS["systems"]:
    cards.append(f'''<a class="card glass sys" href="{s['url']}" data-status="{s['status']}" data-pillar="{html.escape(s['pillar'])}" data-q="{html.escape((s['name']+' '+s['what']+' '+s['pillar']).lower())}">
      <div style="display:flex;justify-content:space-between;gap:10px;align-items:center"><div class="k">{html.escape(s['pillar'])}</div>{pill(s['status'])}</div>
      <h3>{html.escape(s['name'])}</h3><p>{html.escape(s['what'])}</p><span class="go small">{html.escape(s['url'].replace('https://',''))} →</span></a>''')
pillars = sorted({s["pillar"] for s in SYSTEMS["systems"]})
PAGES["systems.html"] = ("Everything we build — UnyKorn",
"Every UnyKorn system in one place, each labeled live, pilot, building or research.", f"""
<section class="hero"><div class="wrap">
  <div class="eyebrow plain">Systems index · updated {SYSTEMS['updated']}</div>
  <h1 style="margin-top:14px">Everything we build, <em>labeled honestly.</em></h1>
  <p class="lead" style="margin-top:18px">{len(SYSTEMS['systems'])} systems across four layers. Open any one; each links to the live site, endpoint or explorer.</p>
</div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="glass proof" style="grid-template-columns:repeat(4,1fr)">
    <div><b>{counts['live']}</b><span>{pill('live')}</span></div><div><b>{counts['pilot']}</b><span>{pill('pilot')}</span></div><div><b>{counts['building']}</b><span>{pill('building')}</span></div><div><b>{counts['research']}</b><span>{pill('research')}</span></div>
  </div>
  <div class="sec-head" style="margin-top:28px">
    <div class="filters" role="group" aria-label="Filter by layer"><button aria-pressed="true" data-f="all">All</button>{''.join(f'<button aria-pressed="false" data-f="{html.escape(p)}">{html.escape(p)}</button>' for p in pillars)}</div>
    <input class="search" type="search" placeholder="Search systems" aria-label="Search systems">
  </div>
  <div class="grid g3" id="sys">{''.join(cards)}</div>
  <p class="small muted" style="margin-top:18px">Live: public and usable today. Pilot: running with design partners or as a public demo. Building: in active development. Research: specified, not yet built.</p>
</div></section>
<script>
(()=>{{const bs=[...document.querySelectorAll('.filters button')],q=document.querySelector('.search'),cs=[...document.querySelectorAll('.sys')];let f='all';
const run=()=>{{const t=q.value.trim().toLowerCase();cs.forEach(c=>{{c.style.display=((f==='all'||c.dataset.pillar===f)&&(!t||c.dataset.q.includes(t)))?'':'none'}})}};
bs.forEach(b=>b.addEventListener('click',()=>{{bs.forEach(x=>x.setAttribute('aria-pressed','false'));b.setAttribute('aria-pressed','true');f=b.dataset.f;run()}}));q.addEventListener('input',run)}})();
</script>
""")

PAGES["developers.html"] = ("Developers — UnyKorn",
"Docs, catalogs, MCP server, SDKs and discovery endpoints for building on UnyKorn.", f"""
<section class="hero"><div class="wrap">
  <div class="eyebrow plain">Developers</div>
  <h1 style="margin-top:14px">Build on the rails in <em>minutes.</em></h1>
  <p class="lead" style="margin-top:18px">Everything is discoverable by machines and people: catalogs, OpenAPI, x402 manifests and an MCP server.</p>
</div></section>
<section style="padding-top:0"><div class="wrap grid g2">
  <div class="glass card"><div class="k">MCP · hosted</div><pre><code>https://twin.unykorn.org/mcp</code></pre><p class="small muted">No install. Free tools work immediately; paid tools return a quote.</p></div>
  <div class="glass card"><div class="k">MCP · local, pays within a cap</div><pre><code>npx -y genesis402-mcp
GENESIS402_LIVE=1  GENESIS402_MAX_USD=0.25</code></pre><p class="small muted">Quote-only until you turn paying on.</p></div>
</div></section>
<section><div class="wrap"><div class="glass rows">
  <a class="row" href="https://twin.unykorn.org/catalog"><b>API catalog</b><span class="muted">All 360 endpoints with prices, schemas and live examples</span>{icon('code')}</a>
  <a class="row" href="https://twin.unykorn.org/.well-known/x402"><b>x402 manifest</b><span class="muted">Machine-readable discovery for x402 clients</span>{icon('code')}</a>
  <a class="row" href="https://twin.unykorn.org/openapi.json"><b>OpenAPI</b><span class="muted">MPP discovery with x-payment-info on every operation</span>{icon('code')}</a>
  <a class="row" href="https://github.com/FTHTrading/genesis402-agent-kit"><b>Agent kit on GitHub</b><span class="muted">MCP server plus Node and Python payers for Base, XRPL and Stellar</span>{icon('code')}</a>
  <a class="row" href="https://registry.modelcontextprotocol.io/v0/servers?search=genesis402"><b>MCP Registry</b><span class="muted">io.github.FTHTrading/genesis402-mcp</span>{icon('link')}</a>
  <a class="row" href="https://glama.ai/mcp/connectors/io.github.FTHTrading/genesis402-mcp"><b>Glama</b><span class="muted">Connector listing with health checks and tool scores</span>{icon('link')}</a>
  <a class="row" href="https://twin.unykorn.org/status"><b>Status</b><span class="muted">The rail's own health report, every 5 minutes</span>{icon('clock')}</a>
  <a class="row" href="https://twin.unykorn.org/receipts"><b>Receipts</b><span class="muted">Public feed of paid calls</span>{icon('proof')}</a>
</div></div></section>
""")

PAGES["company.html"] = ("Company — UnyKorn",
"UnyKorn LLC is a team of infrastructure builders. We design, build and install the rails regulated money and real-world assets move on.", f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <div class="eyebrow plain">Company</div>
    <h1 style="margin-top:14px">We build the rails, then <em>hand you the keys.</em></h1>
    <p class="lead" style="margin-top:18px">UnyKorn is a team of infrastructure builders. We design, build and install the systems that regulated money, real-world assets and AI agents run on, stood up in the client's own name and verifiable on public ledgers.</p>
  </div>
  <div class="crest-big">{CREST}</div>
</div></section>
<section style="padding-top:0"><div class="wrap grid g2">
  <div class="glass card"><div class="k">What we are</div><h3>A technology rails provider</h3><p>We license software, build systems, wire custody and settlement, and make every step verifiable.</p></div>
  <div class="glass card"><div class="k">What we are not</div><h3>Not a bank or an issuer</h3><p>Not a bank, broker-dealer, exchange, custodian, trustee, transfer agent, adviser or money transmitter. We issue no tokens and never hold client funds.</p></div>
</div></section>
<section><div class="wrap">
  <div class="sec-head"><h2>How we work</h2></div>
  <div class="grid g4">
    <div class="card glass"><div class="k">01</div><h3>Scope</h3><p>A five-day sprint and a fixed-price plan.</p></div>
    <div class="card glass"><div class="k">02</div><h3>Paper</h3><p>NDA, engagement letter, KYB in your name.</p></div>
    <div class="card glass"><div class="k">03</div><h3>Build</h3><p>Your instance, custody connector and rails.</p></div>
    <div class="card glass"><div class="k">04</div><h3>Hand over</h3><p>You hold the keys. We keep it running if you want.</p></div>
  </div>
</div></section>
<section id="contact"><div class="wrap">
  <div class="glass hi card" style="padding:36px">
    <h2>Talk to UnyKorn</h2>
    <p class="lead" style="margin-top:10px">Tell us what you want to build. We reply within one business day.</p>
    <div class="grid g3" style="margin-top:22px">
      <a class="card glass" href="https://hire.unykorn.ai">{icon('services')}<h3>Services</h3><p>Fixed-price packages.</p><span class="go">hire.unykorn.ai →</span></a>
      <a class="card glass" href="https://order.unykorn.ai">{icon('capital','blue')}<h3>Engagements</h3><p>Start scoping.</p><span class="go">order.unykorn.ai →</span></a>
      <a class="card glass" href="mailto:kevan.burns@fthtrading.com">{icon('link')}<h3>Email</h3><p>Kevan Burns, Founder &amp; CEO.</p><span class="go">Send an email →</span></a>
    </div>
  </div>
</div></section>
""")

# ------------------------------------------------------------------ write
if os.path.exists(DIST):
    shutil.rmtree(DIST)
os.makedirs(os.path.join(DIST, "assets"))
for f in os.listdir(os.path.join(ROOT, "assets")):
    shutil.copy(os.path.join(ROOT, "assets", f), os.path.join(DIST, "assets", f))
shutil.copy(os.path.join(ROOT, "data/systems.json"), os.path.join(DIST, "systems.json"))
for page, (title, desc, body) in PAGES.items():
    open(os.path.join(DIST, page), "w").write(layout(page, title, desc, body))
print("built", len(PAGES), "pages ->", DIST)
