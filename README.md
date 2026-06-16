# Smart Money Trading (SMT) · The Turing Test 2026 (Mantle)

> **See the smart money. Understand the move.** A *transparent*, multi-persona AI agent for crypto:
> six specialist personas (order-flow · technical · on-chain/whale · sentiment · regime) + a learned
> **Judge** turn market + on-chain data into one **auditable** decision — with a plain-English "why"
> on every call. **Tracks:** AI Alpha & Data (Mirana) · AI Trading & Strategy (BGA).

**The thesis:** retail gets black-box signals they can't trust. SMT's edge isn't a secret indicator —
it's **a decision you can audit**, with performance **verifiable on-chain** (no need to expose the
strategy's private parameters).

---

## Why this wins the rubric (transparency · verifiability · risk)
| What judges score | What SMT does |
|---|---|
| **Verifiability & auditability** (Mirana 15 / BGA 7.5) | white-box persona votes + a **counterfactual faithfulness check** (flip a vote → the decision must move, or the "why" is rejected) + an **on-chain accuracy reputation** |
| **Risk management / anti-overfitting** (Mirana 8 / BGA 7.5) | validation gates — **Deflated Sharpe, PBO, CPCV, conformal** (`smt/learning/validation/`) reject overfit configs *before* they ship; fee-floor + drawdown guardian + live-PBO halt |
| **Innovation & technical depth** (Part A + Part B) | a from-scratch learning loop (TPE Bayesian opt + regime-aware contextual bandit) + a Mantle on-chain decision registry |
| **Transparency / "better systems, not highest PnL"** (BGA ethos) | every decision — *and every "wait"* — is logged with its reasoning; reduces the retail↔institutional information gap |

## Verify it yourself (no API keys needed)
```bash
pip install pytest
pytest -q                                          # 193 passing — incl. the validation gates + faithfulness
python3 mantle/alert_bot.py # offline demo: personas → Judge → a ≤500-char "why" alert
```
- Validation gates (Session F): `smt/learning/validation/{dsr,pbo,fdr,cpcv,conformal,kde,gate}.py`
- Faithfulness + input-cascade: `smt/learning/faithfulness.py` · ground-truth +2h/+4h join: `smt/learning/groundtruth.py`
- Architecture + Mermaid diagrams: **`docs/ARCHITECTURE.md`** (§9 = the validation/faithfulness visuals)

## On-chain (Mantle)
- Contract: **`mantle/contracts/SMTAgentRegistry.sol`** — ERC-8004-style identity
  + reputation + **`recordDecision`** (the AI function callable on-chain) + `gradeDecision` (reputation
  from realized +2h/+4h accuracy). Deploy/verify runbook + the Python bridge (`onchain.py`) are in that folder.
- Deployed address: _added on deploy (Mantle Sepolia/mainnet)._

## Live & links
- **Public dashboard (SMT World):** https://jannetekka.github.io/smt-mantle/
- **X:** https://x.com/JTechSMT · built solo by [@EkkaJanny96](https://x.com/EkkaJanny96)

## Open vs private (the alpha boundary)
The **architecture, learning approach, XAI, and validation methodology are fully open** (this repo).
The **tuned/learned parameters, per-pair research, and raw PnL/equity curve are kept private** — they're
the edge. Judges verify performance from the **on-chain accuracy reputation + the open method**, not
from an exposed track record.
