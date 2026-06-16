# Turing Test Hackathon 2026 — official tracks, judging & awards

> Transcribed from the operator's brief (2026-06-16). Authoritative source:
> https://docs.byreal.io/turing-test-hackathon/evaluation-criteria · Judging-by-prize spreadsheet:
> https://docs.google.com/spreadsheets/d/1TMWhQ8cKp_1NF1ZelxtBGIF6l3bQZTA0ipjSREiqRhM/edit?gid=1857369098
> **$100K total.** Every track project can be executed by an AI agent end-to-end, or via AI-assisted / human-developed tools.

## Tracks (6) + title sponsors

| Track | Sponsor(s) | Description |
|---|---|---|
| **AI Trading & Strategy** ⬅ *entered* | Bybit + BGA | AI quant bots and macro-driven smart contracts, with Python and Solidity templates and Bybit API support. |
| **AI Alpha & Data** ⬅ *entered* | Mirana Ventures | Smart money tracking and on-chain anomaly detection bots via Telegram and Discord. |
| **AI x RWA** | Mantle Network | Dynamic yield strategies and automated risk management for assets including USDY and mETH, built on Mantle's RWA infrastructure. |
| **Consumer & Viral DApps** | Animoca Minds, OpenCheck, Animoca Brands | Gamified trading interfaces and shareable consumer applications. |
| **AI DevTools** | Tencent Cloud | Smart gas-optimisation tools and Mantle-specific audit assistants. |
| **Agentic Wallets & Economy** | Byreal | Agentic wallet economies built using the Byreal Skills CLI. |

**SMT entered AI Trading & Strategy + AI Alpha & Data (max 2 tracks allowed).**

## Judging process — two scorecards per judge
Every judge completes **two** scorecards per project; both must be submitted for a score to count.
1. **General scorecard** (all tracks) — Mantle's core dimensions: Technical, Ecosystem Fit, Business
   Potential, Innovation, User Experience.
2. **Track-specific scorecard** — customised by each track's title sponsor (their focus areas).

## Prizes

### Grand Champion (cross-track, highest honor)
Open to all tracks; must perform across all dimensions.

| Dimension | Weight | Description |
|---|---|---|
| Technical Depth | 30% | AI × on-chain integration, architecture completeness, code quality |
| Innovation | 25% | Originality; whether it proposes a new AI × Web3 paradigm |
| Mantle Ecosystem Contribution | 25% | Substantive use of Mantle + long-term ecosystem value |
| Product Completeness | 20% | Runnable demo, UX, scalability |

**Requirements:** deployed on **Mantle Network**; open-source repo + runnable demo + project pitch;
nominated from ≥1 track.

### By-track first prizes
Trading & Strategy (Bybit + BGA) · Alpha & Data (Mirana Ventures) · AI x RWA (Mantle Network) ·
Agentic Economy (Byreal) · DevTools (Tencent Cloud) · Consumer Viral DApp (Animoca Minds / OpenCheck /
Animoca Brands). Each scored on the track sponsor's own scorecard (the per-track grids in the brief).

### Community Voting
Entirely community-decided (greatest public appeal/reach). All submitted projects auto-eligible;
voting on **X**; most votes wins. Wins on: a clear/compelling demo (even for non-technical viewers),
resonance with real pain points, and community presence + shareability.

### Best UI/UX Award

| Dimension | Weight | Description |
|---|---|---|
| Visual Design | 30% | Aesthetic quality, design consistency, brand identity |
| Interaction & Flow | 30% | Smoothness, user guidance, responsiveness |
| AI Interaction Design | 25% | AI presented in a natural, user-friendly way |
| Accessibility | 15% | Beginner-friendliness; lowering the Web3 barrier |

**Requirements:** runnable frontend; demo video or public link.

### 20 Project Deployment Award (first-come, 20 spots, no judge scoring)
Meet ALL:
- **Technical:** contract deployed on Mantle Mainnet or Testnet; verified on Mantle Explorer; ≥1
  AI-powered function callable on-chain (agent trigger / inference written on-chain / automated execution).
- **Product:** frontend publicly accessible (not localhost); deployment address in the DoraHacks
  submission; demo video ≥2 min walking the core use case.
- **Docs:** open-source GitHub repo with README (setup, architecture, deployed contract address).

## What this means for SMT (gap → bridge)
SMT is off-chain Python today; the **Mantle-deployment requirement** gates Grand Champion + the
20-Deploy award. Bridge = the **ERC-8004 identity/reputation contract** (reputation from `groundtruth`
+2h/+4h accuracy) + a minimal on-chain decision/anomaly record → satisfies "≥1 AI function callable
on-chain." Per-track first prizes (esp. **Alpha & Data**, signal-only) are reachable off-chain; the
cross-track + deployment prizes need the Mantle piece. See this folder's `README.md` for the per-track
fit + plan.
