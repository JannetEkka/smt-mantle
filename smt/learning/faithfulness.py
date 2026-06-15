"""Counterfactual persona-flip faithfulness check.

Holding everything else constant, flip ONE persona's vote (e.g. force
WhalePersona to vote LONG instead of NEUTRAL). Does the JUDGE decision
change in the predicted direction with the predicted magnitude? If not,
the JUDGE weighting is mis-attributing — fix before shipping new
weights.

Output feeds the agentic explanation layer (Session H): only ship a
persona attribution to retail if the counterfactual flip confirms the
attribution is real.
"""


def counterfactual_persona_flip(*args, **kwargs):
    raise NotImplementedError("Session F: faithfulness check on JUDGE attribution.")
