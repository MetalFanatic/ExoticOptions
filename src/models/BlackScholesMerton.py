from unicodedata import numeric
from  BlackScholes import BlackSholes
from typing import Union
from math import log, sqrt

numeric = Union[int, float]

class BlackScholesMerton(BlackSholes):

    def __init__(self, s: numeric, k: numeric, r: numeric, q:numeric, vol: numeric, tau: numeric) -> None:
        super().__init__(s, k, r, vol, tau)
        self.q = q
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

        return (log(s / k) + (r - q +  vol ** 2 / 2) * tau) / (vol * sqrt(tau))
    

