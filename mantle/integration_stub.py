"""Mantle "AI Alpha & Data" bot — signal-only wrapper around the SMT brain.

NOT imported by the main package or tests. Whale/on-chain/regime personas → JUDGE →
≤500-char Discord/Telegram alert, plus the ERC-8004 agent-card shape. No execution.
External pieces (data API, ERC-8004 mint, Telegram) are TODO.
"""

from __future__ import annotations
from typing import Any, Dict

from smt.personas.judge import JudgePersona
from smt.personas.whale import WhalePersona
from smt.personas.onchain import OnChainPersona
from smt.personas.regime import RegimePersona
from smt.personas.flow import FlowPersona

ALPHA_PERSONAS = [WhalePersona(), OnChainPersona(), RegimePersona(), FlowPersona()]


def onchain_adapter(symbol: str) -> Dict[str, Any]:
    """Map a free/paid on-chain source onto SMT's whale/onchain context dicts."""
    # TODO: Whale Alert public feed / Dune query / Nansen Smart Money net-flow.
    return {
        "whale_data": {},        # TODO large-transfer + smart-money labels
        "onchain_signal": {},    # TODO net-flow / accumulation signal
        "regime": {symbol: "NORMAL"},
        "fear_greed": 50,
    }


def alpha_alert(symbol: str) -> Dict[str, Any]:
    """Produce one smart-money alert with a ≤500-char 'why' (the XAI payload)."""
    ctx = onchain_adapter(symbol)
    votes = JudgePersona.votes_from_personas(ALPHA_PERSONAS, symbol, ctx)
    d = JudgePersona().decide(symbol, votes, ctx)
    why = f"{symbol} {d.action} ({d.confidence:.0%}): " + " · ".join(
        f"{k} {v.direction}" for k, v in votes.items() if v.direction != "NEUTRAL"
    )
    return {"symbol": symbol, "action": d.action, "why": why[:500]}


def post_alert(alert: Dict[str, Any]) -> None:
    # TODO: reuse v4.trade_alert_logger Discord webhook; mirror to Telegram.
    ...


def erc8004_agent_card() -> Dict[str, Any]:
    """The on-chain identity descriptor (points to off-chain endpoints + reputation)."""
    return {
        "name": "Smart Money Trading — Alpha Agent",
        "skills": ["smart-money-tracking", "onchain-anomaly", "regime-detection"],
        "endpoints": {"a2a": "TODO", "mcp": "TODO"},
        "reputation": {"metric": "alert direction accuracy (+2h/+4h)", "source": "logged"},
        # TODO: mint ERC-721 identity NFT (testnet) pointing to this card.
    }
