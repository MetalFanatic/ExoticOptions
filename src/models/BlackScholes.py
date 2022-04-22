from typing import Union
from math import log, sqrt, exp
from src.distribution.standard_normal_dist import normcdf


numeric = Union[int, float]

class BlackScholes:
    """
    s: spot - Underlying stock price 
    k: Strike price
    r: domestic risk free rate (continuously compuounded)  
    vol: Volatility
    tau: (T - t) / 252   
    """
    def __init__(self, s:numeric, k:numeric, r: numeric, vol: numeric, tau: numeric) -> None:
        self.s = s
        self.k = k
        self.r = r
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
        return (log(s / k) + (r + vol ** 2 / 2) * tau) / (vol * sqrt(tau))


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
        return s * normcdf(d1) - k * exp(-r * tau) * normcdf(d2)
            


    def get_put(self) -> float:
        s = self.s
        k = self.k
        r = self.r
        tau = self.tau
        d1 = self.d1
        d2 = self.d2 
        return -s * normcdf(-d1) + k * exp(-r * tau) * normcdf(-d2)



