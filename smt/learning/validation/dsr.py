"""Deflated Sharpe Ratio — Bailey & López de Prado, JFDS 2014.

Discounts the observed Sharpe for the number of trials searched +
skew / kurt of returns. Filter: a candidate passes only if DSR > 0
at 95% confidence (one-tailed).
"""


def deflated_sharpe(*args, **kwargs):
    raise NotImplementedError("Session F: DSR per Bailey & López de Prado 2014.")
