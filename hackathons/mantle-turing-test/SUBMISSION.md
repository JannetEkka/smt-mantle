# How to submit SMT to the Turing Test 2026 (step-by-step)

> Plain runbook for the operator. Full rubric → `CRITERIA.md`. The code is built + tested; the steps
> **you** must do (deploy + record a video + fill the DoraHacks form) are marked 👤. Everything else is
> already in the repo.

**Submitting:** repo `https://github.com/JannetEkka/smart-money-trading` · tracks **AI Alpha & Data**
(primary) + **AI Trading & Strategy** · platform **DoraHacks**.
⚠ **Confirm the live deadline** on the DoraHacks page first — the old note (2026-06-15) is past.

---

## What you can submit at two levels
- **Minimum (Alpha & Data, signal-only):** the `alert_bot.py` Discord/Telegram bot + the public
  Streamlit dashboard + a demo video. No chain needed. Eligible for the Alpha & Data track + Community
  Voting + Best UI/UX. **Ships today.**
- **Full (unlocks Grand Champion + 20-Deploy + Trading & Strategy):** the above **+** deploy
  `contracts/SMTAgentRegistry.sol` to Mantle and record a few decisions on-chain. ~1 hour of the steps below.

---

## Step 1 — 👤 Deploy the contract to Mantle (for the full submission)
From `hackathons/mantle-turing-test/` (needs Node 18+):
```bash
npm install                                   # installs hardhat + toolbox
export MANTLE_PRIVATE_KEY=0xYOURTESTNETKEY     # a funded Mantle Sepolia key (get test MNT from the faucet)
npm run build                                  # compiles SMTAgentRegistry.sol
npm run deploy:testnet                         # prints: SMTAgentRegistry deployed: 0x....
npx hardhat verify --network mantleSepolia 0xDEPLOYED_ADDRESS   # verify on Mantle Explorer ✅
```
Get testnet MNT from the Mantle Sepolia faucet (see docs.mantle.xyz). Mainnet = `npm run deploy:mainnet`.

## Step 2 — 👤 Register the agent + record decisions on-chain
```bash
export SMT_REGISTRY_ADDRESS=0xDEPLOYED_ADDRESS
export MANTLE_RPC_URL=https://rpc.sepolia.mantle.xyz
pip install web3                               # only needed for the on-chain write
```
- Put `0xDEPLOYED_ADDRESS` into `agent_card.json` (`registry.contract`), host that JSON (GitHub raw / IPFS), then call `registerAgent(cardURI)` once (via the bridge or Mantle Explorer's write tab).
- Run `python3 alert_bot.py` — with `web3` + the env set, each LONG/SHORT decision calls
  `recordDecision(...)` on-chain (that's your **"≥1 AI function callable on-chain"** ✅). Without web3 it
  runs signal-only.

## Step 3 — 👤 Frontend + demo video
- Frontend: the live Streamlit dashboard `https://smt-aiquant-bot.streamlit.app/` (publicly accessible ✅, not localhost).
- Record a **≥2-min** video: dashboard tour → run `alert_bot.py` → show the Discord alert with its "why"
  → show the on-chain decision/tx on Mantle Explorer.

## Step 4 — 👤 Fill the DoraHacks submission
Use the paste-ready text in `BUIDL.md`. Provide:
- **Project:** Smart Money Trading (SMT) · **Category:** AI / Robotics · **Is it an AI Agent?** Yes.
- **Repo:** `https://github.com/JannetEkka/smart-money-trading` (open-source, README ✅).
- **Tracks:** AI Alpha & Data (primary) + AI Trading & Strategy.
- **Deployed contract address** (Step 1) — required for Grand Champion + the 20-Deploy award.
- **Demo video link** (Step 3) + **website** (the dashboard) + **vision** (≤256 chars, in `BUIDL.md`).

---

## 20-Project Deployment Award — SMT checklist
| Requirement | Status |
|---|---|
| Contract on Mantle mainnet/testnet | 👤 Step 1 (`SMTAgentRegistry.sol` ready) |
| Verified on Mantle Explorer | 👤 Step 1 (`hardhat verify`) |
| ≥1 AI function callable on-chain | ✅ `recordDecision(...)` (call it via Step 2) |
| Frontend publicly accessible | ✅ Streamlit dashboard (live) |
| Deployment address in DoraHacks submission | 👤 Step 4 |
| Demo video ≥2 min | 👤 Step 3 |
| Open-source repo + README (setup/arch/address) | ✅ repo + README (add the address after Step 1) |

## Don't-forget (the moat)
Keep the **tuned params + per-pair research private** (`v4/learned_params.json`, `docs/research/`) — the
public repo ships the brain + XAI + learning approach, never the calibrated numbers (`../README.md`
"Alpha boundary"). Open enough to win on engineering; private where the edge lives.
