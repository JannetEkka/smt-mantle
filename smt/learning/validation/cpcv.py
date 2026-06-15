"""Bagged Combinatorial Purged Cross-Validation — López de Prado, AFML ch. 7.

Standard k-fold leaks future info via label overlap; CPCV purges train
windows around the test fold + embargoes adjacent bars. Bagged across
N=20+ paths to produce a Sharpe distribution (not a point estimate).

Output consumed by smt.learning.validation.conformal to produce a
calibrated prediction interval.
"""


def bagged_cpcv_sharpe(*args, **kwargs):
    raise NotImplementedError("Session F: bagged CPCV over per-pair returns.")
