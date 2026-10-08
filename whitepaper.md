# UNYKORN: THE ZERO-FEE PAYMENT NETWORK
## A White Paper on Sovereign Digital Asset Infrastructure

**Version 1.0 | October 2026**
**UnyKorn LLC | Wyoming**
**twin.unykorn.org**

---

## 1. EXECUTIVE SUMMARY

UnyKorn is a sovereign payment network that eliminates the fee stack of traditional banking by replacing correspondent banks, wire desks, and card processors with on-chain settlement, passkey wallets, and AI agents. The result: a $50,000 transfer that costs a bank $810 and three business days costs UnyKorn $0.03 and two seconds.

The network is funded by accredited investors who deposit USDC into a yield-bearing vault. Investors earn on-chain yield plus a share of network revenue. Clients pay nothing. The network eats its own cost.

---

## 2. THE PROBLEM: THE BANKING FEE STACK

A single $50,000 domestic wire today:

| Cost Component | Amount |
|---|---|
| Outgoing wire fee | $30 |
| FX spread (1.5%) | $750 |
| Intermediary bank fee | $15 |
| Receiving bank fee | $15 |
| **TOTAL** | **$810** |
| Settlement time | 1-3 business days |

At $1M/month in volume, that is $11,200/month or $134,000/year in pure leakage. At $5M/month, $56,000/month or $672,000/year.

Card processing adds another layer: $100K/month in card spend generates $2,900 in interchange, partially offset by rewards but still a permanent tax on every transaction.

The root cause is structural. Every dollar moving through the banking system passes through multiple institutions, each taking a toll. The toll is not a bug. It is the business model.

---

## 3. THE UNYKORN ARCHITECTURE

### 3.1 The Vault (Custody Layer)

- A Safe multisig on Base, controlled by hardware wallet keys plus phone passkeys
- Accredited investors deposit USDC; the vault earns yield on idle float (currently ~3.43% net on Morpho Steakhouse)
- The vault is the institution. There is no bank account behind it.

### 3.2 The Phone Wallet (Client Layer)

- Expo/React Native app, one codebase for iPhone and Android
- Keys live in the Secure Enclave (iPhone) or StrongBox (Android)
- Face ID via expo-local-authentication; passkeys via react-native-passkey
- Saved recipients, auto-send limits, and spending caps stored on-device
- NFC tag (YubiKey 5 NFC or NTAG424) as the cold-vault unlock key

### 3.3 Chuck (Agent Layer)

- An ERC-8004 registered agent with a single job: sending money to saved people
- Wake word "Hey Chuck" via Picovoice Porcupine
- Voice match via Picovoice Eagle (runs as local Python service)
- Speech-to-text via Apple Speech / on-device Whisper
- Session keys with spending caps: under the cap, instant send; over the cap, Face ID
- Every send posts its transaction hash to Chuck's 8004 record

### 3.4 The Rail (Settlement Layer)

- 370 endpoints across Base, Solana, XRPL, Stellar, and Polygon
- x402 v2 payment protocol: HTTP 402 challenge, signed USDC authorization, instant settlement
- Multi-rail routing picks the cheapest chain per transaction
- MCP server (npx genesis402-mcp) for developer distribution
- Ranked 7th of 2,028 sellers in the Coinbase x402 Bazaar by endpoints

### 3.5 The Off-Ramp (Fiat Edge)

- POST /v1/offramp/session on twin.unykorn.org
- Converts USDC to fiat via licensed partner (FiatDock-style) or self-hosted bank partner
- ACH delivery in 1-2 business days; receipt text with ACH trace number
- Minimum $50 equivalent per conversion
- $0.01 session fee, charged only on successful settlement

---

## 4. THE ZERO-FEE MODEL

### 4.1 Fee Stack Collapse

