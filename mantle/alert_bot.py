"""SMT AI Alpha bot — Turing Test 2026 (AI Alpha & Data track).

Reuses the SMT brain (``smt.*``) and adds ONLY: a ≤500-char alert formatter, a
Discord/Telegram broadcast, and an optional on-chain decision record. No new
trading logic — the personas + Judge already decide.

Flow:  context → personas vote → JudgePersona.decide → ≤500-char "why" alert
       → Discord/Telegram → (optional) Mantle on-chain record via onchain.MantleBridge.

Run live:  python3 mantle/alert_bot.py
(personas degrade to NEUTRAL with no API keys, so the demo runs offline.)
"""

from __future__ import annotations
import json
import logging
import os
import sys
import urllib.request
from typing import Any, Dict, List, Optional

# Make `smt` importable when run directly — works whether this file lives in
# mantle/ (main repo) or top-level mantle/ (submission repo).
_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (os.path.join(_here, ".."), os.path.join(_here, "..", "..")):
    if os.path.isdir(os.path.join(_cand, "smt")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

from smt.personas.base import PersonaVote  # noqa: E402
from smt.personas.judge import JudgePersona  # noqa: E402

log = logging.getLogger("smt.hackathons.mantle.alert_bot")

ALERT_MAX_CHARS = 500
_ARROW = {"LONG": "🟢 LONG", "SHORT": "🔴 SHORT", "WAIT": "⏸ WAIT", "BLOCK": "⛔ BLOCK"}


def _top_drivers(votes: Dict[str, PersonaVote], k: int = 3) -> List[str]:
    """The k most-confident non-neutral personas, named + signed (the 'why')."""
    ranked = sorted(
        [(n, v) for n, v in (votes or {}).items()
         if v is not None and getattr(v, "direction", "NEUTRAL") in ("LONG", "SHORT")],
        key=lambda nv: float(getattr(nv[1], "confidence", 0.0) or 0.0), reverse=True,
    )
    out = []
    for name, v in ranked[:k]:
        out.append(f"{name.capitalize()} {v.direction.lower()} {int(round(v.confidence * 100))}%")
    return out


def format_alert(pair: str, decision: Any, votes: Dict[str, PersonaVote],
                 max_chars: int = ALERT_MAX_CHARS) -> str:
    """Build the transparency-first alert — always ≤ max_chars (the contract's reasoningHash text)."""
    action = getattr(decision, "action", "WAIT")
    conf = int(round(float(getattr(decision, "confidence", 0.0) or 0.0) * 100))
    head = f"🚨 SMT {_ARROW.get(action, action)} {pair} · conf {conf}%"
    drivers = _top_drivers(votes)
    why = ("driven by " + ", ".join(drivers)) if drivers else "no persona conviction"
    tail = getattr(decision, "reasoning", "") or ""
    alert = f"{head}\nWhy: {why}.\n{tail}".strip()
    if len(alert) > max_chars:
        alert = alert[: max_chars - 1].rstrip() + "…"
    return alert


def post_discord(webhook_url: str, content: str) -> bool:
    """POST the alert to a Discord webhook. Returns success; never raises."""
    try:
        req = urllib.request.Request(
            webhook_url, data=json.dumps({"content": content}).encode(),
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=10) as resp:
            return 200 <= resp.status < 300
    except Exception as exc:  # noqa: BLE001 — broadcast best-effort
        log.warning("[ALERT] Discord post failed: %s", exc)
        return False


def decide_and_alert(
    pair: str,
    votes: Dict[str, PersonaVote],
    context: Dict[str, Any],
    judge: Optional[JudgePersona] = None,
    bridge: Any = None,
    discord_webhook: Optional[str] = None,
) -> Dict[str, Any]:
    """Aggregate votes → Judge decision → ≤500-char alert → (broadcast) → (on-chain).

    Pure + offline by default: only posts to Discord if a webhook is passed, only
    writes on-chain if a (connected) bridge is passed.
    """
    judge = judge or JudgePersona()
    decision = judge.decide(pair, votes, context)
    alert = format_alert(pair, decision, votes)
    posted = post_discord(discord_webhook, alert) if discord_webhook else False
    tx = None
    if bridge is not None and decision.action in ("LONG", "SHORT"):
        tx = bridge.record_decision(pair, decision.action, decision.confidence, alert)
    return {"pair": pair, "action": decision.action, "confidence": decision.confidence,
            "alert": alert, "posted": posted, "tx": tx}


def _demo() -> None:
    """Offline demo: synthetic strong-FLOW LONG context → alert (no network)."""
    logging.basicConfig(level=logging.INFO)
    votes = {
        "flow": PersonaVote("LONG", 0.82, "order flow firmly bid"),
        "technical": PersonaVote("LONG", 0.7, "reclaimed the range high"),
        "whale": PersonaVote("LONG", 0.6, "accumulation wallet active"),
        "sentiment": PersonaVote("SHORT", 0.4, "crowd nervous"),
    }
    ctx = {"fear_greed": 55, "regime": {"BTC": "TRENDING_UP"}}
    webhook = os.getenv("DISCORD_WEBHOOK_B")          # optional
    bridge = None
    try:                                              # optional on-chain (needs web3+key)
        import importlib.util
        import sys as _sys
        here = os.path.dirname(os.path.abspath(__file__))
        spec = importlib.util.spec_from_file_location("smt_onchain", os.path.join(here, "onchain.py"))
        oc = importlib.util.module_from_spec(spec)
        _sys.modules["smt_onchain"] = oc                  # dataclasses need this before exec
        spec.loader.exec_module(oc)  # type: ignore
        b = oc.MantleBridge()
        bridge = b if b.available() else None
    except Exception:  # noqa: BLE001
        bridge = None
    out = decide_and_alert("BTCUSDT", votes, ctx, discord_webhook=webhook, bridge=bridge)
    print(out["alert"])
    print(f"\n[{len(out['alert'])} chars] action={out['action']} posted={out['posted']} tx={out['tx']}")


if __name__ == "__main__":
    _demo()
