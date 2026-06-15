"""smt.learning.validation — CPCV / DSR / PBO / FDR / conformal / KDE.

Every TPE-optimized candidate must pass DSR + PBO + FDR before going
to CPCV (Bagged Combinatorial Purged CV) for held-out evaluation;
the CPCV Sharpe gets wrapped in a conformal prediction interval.
"""
