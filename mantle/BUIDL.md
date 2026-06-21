# Turing Test Hackathon 2026 — BUIDL submission (paste-ready)

> Tracks entered (both; max 2 allowed): **AI Alpha & Data** (Mirana Ventures) — lead, smart-money +
> on-chain anomaly detection via Telegram/Discord, signal-only — and **AI Trading & Strategy** (Bybit +
> BGA) — on-chain extension (Bybit adapter + macro-REGIME Mantle contract). Theme: **radical
> transparency**. Official rubric: docs.byreal.io/turing-test-hackathon/evaluation-criteria.

---

## Profile

**BUIDL (project) name:**
Smart Money Trading (SMT)

**BUIDL logo:** the 480×480 PNG (double-ring badge, candles + whale fluke + circuit motif).

**Vision (problem it solves — ≤256 chars):**
> Retail traders get black-box crypto signals they can't trust. Smart Money Trading is a transparent AI agent: 6 personas track smart-money/whale moves, a learned Judge decides, and every call ships with its reasoning. Act and understand.

*(The longer narrative goes in the Details section below, not Vision.)*

**Category:** AI / Robotics

**Is this BUIDL an AI Agent?** **Yes**

**Links**
- GitHub (submission repo): `https://github.com/JannetEkka/smt-mantle`
- Project website: `https://jannetekka.github.io/smt-mantle/`
- Demo video: *(record a ≥2-min walkthrough: public SMT World dashboard → alert with its "why" → the on-chain decision on Mantle Explorer)*
- Social links: `https://x.com/JTechSMT` (SMT project) · `https://www.linkedin.com/in/jannet-akanksha-ekka-a18692122/`

---

## Details

**Smart Money Trading (SMT)** is a transparent, multi-persona AI agent for crypto. Six specialist
personas — **order-flow, technical, on-chain/whale, sentiment, market-regime**, and a learned
**Judge** — each cast a confidence-weighted vote, and the Judge aggregates them into one auditable
call. For the **AI Alpha & Data** track, SMT runs as a **smart-money + on-chain-anomaly signal bot**:
it watches large-wallet flows and exchange aggTrades, flags anomalies, and broadcasts them to
**Discord/Telegram** — each alert carrying a ≤500-character explanation of *which personas drove it
and why*.

**Why it fits the Turing Test's "radical transparency":**
- **White-box by design.** The decision *is* the weighted persona vote — there's no hidden layer to
  reverse-engineer. We also run a **counterfactual faithfulness check**: flip one persona's vote and
  confirm the decision moves the predicted way, so an attribution is only shipped if it's *real*.
- **Verifiable WITHOUT leaking the edge.** The agent's +2h/+4h direction accuracy is recorded
  on-chain as an auditable reputation, and the methodology (validation gates + faithfulness) is fully
  open — judges can verify performance and inspect the logic. The tuned parameters, equity curve, and
  version history stay private (the moat).
- **On-chain identity + reputation (Mantle).** The agent mints an **ERC-8004** identity (agent card
  + endpoints) and accrues an on-chain reputation from its logged +2h/+4h direction accuracy — a
  verifiable, decentralized record of performance, exactly the benchmark this hackathon is built on.

**Under the hood:** a from-scratch learning loop (TPE Bayesian optimization + a regime-aware
contextual bandit, seeded offline from its own logged history) tunes the engine from realized
outcomes; an un-disableable fee floor + per-pair, multi-lane discipline keep it grounded; validation
gates (Deflated Sharpe / PBO / CPCV / conformal) reject overfit configurations before they ship.

## Track record
SMT isn't vaporware: a live multi-persona daemon ran in **real time Jan–May 2026** — thousands of
executed decisions across 8 perpetual-futures pairs, every win *and* loss logged. That corpus is what
the learning loop trains on and the validation gates guard against (we treat honesty about drawdowns
as a feature). The raw equity curve + tuned parameters stay private (the edge); the method is open.

## Team
**One-person team — Jannet Akanksha Ekka.** Google Cloud AI Engineer; 4+ years enterprise software
at Deloitte, then a deliberate move into AI/ML/GenAI and agentic systems (Rank 1, 4.09/5 GPA, PG
AI/ML). Designed and built SMT v6.1 end-to-end — multi-persona engine, learned Judge, a from-scratch
learning + validation stack, and an XAI layer. Fluent in Vertex AI / BigQuery ML and the agent stack
(MCP, A2A/AP2, x402, ERC-8004).

## Contact
`jtech26smt@gmail.com` · LinkedIn (above) · X `@EkkaJanny96`

## Submission notes
- Open-source repo (public). **Tuned parameters / per-pair research / raw equity curve kept private**
  (the edge); architecture, XAI, and learning approach are fully open. SMT ran live Jan–May 2026 (see
  Track record) — verified by the open method + on-chain reputation, not an exposed ledger.
- Entered **AI Alpha & Data** (lead, signal-only) + **AI Trading & Strategy** (on-chain extension);
  ERC-8004 identity on Mantle. Grand Champion / 20-Deploy awards need Mantle deployment.
