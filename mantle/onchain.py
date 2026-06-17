"""Mantle on-chain bridge for SMT — Turing Test 2026.

Thin web3.py client over ``SMTAgentRegistry.sol``. The SMT brain stays off-chain
Python; this writes each Judge decision (and its graded +2h/+4h outcome) on-chain
so the agent accrues a verifiable reputation — the hackathon's "≥1 AI function
callable on-chain" bar.

Bare-container safe: web3 is imported LAZILY inside methods. With no web3 / no RPC
/ no key, ``available()`` is False and the alert bot runs SIGNAL-ONLY — never blocks.
The pure encoders (pair/direction/conviction) + the agent-card builder need no web3
and are unit-tested.
"""

from __future__ import annotations
import json
import logging
import os
from dataclasses import dataclass
from typing import Any, Dict, Optional

log = logging.getLogger("smt.hackathons.mantle.onchain")

# Mantle endpoints (verify current values at docs.mantle.xyz before mainnet).
MANTLE_SEPOLIA = {"rpc": "https://rpc.sepolia.mantle.xyz", "chain_id": 5003,
                  "explorer": "https://explorer.sepolia.mantle.xyz"}
MANTLE_MAINNET = {"rpc": "https://rpc.mantle.xyz", "chain_id": 5000,
                  "explorer": "https://explorer.mantle.xyz"}


# ── pure encoders (match the Solidity types; no web3 needed) ───────────────────

def pair_to_bytes32(pair: str) -> bytes:
    """'BTCUSDT' → 32-byte right-padded ASCII (the contract's bytes32 pair field)."""
    b = (pair or "").upper().encode()[:32]
    return b + b"\x00" * (32 - len(b))


def direction_to_int(direction: str) -> int:
    """LONG → +1, SHORT → -1, anything else (WAIT/BLOCK/NEUTRAL) → 0."""
    d = (direction or "").upper()
    return 1 if d == "LONG" else -1 if d == "SHORT" else 0


def conviction_to_bps(confidence: float) -> int:
    """JUDGE confidence (0..1) → basis points (0..10000), clamped."""
    return max(0, min(10000, int(round(float(confidence or 0.0) * 10000))))


def build_agent_card(
    *,
    registry_address: Optional[str] = None,
    agent_id: Optional[int] = None,
    discord: Optional[str] = None,
    network: str = "mantleSepolia",
) -> Dict[str, Any]:
    """ERC-8004 agent card (identity + endpoints + on-chain registry pointer)."""
    return {
        "name": "Smart Money Trading (SMT)",
        "description": ("Transparent multi-persona AI agent: smart-money / whale tracking + "
                        "on-chain anomaly detection, with a plain-English 'why' on every call."),
        "version": "6.1.0",
        "agentType": "ai-alpha-signal",
        "owner": "@EkkaJanny96",
        "skills": ["smart-money-tracking", "on-chain-anomaly-detection", "explainable-signals"],
        "endpoints": {
            "dashboard": "https://jannetekka.github.io/smt-mantle/",
            "repo": "https://github.com/JannetEkka/smt-mantle",
            "discord": discord or "<discord-invite-or-webhook>",
        },
        "registry": {"chain": network, "contract": registry_address or "<deployed-address>",
                     "agentId": agent_id},
        "reputation": "on-chain correct/graded from +2h/+4h direction accuracy",
        "transparency": "white-box persona votes + counterfactual faithfulness check",
    }


@dataclass
class OnchainConfig:
    rpc_url: str = MANTLE_SEPOLIA["rpc"]
    chain_id: int = MANTLE_SEPOLIA["chain_id"]
    registry_address: Optional[str] = None
    private_key: Optional[str] = None

    @classmethod
    def from_env(cls) -> "OnchainConfig":
        """Read RPC / registry / key from env (MANTLE_RPC_URL, SMT_REGISTRY_ADDRESS, MANTLE_PRIVATE_KEY)."""
        return cls(
            rpc_url=os.getenv("MANTLE_RPC_URL", MANTLE_SEPOLIA["rpc"]),
            chain_id=int(os.getenv("MANTLE_CHAIN_ID", MANTLE_SEPOLIA["chain_id"])),
            registry_address=os.getenv("SMT_REGISTRY_ADDRESS"),
            private_key=os.getenv("MANTLE_PRIVATE_KEY"),
        )


