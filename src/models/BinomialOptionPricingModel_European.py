from typing import Union, Optional
from math import log, sqrt, exp
import numpy as np
from src.models.ContinuousModels import ContinuousModel

numeric = Union[int, float]


class BinomialOptionPricingModel(ContinuousModel):

    nsteps: numeric
    right: numeric
    opt_type: numeric

    def binomial_option_pricing_model(self) -> float:
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
            up = exp(vol * sqrt(tau))
            down = up ** (-1)
            yld = exp((r - q) * dt)
            p = (yld - down) / (up - down)
            q2 = (up - yld) / (up - down)
            tp = np.array([])
            for i in range(nsteps):
                tp = np.append(tp, right * (s - k), 0) * exp((2 * i - nsteps) * vol * sqrt(dt))
            tp = max(tp)
            for i in range(range(nsteps,0,-1)):
                a = right * (s - k) * exp((2 * i - nsteps)*vol * sqrt(dt))
                b = (q2 * tp[i + 1] + p * tp[i + 2]) / yld
                tp[i + 1] = max(a, b)
            return tp[1]
        elif opt_type == "American":
            ...



