from src.models.BlackScholes import BlackScholes
from typing import Union
from math import log, sqrt, exp
from src.distribution.standard_normal_dist import normcdf

numeric = Union[int, float]


class BlackScholesMerton(BlackScholes):

    def __init__(self, s: numeric, k: numeric, r: numeric, q: numeric, vol: numeric, tau: numeric) -> None:
        self.s = s
        self.k = k
        self.r = r
        self.q = q
        self.vol = vol
        self.tau = tau
        self.d1 = self.get_d1()
        self.d2 = self.get_d2()

    def get_d1(self) -> float:
        """"z-score"""
        s = self.s
        k = self.k
        r = self.r
        vol = self.vol
        tau = self.tau
        q = self.q

        return (log(s / k) + (r - q + vol ** 2 / 2) * tau) / (vol * sqrt(tau))

    def get_call(self) -> float:
        s = self.s
        k = self.k
        q = self.q
        r = self.r
        tau = self.tau
        d1 = self.d1
        d2 = self.d2
        return s * exp(-q * tau) * normcdf(d1) - k * exp(-r * tau) * normcdf(d2)

    def get_put(self) -> float:
        s = self.s
        k = self.k
        r = self.r
        q = self.q
        tau = self.tau
        d1 = self.d1
        d2 = self.d2
        return -s * exp(-q * tau) * normcdf(-d1) + k * exp(-r * tau) * normcdf(-d2)

    def _price(self):
        pass
        # TODO: this function
        # I want to have it a lazy reference to get_put, get_call based on input criteria in mod that we'll build in later. We don't want to call get_call,
        # rather price("c", ...) where "c" would designate that we mean to get_call

    # code checking
    def __repr__(self) -> str:
        return f"s: {self.s}\tk: {self.k}\tq: {self.q}\tr: {self.r}\ttau: {self.tau}\td1: {self.d1}\td2: {self.d2}"
