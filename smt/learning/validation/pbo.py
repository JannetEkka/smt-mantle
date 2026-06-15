"""Probability of Backtest Overfitting — Bailey/Borwein/López de Prado/Zhu, JCF 2017.

Probability that an IS-winning configuration is a median OOS performer.
Filter: candidate passes only if PBO < 0.20.

Also used in production as a live-PBO stopping rule (rolling 30d window;
halt new entries when live PBO > 0.30).
"""


def probability_of_backtest_overfitting(*args, **kwargs):
    raise NotImplementedError("Session F: combinatorial PBO per BBLZ 2017.")
