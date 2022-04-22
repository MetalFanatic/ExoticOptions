from cmath import tau
from typing import Union
from math import log, sqrt

numeric = Union[int, float]

class BlackSholes:
    """
    s: spot - Underlying stock price 
    k: Strike price
    r: domestic risk free rate (continuously compuounded)  
    vol: Volatility
    #TODO
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

        
