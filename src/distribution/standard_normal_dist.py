from math import sqrt, pi, exp, erf
from typing import Union

numeric = Union[int, float]


def normpdf(x: numeric, sig=1.0, mu=0) -> float:
    """phi"""
    return 1/ (sig * sqrt(2 * pi)) * exp(-0.5((x-mu)/sig) ** 2)


def normcdf(x: numeric, sig=1.0, mu=0) -> float:
    """Phi"""
    return 1/2*(1+erf((x- mu)/(sig * sqrt(2))))
