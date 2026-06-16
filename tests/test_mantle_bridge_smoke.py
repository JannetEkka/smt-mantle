"""Smoke tests for the Mantle Turing Test bridge (hackathons/mantle-turing-test/).

The hackathon folder is hyphenated (not an importable package), so we load
``onchain.py`` + ``alert_bot.py`` by file path. Everything here is pure-Python +
offline: the on-chain bridge must DEGRADE (no web3/RPC/key → available() False),
and the alert must always be ≤500 chars (the contract's reasoningHash text).
"""

from __future__ import annotations
import importlib.util
import os
import sys

import pytest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRIDGE = os.path.join(REPO, "hackathons", "mantle-turing-test")


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(BRIDGE, filename))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod          # dataclasses need the module registered before exec
    spec.loader.exec_module(mod)
    return mod


onchain = _load("smt_mantle_onchain", "onchain.py")
alert_bot = _load("smt_mantle_alert_bot", "alert_bot.py")

from smt.personas.base import PersonaVote  # noqa: E402


# ── pure encoders match the Solidity types ────────────────────────────────────

def test_pair_to_bytes32_is_32_bytes_and_padded():
    b = onchain.pair_to_bytes32("BTCUSDT")
    assert len(b) == 32 and b.startswith(b"BTCUSDT") and b.endswith(b"\x00")


def test_direction_and_conviction_encoders():
    assert onchain.direction_to_int("LONG") == 1
    assert onchain.direction_to_int("SHORT") == -1
    assert onchain.direction_to_int("WAIT") == 0
    assert onchain.conviction_to_bps(0.55) == 5500
    assert onchain.conviction_to_bps(1.7) == 10000      # clamp high
    assert onchain.conviction_to_bps(-1.0) == 0         # clamp low


def test_agent_card_has_required_fields():
    card = onchain.build_agent_card(registry_address="0xABC", agent_id=1)
    assert card["name"] and card["skills"] and card["transparency"]
    assert card["registry"]["contract"] == "0xABC" and card["registry"]["agentId"] == 1
    assert card["endpoints"]["repo"].endswith("smart-money-trading")


# ── on-chain bridge degrades gracefully (no web3 / no config) ──────────────────

def test_bridge_unavailable_without_web3_or_config():
    b = onchain.MantleBridge(onchain.OnchainConfig(registry_address=None, private_key=None))
    assert b.available() is False
    assert b.record_decision("BTCUSDT", "LONG", 0.8, "why") is None   # never raises, returns None


# ── alert formatter is always ≤500 chars and names the drivers ─────────────────

def test_format_alert_within_500_chars_and_names_drivers():
    votes = {
        "flow": PersonaVote("LONG", 0.82, "tape bid"),
        "technical": PersonaVote("LONG", 0.7, "range high"),
        "sentiment": PersonaVote("SHORT", 0.4, "nervous"),
    }
    from smt.personas.judge import JudgePersona
    decision = JudgePersona().decide("BTCUSDT", votes, {"fear_greed": 55, "regime": {"BTC": "TRENDING_UP"}})
    alert = alert_bot.format_alert("BTCUSDT", decision, votes)
    assert len(alert) <= 500
    assert "BTCUSDT" in alert and "SMT" in alert
    assert "Flow" in alert            # top driver named (real name, capitalized)


def test_format_alert_truncates_overlong_reasoning():
    class _D:
        action = "LONG"; confidence = 0.9; reasoning = "x" * 1000
    alert = alert_bot.format_alert("ETHUSDT", _D(), {})
    assert len(alert) <= 500 and alert.endswith("…")


# ── decide_and_alert runs fully offline (no webhook, no bridge) ────────────────

def test_decide_and_alert_offline_no_network():
    votes = {"flow": PersonaVote("LONG", 0.85), "technical": PersonaVote("LONG", 0.8)}
    out = alert_bot.decide_and_alert(
        "BTCUSDT", votes, {"fear_greed": 55, "regime": {"BTC": "TRENDING_UP"}})
    assert out["action"] in ("LONG", "SHORT", "WAIT", "BLOCK")
    assert isinstance(out["alert"], str) and len(out["alert"]) <= 500
    assert out["posted"] is False and out["tx"] is None      # no webhook, no bridge
