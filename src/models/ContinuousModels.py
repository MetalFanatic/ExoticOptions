from dataclasses import dataclass
from typing import Union, Optional
from abc import ABC
from math import log, sqrt, exp
from src.distribution.standard_normal_dist import normcdf


@dataclass
class ContinuousModel(ABC):
    """
    Abstract representation of a continuous model, this class is not meant to be instantiated

    :Attrs:
        s: spot - Underlying stock price
        k: Strike price
        r: domestic risk-free rate (continuously compounded)
        vol: Volatility
        tau: (T - t) / 252
    """
    s: Union[int, float]
    k: Union[int, float]
    r: Union[int, float]
    vol: Union[int, float]
    tau: Union[int, float]
    q: Union[int, float] = 0

    @property
    def d1(self) -> float:
        """"z-score"""
        s = self.s
        k = self.k
        r = self.r
        vol = self.vol
        tau = self.tau

        return (log(s / k) + (r - 0 + vol ** 2 / 2) * tau) / (vol * sqrt(tau))

    @property
    def d2(self) -> float:
        """z-score"""
        d1 = self.d1
        tau = self.tau
        vol = self.vol
        return d1 - vol * sqrt(tau)

    def get_call(self) -> float:
        s = self.s
        k = self.k
        r = self.r
        tau = self.tau
        d1 = self.d1
        d2 = self.d2
        q = self.q

        return s * exp(-q * tau) * normcdf(d1) - k * exp(-r * tau) * normcdf(d2)

    def get_put(self) -> float:
        s = self.s
        k = self.k
        r = self.r
        tau = self.tau
        d1 = self.d1
        d2 = self.d2
        q = self.q
        return -s * exp(-q * tau) * normcdf(-d1) + k * exp(-r * tau) * normcdf(-d2)
