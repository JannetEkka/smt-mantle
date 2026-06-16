# hackathons/ — SMT on every platform, one brain

> **Principle: ONE SMT brain, thin per-platform adapters.** These folders do **not** fork the
> codebase. The personas → JUDGE → learning → XAI engine lives in `smt/` (single source of truth);
> each folder is a thin wrapper that **imports `smt.*`** and adds only the platform-specific piece
> (a data source, an execution adapter, an agent/payment wrapper). This is *why* SMT is flexible
> enough for any hackathon — and it keeps the main SMT world untouched.
>
> **Maintenance (CLAUDE.md contract):** when a session changes a component a folder reuses, update
> that folder's "Components reused" manifest + stub in the same PR.
> **Last updated:** 2026-06-16 (Session F — Mantle 2-track update + CRITERIA.md).

---

## Targets (operator-selected 2026-06-14)

| Folder | Hackathon | Prize | Deadline | Fit / what we ship |
|---|---|---|---|---|
| `bnb-ai-trading-agent/` | BNB Hack: AI Trading Agent (CMC × Trust Wallet) | $36k | **2026-06-21** | Track 2 Strategy Skill (drop-in) + Track 1 live BSC agent (TWAK adapter) |
| `mantle-turing-test/` | Mantle Turing Test 2026 — Phase 2 | $100k | DoraHacks — **confirm (old 2026-06-15 is past)** | **2 tracks entered:** Alpha & Data (Mirana, ship-ready) + Trading & Strategy (Bybit+BGA, on-chain stretch). Submission repo: `smart-money-trading`. Rubric → `mantle-turing-test/CRITERIA.md` |
| `croo-agent/` | CROO Agent Hackathon | ~$10.2k | **2026-07-12** | Personas as paid, A2A-callable agents via CAP |

*Operator: "screw deadlines, do our best." Mantle entered TWO tracks (Alpha & Data = ship-ready
signal product; Trading & Strategy = the on-chain/Bybit stretch). BNB has the most code-reuse value.*

---

## Alpha boundary (public repo, private edge)

All require public/open-source repos. The moat is **not** the architecture (multi-agent + judge + RL
is a known, respectable pattern judges *reward*). The moat is **(a)** per-pair research
(`docs/research/`), **(b)** the *learned* params (`v4/learned_params.json` + its corpus), **(c)** the
specific calibrated thresholds / HARD-BLOCK cells, **(d)** the **WEEX-verified Streamlit dashboard +
raw simulated funds / PnL ledger / per-version journey**. **Keep all of those private.**

**Public frontend = GitHub Pages `https://jannetekka.github.io/smart-money-trading/` (curated SMT
World) — NEVER the Streamlit dashboard** (that one is WEEX-linked and shows funds/PnL/versions =
alpha). Judges get verifiability from the **on-chain +2h/+4h accuracy reputation + the open
methodology** (validation gates, faithfulness), NOT from the equity curve. Submit the brain + XAI
story + on-chain proof; never the tuned numbers or the raw PnL.

---

## Shared submission blocks (paste-ready; folders note deltas only)

### Details
> **Smart Money Trading (SMT)** is a *transparent*, multi-persona AI trading system for crypto.
> Six specialist agents — order-flow, technical, on-chain/whale, sentiment, market-regime, and a
> learned **Judge** — each cast a confidence-weighted vote; the Judge aggregates them into a single,
> auditable decision. A learning loop (Bayesian optimization + a regime-aware contextual bandit,
> seeded offline from the system's own logged history) tunes the engine from realized outcomes. An
> un-disableable fee-floor plus per-pair, multi-lane exit discipline converts signals into PnL, and
> an **explainability layer** — white-box persona votes + a counterfactual *faithfulness* check —
> logs every trade *and every "wait"* with its reason (≤500-char "why" on each decision). The edge
> we sell isn't a secret indicator; it's **a decision you can audit.**

### About / Team
> **One-person team — Jannet Akanksha Ekka.** Google Cloud AI Engineer, 4+ years enterprise
> software at Deloitte, then a deliberate move into AI/ML/GenAI and agentic systems (Rank 1, 4.09/5
> GPA, PG AI/ML). Across 2026 she designed and built SMT v6.1 end-to-end: a multi-persona quant
> engine, a Judge aggregator with learned per-pair/per-regime weighting, a from-scratch learning
> stack (TPE Bayesian optimization + Thompson-sampling contextual bandit + a fat-tail-aware reward +
> validation gates: Deflated Sharpe / PBO / CPCV / conformal), and an XAI layer (white-box votes +
> counterfactual faithfulness). Fluent in Vertex AI / BigQuery ML, MLOps, and the emerging agent
> stack (MCP, A2A/AP2, x402, ERC-8004). Builds in the open — losses logged as loudly as wins.

### How it works (judge-friendly)
1. **Read** — 6 personas turn market + on-chain + sentiment data into confidence-weighted votes.
2. **Decide** — a learned Judge aggregates them (raw-judge bypass above a confidence floor; a
   HARD-BLOCK mask vetoes known-catastrophic regimes).
3. **Size & gate** — a regime bandit scales conviction by historical profitability; an
   un-disableable fee floor + learnable sizing finalize the order.
4. **Learn & explain** — every decision is logged with its full reasoning; a weekly optimizer
   refit + faithfulness check keeps weights honest before they ship.
