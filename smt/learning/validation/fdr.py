"""False Discovery Rate (Benjamini-Hochberg, JRSSB 1995).

Across 8 pairs × multiple param sets we have multiple-comparisons
inflation. FDR caps the expected false-discovery proportion at 0.10.
"""


def bh_fdr(*args, **kwargs):
    raise NotImplementedError("Session F: BH-FDR over per-pair p-values.")