| Traditional Cost | UnyKorn Cost | Mechanism |
|---|---|---|
| Wire fee $30 | $0 | No wire desk |
| FX spread $750 | $0 | USDC IS the dollar |
| Intermediary bank $15 | $0 | No correspondent banks |
| Receiving bank $15 | $0 | ACH from own account / on-chain only |
| Gas | $0.02 | Sponsored via paymaster |
| Session fee | $0.01 | Absorbed at scale |
| Off-ramp 0.5% | $0 | Rebated from investor yield |

On-chain-only send: **$0.03 total.**

### 4.2 Investor-Provided Liquidity

An accredited investor deposits $500,000 USDC:

- Vault yield at 3.43%: $17,150/year = $1,429/month
- That yield covers ~6 off-ramp sends of $50K each per month
- Investor also receives 20% of network revenue from 22 agents + 370 endpoints
- At $100K/month network volume (0.5% blended fees), investor earns $100/month from fees alone, plus yield: ~3.7% APY total
- Break-even off-ramp volume: ~$286K/month. Below that, UnyKorn subsidizes. Above that, pure profit.

### 4.3 The Investor Pitch

"Deposit $500K USDC. Earn 3.43% vault yield plus 20% of all network fees. Your capital funds the liquidity that makes client sends free. No bank. No FDIC. No correspondent. Pure on-chain yield with a revenue share on top."

---

## 5. SECURITY MODEL

Two rules, enforced at the protocol level:

1. **Voice starts a send. Voice never finishes one.** Caller ID can be faked; voices can be cloned from a short clip. Voice-only sends work only on an unlocked phone and under the auto-send cap. Face ID covers anything larger.

2. **Sending your own or UnyKorn's money needs no license. Sending clients' money for them is money transmission** and routes through a licensed partner or self-hosted compliance layer.

Additional controls:

- NFC tap as physical second factor for cold-vault unlocks
- Session keys with hard spending caps
- Every transaction logged to the agent's 8004 record for auditability
- KYT screening on facilitator settlements

---

## 6. THE BUSINESS MODEL

### 6.1 Revenue Streams

1. **Network fees**: 0.5% blended across 370 endpoints (counterparty reports $0.25, entity screens $0.01, deal scans $0.05, sanctions screens $0.02)
2. **Off-ramp fees**: 0.5% on fiat conversions (rebated to clients via investor yield)
3. **Investor spread**: the gap between vault yield earned and yield paid out
4. **Agent subscriptions**: $29/month or $299/year for Chuck access
5. **Pay-per-use x402**: $0.10/send or monthly passes for API consumers

### 6.2 Cost Structure

- Telnyx SIMs: $2/month recurring per active SIM (the real tax on small fleets)
- Gas: sponsored via paymaster
- Facilitator: Coinbase CDP free tier (1,000 tx/month), then $0.001/tx
- Infrastructure: Vercel, QuickNode, Alienware brain

---

## 7. ROADMAP

**Phase 1 (Current):** Testnet deployment on Base Sepolia. Phone wallet skeleton, Chuck intent parser, off-ramp endpoint skeleton, 8004 registration.

**Phase 2:** Mainnet $1 sends between own wallets. Telnyx SIM registration (SIMs ending 6476 and 6484). Voice AI webhook on the Alienware.

**Phase 3:** Licensed off-ramp partner integration. ACH origination. First accredited investor deposit. Investor yield + revenue share live.

**Phase 4:** Self-hosted money transmitter compliance. Own bank partner. Full fee collapse. Network revenue share at scale.

**Phase 5:** Closed-loop card network (BIN sponsor) if open-loop becomes necessary. Otherwise, stay on-chain-only and let the edges stay thin.

---

## 8. THE ONE-LINER

Traditional banking is a toll road with four toll booths on every trip. UnyKorn is a private road with no booths, funded by investors who earn yield for providing the pavement.

---

## 9. CONTACT

UnyKorn LLC
Wyoming
twin.unykorn.org
troptionsmint.com

---

*This document is for informational purposes. It does not constitute an offer to sell securities. Accredited investor status and regulatory compliance are required before any investment. Legal counsel should be engaged before launching money transmission services.*
