"""Conformal prediction interval over CPCV Sharpe (MAPIE).

Distribution-free; no normality assumption. Output:
expected_daily_pnl_usd ± half-width at the requested confidence level
(90% by default). Surfaces in the dashboard so retail sees an honest
interval, not a point estimate.
"""


def conformal_interval(*args, **kwargs):
    raise NotImplementedError("Session F: MAPIE conformal over CPCV bag.")
