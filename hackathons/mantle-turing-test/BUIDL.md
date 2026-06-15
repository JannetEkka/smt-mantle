# Turing Test Hackathon 2026 — BUIDL submission (paste-ready)

> Track target: **AI Alpha & Data** (smart-money tracking + on-chain anomaly detection via
> Telegram/Discord). Signal-only — no execution. Theme to lean on: **radical transparency**.

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
- GitHub: `https://github.com/JannetEkka/smt-weex-trading-bot`
- Project website: `https://smt-aiquant-bot.streamlit.app/`
- Demo video: *(optional — record a 2-min Streamlit + alert walkthrough; can add after submit)*
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
- **Honest track record.** Losses are logged as loudly as wins; the public dashboard shows per-pair
  PnL vs. buy-and-hold.
- **On-chain identity + reputation (Mantle).** The agent mints an **ERC-8004** identity (agent card
  + endpoints) and accrues an on-chain reputation from its logged +2h/+4h direction accuracy — a
  verifiable, decentralized record of performance, exactly the benchmark this hackathon is built on.

**Under the hood:** a from-scratch learning loop (TPE Bayesian optimization + a regime-aware
contextual bandit, seeded offline from its own logged history) tunes the engine from realized
outcomes; an un-disableable fee floor + per-pair, multi-lane discipline keep it grounded; validation
gates (Deflated Sharpe / PBO / CPCV / conformal) reject overfit configurations before they ship.

## Team
**One-person team — Jannet Akanksha Ekka.** Google Cloud AI Engineer; 4+ years enterprise software
at Deloitte, then a deliberate move into AI/ML/GenAI and agentic systems (Rank 1, 4.09/5 GPA, PG
AI/ML). Designed and built SMT v6.1 end-to-end — multi-persona engine, learned Judge, a from-scratch
learning + validation stack, and an XAI layer. Fluent in Vertex AI / BigQuery ML and the agent stack
(MCP, A2A/AP2, x402, ERC-8004).

## Contact
`jtech26smt@gmail.com` · LinkedIn (above) · X `@EkkaJanny96`

## Submission notes
- Open-source repo (public). **Tuned parameters / per-pair research kept private** (the edge);
  architecture, XAI, and learning approach are fully open.
- AI Alpha & Data track; signal-only (no on-chain execution); ERC-8004 identity on Mantle.
