"""BNB Hack adapter shapes — thin wrappers around the SMT brain (`smt.*`).

NOT imported by the main package or tests (hackathons/ is excluded from the build).
This is the integration skeleton: a CMC-data adapter that feeds the existing personas,
plus a Trust-Wallet-Agent-Kit execution adapter that mirrors ExecutionClient's surface.
External SDKs (CMC Agent Hub, TWAK) are marked TODO — wire during the build window.
"""

from __future__ import annotations
from typing import Any, Dict

# Reused, unchanged, from the main SMT brain:
from smt.personas.judge import JudgePersona
from smt.personas.flow import FlowPersona
from smt.personas.technical import TechnicalPersona
from smt.personas.regime import RegimePersona
from smt.core.risk import RiskGate


# ── Track 2: CoinMarketCap data → the context dicts the personas already read ──
def cmc_adapter(symbol: str) -> Dict[str, Any]:
    """Map CMC Agent Hub fields onto SMT's context signal dicts.

    Personas read context["flow_signal"][sym] / ["technical_signal"][sym] / etc., so the
    brain is untouched — we only translate the data source.
    """
    # TODO: pull from CMC Agent Hub (MCP / x402 / CLI): funding, F&G, derivatives, OHLCV.
    fng = 50          # TODO cmc.fear_and_greed()
    funding = 0.0     # TODO cmc.funding_rate(symbol)
    return {
        "fear_greed": fng,
        "funding_rates": {symbol: funding},
        "flow_signal": {},        # TODO derive from CMC derivatives/orderbook proxy
        "technical_signal": {},   # TODO derive from CMC OHLCV
        "regime": {symbol: "NORMAL"},
        "prices": {},             # TODO cmc.price(symbol)
    }


def strategy_spec(symbol: str) -> Dict[str, Any]:
    """Track 2 deliverable: a backtestable strategy spec (no live execution)."""
    ctx = cmc_adapter(symbol)
    personas = [FlowPersona(), TechnicalPersona(), RegimePersona()]
    votes = JudgePersona.votes_from_personas(personas, symbol, ctx)
    decision = JudgePersona().decide(symbol, votes, ctx)
    return {
        "symbol": symbol,
        "action": decision.action,
        "confidence": decision.confidence,
        "reason": decision.reasoning,
        "votes": {k: (v.direction, v.confidence) for k, v in votes.items()},
        "risk": {"fee_floor": "net>fees (hard)", "drawdown_cap_pct": 30},
    }


# ── Track 1: TWAK execution adapter — same surface as smt.core.execution ──
class TWAKExecutionAdapter:
    """Mirrors ExecutionClient.place/close, but signs + executes on BSC via Trust Wallet.

    Self-custodial: keys stay with the user; the agent signs each tx locally (TWAK
    autonomous mode) inside guardrails. Drop-in sibling to the WEEX adapter.
    """

    def __init__(self, risk: RiskGate | None = None):
        self.risk = risk or RiskGate()
        # TODO: init TWAK client (local signer), token allowlist, per-trade/daily limits.

    def place(self, plan) -> Dict[str, Any]:
        # TODO: twak.sign_and_send(reduce_only=False, ...) → return {tx_hash, ...}
        return {"executed": False, "todo": "TWAK BSC place"}

    def close(self, symbol: str, side: str) -> Dict[str, Any]:
        # TODO: twak.sign_and_send(reduce_only=True, ...)
        return {"closed": False, "todo": "TWAK BSC close"}
