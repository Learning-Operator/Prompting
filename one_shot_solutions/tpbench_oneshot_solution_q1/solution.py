# filename: codebase/b_eff.py
def b_eff(sigma: float, b_in: float) -> float:
    """
    Calculate the effective bias of the sampled halo field.

    Parameters:
    sigma (float): The standard deviation of the Gaussian matter density field (unitless).
    b_in (float): The bare bias of the halo field (unitless).

    Returns:
    float: The effective bias of the sampled halo field (unitless).
    """
    return b_in * (1 + sigma**2)
