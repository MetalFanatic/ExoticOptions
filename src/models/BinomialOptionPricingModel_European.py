from typing import Union, Optional
from math import log, sqrt, exp
from src.distribution.standard_normal_dist import normcdf
from dataclasses import dataclass
from numpy import append, array as np


numeric = Union[int, float]

class BinomialOptionPricingModel():

    def __init__(self, s: numeric, k: numeric, r: numeric, q: numeric, vol: numeric, tau: numeric, nsteps: int, right: numeric, opt_type) -> None:
        self.s = s
        self.k = k
        self.r = r
        self.q = q
        self.vol = vol
        self.tau = tau
        self.nsteps  = nsteps
        self.right = right
        self.opt_type = opt_type

    def BinomialOptionPricingModel(self) -> float:
        s = self.s
        k = self.k
        r = self.r
        q = self.q
        vol = self.vol
        tau = self.tau
        nsteps = self.nsteps
        right = self.right
        opt_type = self.opt_type

        if opt_type == "European":
            dt = tau / nsteps
            up = exp(vol*sqrt(tau))
            down = up**(-1)
            yld = exp((r-q)*dt)
            p = (yld - down)/(up - down)
            q2 = (up - yld)/(up - down)
            tp = np.array([])
            for i in range(0,nsteps):
                tp = np.append(tp, right*(s-k),0) * exp((2*i-nsteps)*vol*sqrt(dt))
            tp = max(tp)
            for i in range(0,range(nsteps,0,-1)):
                a = right*(s-k) * exp((2*i-nsteps)*vol*sqrt(dt))
                b = (q2 * tp[i+1] + p * tp[i+2]) / yld
                tp[i+1] = max(a,b)
            return tp[1]
        elif opt_type == "American": ...