# Minimal ABI — only the functions the bridge calls.
REGISTRY_ABI = [
    {"inputs": [{"name": "cardURI", "type": "string"}], "name": "registerAgent",
     "outputs": [{"name": "agentId", "type": "uint256"}], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"name": "pair", "type": "bytes32"}, {"name": "direction", "type": "int8"},
                {"name": "convictionBps", "type": "uint16"}, {"name": "reasoningHash", "type": "bytes32"}],
     "name": "recordDecision", "outputs": [{"name": "decisionId", "type": "uint256"}],
     "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"name": "decisionId", "type": "uint256"}, {"name": "correct", "type": "bool"}],
     "name": "gradeDecision", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"name": "agentId", "type": "uint256"}], "name": "reputationBps",
     "outputs": [{"name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
]


class MantleBridge:
    """web3.py client; degrades to a no-op (returns None) when web3/RPC/key absent."""

    def __init__(self, config: Optional[OnchainConfig] = None):
        self.config = config or OnchainConfig.from_env()
        self._w3 = None
        self._contract = None

    def _connect(self) -> bool:
        if self._w3 is not None:
            return True
        try:
            from web3 import Web3  # lazy: bare container has no web3
        except ImportError:
            log.warning("[MANTLE] web3 not installed — signal-only (no on-chain write)")
            return False
        if not (self.config.registry_address and self.config.private_key):
            log.warning("[MANTLE] missing registry address or key — signal-only")
            return False
        try:
            self._w3 = Web3(Web3.HTTPProvider(self.config.rpc_url))
            self._contract = self._w3.eth.contract(
                address=Web3.to_checksum_address(self.config.registry_address), abi=REGISTRY_ABI)
            return self._w3.is_connected()
        except Exception as exc:  # noqa: BLE001 — degrade, never block the alert
            log.warning("[MANTLE] connect failed (%s) — signal-only", exc)
            return False

    def available(self) -> bool:
        return self._connect()

    def _send(self, fn) -> Optional[str]:
        """Sign + send a contract call; return tx hash hex, or None on any failure."""
        try:
            from web3 import Web3
            acct = self._w3.eth.account.from_key(self.config.private_key)
            tx = fn.build_transaction({
                "from": acct.address,
                "nonce": self._w3.eth.get_transaction_count(acct.address),
                "chainId": self.config.chain_id,
            })
            signed = acct.sign_transaction(tx)
            tx_hash = self._w3.eth.send_raw_transaction(signed.raw_transaction)
            return Web3.to_hex(tx_hash)
        except Exception as exc:  # noqa: BLE001
            log.warning("[MANTLE] tx failed (%s) — skipped", exc)
            return None

    def record_decision(self, pair: str, direction: str, confidence: float, reasoning: str) -> Optional[str]:
        """Write one Judge decision on-chain. Returns tx hash, or None if unavailable."""
        if not self._connect():
            return None
        from web3 import Web3
        fn = self._contract.functions.recordDecision(
            pair_to_bytes32(pair), direction_to_int(direction),
            conviction_to_bps(confidence), Web3.keccak(text=reasoning or ""))
        tx = self._send(fn)
        if tx:
            log.info("[MANTLE] recordDecision %s %s conf=%.2f → %s", pair, direction, confidence, tx)
        return tx

    def grade_decision(self, decision_id: int, correct: bool) -> Optional[str]:
        if not self._connect():
            return None
        return self._send(self._contract.functions.gradeDecision(int(decision_id), bool(correct)))
