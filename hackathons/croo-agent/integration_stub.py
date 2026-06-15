"""CROO Agent Hackathon — a CAP-callable, paid agent wrapping one SMT persona.

NOT imported by the main package or tests. Shows the shape: a persona becomes a paid
A2A service (pay-per-call in USDC via CAP/x402), and the Judge agent can hire the persona
agents. CAP/x402 SDK calls are TODO.
"""

from __future__ import annotations
from typing import Any, Dict, List

from smt.personas.judge import JudgePersona
from smt.personas.regime import RegimePersona
from smt.personas.flow import FlowPersona
from smt.personas.whale import WhalePersona
from smt.personas.base import Persona


class PaidPersonaAgent:
    """Wrap any SMT persona as a CAP-callable, pay-per-call A2A agent."""

    def __init__(self, persona: Persona, price_usdc: float = 0.05):
        self.persona = persona
        self.price_usdc = price_usdc

    def manifest(self) -> Dict[str, Any]:
        return {
            "name": f"SMT {self.persona.name} agent",
            "price_usdc_per_call": self.price_usdc,
            "protocol": "CAP / A2A",
            "returns": "{direction, confidence, reasoning}",
        }

    def call(self, symbol: str, ctx: Dict[str, Any], payment_proof: Any = None) -> Dict[str, Any]:
        # TODO: verify CAP/x402 payment_proof (HTTP 402 → settle USDC) before serving.
        vote = self.persona.analyze(symbol, ctx)
        return {
            "agent": self.persona.name,
            "direction": vote.direction,
            "confidence": vote.confidence,
            "why": (vote.reasoning or "")[:500],
        }


class JudgeAgent:
    """Orchestrator: hires the persona agents over A2A, aggregates, returns the 'why'."""

    def __init__(self, agents: List[PaidPersonaAgent]):
        self.agents = agents
        self.judge = JudgePersona()

    def decide(self, symbol: str, ctx: Dict[str, Any]) -> Dict[str, Any]:
        # TODO: each call pays the sub-agent (A2A composability → network effect).
        votes = {}
        for a in self.agents:
            r = a.call(symbol, ctx)
            from smt.personas.base import PersonaVote
            votes[a.persona.name] = PersonaVote(r["direction"], r["confidence"], r["why"])
        d = self.judge.decide(symbol, votes, ctx)
        return {"symbol": symbol, "action": d.action, "confidence": d.confidence, "why": d.reasoning[:500]}


def build_store_listing() -> List[Dict[str, Any]]:
    agents = [PaidPersonaAgent(RegimePersona()), PaidPersonaAgent(FlowPersona()), PaidPersonaAgent(WhalePersona())]
    return [a.manifest() for a in agents]
