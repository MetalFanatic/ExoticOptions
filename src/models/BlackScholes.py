from typing import Union, Optional
from math import log, sqrt, exp
from src.distribution.standard_normal_dist import normcdf
from dataclasses import dataclass
from errors.BlackcsholesException import BlackSholesException

numeric = Union[int, float]


@dataclass(frozen=True)
class BlackScholes:
    """
    s: spot - Underlying stock price 
    k: Strike price
    r: domestic risk free rate (continuously compuounded)  
    vol: Volatility
    tau: (T - t) / 252   
    """

    s: numeric
    k: numeric
    r: numeric
    vol: numeric
    tau: numeric

    q: Optional[numeric] = 0
    merton: Optional[bool] = False

    def __post_init__(self):
        if self.merton and not self.q:
            raise BlackSholesException(self.q, message="q should be > 0 if merton=True")

        object.__setattr__(self, "d1", self.get_d1())
        object.__setattr__(self, "d2", self.get_d2())

    def get_d1(self) -> float:
        """"z-score"""
        s = self.s
        k = self.k
        r = self.r
        vol = self.vol
        tau = self.tau

        return (log(s / k) + (r - 0 + vol ** 2 / 2) * tau) / (vol * sqrt(tau))

    def get_d2(self) -> float:
        """z-score"""
        d1 = self.get_d1()
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


model = BlackScholes(100, 105, 0.012, 0.21, 0.45, merton=True, q=3)
print(model)
