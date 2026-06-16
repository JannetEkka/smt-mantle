# The Turing Test Hackathon 2026 — tracks, judging requirements & criteria

> **Phase 2 "AI Awakening" · Mantle ecosystem · $100K total · submitted via DoraHacks.**
> Official rubric: https://docs.byreal.io/turing-test-hackathon/evaluation-criteria ·
> judging-by-prize sheet: https://docs.google.com/spreadsheets/d/1TMWhQ8cKp_1NF1ZelxtBGIF6l3bQZTA0ipjSREiqRhM
> *Transcribed from the operator's brief, 2026-06-16. If this drifts from the official page, the official page wins.*
> **Premise:** every track project may be executed end-to-end by an AI agent, or via AI-assisted / human-built tools.

---

## 1. Tracks (6) + title sponsors

| Track | Sponsor(s) | Description |
|---|---|---|
| **AI Trading & Strategy** ⬅ *SMT entered* | Bybit + BGA | AI quant bots and macro-driven smart contracts, with Python and Solidity templates and Bybit API support. |
| **AI Alpha & Data** ⬅ *SMT entered* | Mirana Ventures | Smart money tracking and on-chain anomaly detection bots via Telegram and Discord. |
| **AI x RWA** | Mantle Network | Dynamic yield strategies and automated risk management for assets including USDY and mETH, built on Mantle's RWA infrastructure. |
| **Consumer & Viral DApps** | Animoca Minds · OpenCheck · Animoca Brands | Gamified trading interfaces and shareable consumer applications. |
| **AI DevTools** | Tencent Cloud | Smart gas-optimisation tools and Mantle-specific audit assistants. |
| **Agentic Wallets & Economy** | Byreal | Agentic wallet economies built using the Byreal Skills CLI. |

**SMT entered AI Trading & Strategy + AI Alpha & Data (max 2 tracks per project).** A project must be
nominated from ≥1 track to be eligible for the Grand Champion.

---

## 2. Judging process — TWO scorecards per judge

Every judge submits **two** scorecards per project; **both must be submitted for a score to count.**

1. **General scorecard** (universal, all tracks) — Mantle's core dimensions:
   **Technical · Ecosystem Fit · Business Potential · Innovation · User Experience.**
2. **Track-specific scorecard** — customised by each track's **title sponsor**, reflecting that
   sponsor's focus areas + unique criteria (the per-track "Part a / Part b / Grade" grids in the brief).

---

## 3. Prizes & their criteria

### 3a. Grand Champion (highest honor, cross-track)
The project that best demonstrates excellence across technology, innovation, and ecosystem
contribution — regardless of track. Open to all tracks; must perform across **all** dimensions.

| Dimension | Weight | Description |
|---|---|---|
| Technical Depth | 30% | AI × on-chain integration, architecture completeness, code quality |
| Innovation | 25% | Originality; whether it proposes a new AI × Web3 paradigm |
| Mantle Ecosystem Contribution | 25% | Substantive use of Mantle + long-term value to the ecosystem |
| Product Completeness | 20% | Runnable demo, user experience, scalability |

**Requirements:** deployed on **Mantle Network** · open-source repo + runnable demo + project pitch ·
nominated from ≥1 track.

### 3b. By-track First Prize (per track, sponsor-scored)
Each track awards a first prize judged on the **title sponsor's own scorecard**:
Trading & Strategy (Bybit + BGA) · Alpha & Data (Mirana Ventures) · AI x RWA (Mantle Network) ·
Agentic Economy (Byreal) · DevTools (Tencent Cloud) · Consumer Viral DApp (Animoca Minds / OpenCheck /
Animoca Brands). *(The sponsor grids — "Part a / Part b / Grade" — live in the official sheet.)*

### 3c. Community Voting (public choice)
Decided entirely by the community — the project with the greatest public appeal and reach.
- **How it works:** all submitted projects are automatically eligible · voting is open to everyone on
  **X** · the project with the most votes wins.
- **What wins here:** a clear, compelling demo (even for non-technical viewers) · a solution that
  resonates with real pain points · strong community presence + shareability.

### 3d. Best UI/UX Award
Most outstanding user experience + interface design.

| Dimension | Weight | Description |
|---|---|---|
| Visual Design | 30% | Aesthetic quality, design consistency, brand identity |
| Interaction & Flow | 30% | Smoothness of interactions, user guidance, responsiveness |
| AI Interaction Design | 25% | Whether AI capabilities are presented in a natural, user-friendly way |
| Accessibility | 15% | Beginner-friendliness; lowering the Web3 barrier for new users |

**Requirements:** a runnable frontend interface · a demo video or publicly accessible link.

### 3e. 20 Project Deployment Award (first-come, 20 spots, NO judge scoring)
Awarded to the first 20 projects that clear every bar below (first-come, first-served):

- **Technical deployment**
  - ✅ Smart contract deployed on Mantle **Mainnet or Testnet**
  - ✅ Contract **verified** on Mantle Explorer
  - ✅ **≥1 AI-powered function callable on-chain** (agent trigger / inference result written on-chain / automated execution)
- **Product completeness**
  - ✅ Frontend demo **publicly accessible** (not localhost)
  - ✅ Deployment address included in the **DoraHacks** submission
  - ✅ Demo video **≥2 min** walking the core use case
- **Documentation**
  - ✅ Open-source GitHub repo with README (setup, architecture overview, deployed contract address)

> No judge scoring — but real bars. Meet all and the award is yours.

---

## 4. Requirements summary (what EVERY serious submission needs)
1. **Deployed on Mantle** (mainnet or testnet), contract **verified** on Mantle Explorer.
2. **Open-source GitHub repo** + README (setup, architecture, contract address).
3. **Runnable demo** — publicly accessible frontend (not localhost) + **demo video ≥2 min**.
4. **Project pitch** + nomination from ≥1 track; **deployment address in the DoraHacks submission.**

## 5. What SMT targets (fit → bridge)
- **AI Alpha & Data (Mirana)** — primary, ship-ready: smart-money + on-chain anomaly alerts to
  Discord/Telegram with a ≤500-char "why" (`alert_bot.py`).
- **AI Trading & Strategy (Bybit + BGA)** — on-chain extension (Bybit adapter + macro-REGIME contract).
- **Grand Champion + 20-Deploy** — unlocked by deploying `contracts/SMTAgentRegistry.sol` on Mantle
  (the `recordDecision` call = the on-chain AI function; reputation = +2h/+4h accuracy).
- **Community Voting + Best UI/UX** — NOT track-locked; the @JTechSMT voice + the Streamlit dashboard +
  the per-trade "why" cards target these directly.

See `README.md` (per-track fit + plan) and `SUBMISSION.md` (deploy runbook + step-by-step submit).
