from cmath import tau
from re import S
from src.models import BlackScholes
from src.models.BlackScholesMerton import BlackScholesMerton
from typing import Union
from math import log, sqrt, exp
from src.distribution.standard_normal_dist import normcdf, normpdf
from dataclasses import dataclass

numeric = Union[int, float]

# TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases
@dataclass
class BSM_Greeks(BlackScholes):
    def __init__(
            self, s: numeric = None, k=None, r: numeric = None, q=0, vol: numeric = None, tau: numeric = None, get_d1=None, get_d2: numeric = None, get_call: numeric = None, get_put: numeric = None):
        self.s = s or self.s
        self.k = k or self.k
        self.r = r or self.r
        self.q = q or self.q
        self.vol = vol or self.vol
        self.tau = tau or self.tau
        self.get_d1 = get_d1 or self.get_d1
        self.get_d2 = get_d2 or self.get_d2
        self.get_call = get_call or self.get_call
        self.get_put = get_put or self.get_put
        # instantiated
        # TODO pass in mod parameter so right can be used as a sign for methods to obtain that require knowing whether to return a call or put

    # TODO
    # so the idea for these greeks, or the way I'm envisioning it is we can store
    # them in a dataclass or whatever as a get method and then we create 5 more classes that depend upon
    # BSM_Greeks that simply call the methods with a self function that is one of these five: Common_Greeks, First_Order_Greeks,
    # Second_Order_Greeks, Third_Order_Greeks, All_Greeks

    # the common greeks include delta, gamma, theta, vega, and rho
    # the first order greeks ... sorry ran out of time, the link below shows it

    def get_delta(self): ...


    def get_theta(self): ...


    def get_vega(self): ...


    def get_rho(self): ...


    def get_epsilon(self): ...


    def get_lambda(self): ...


    def get_gamma(self): ...


    def get_vanna(self): 
        q = self.q
        tau = self.tau
        d1 = self.d1
        d2 = self.d2
        # TODO sigma?
        return -exp(-q* tau) * normcdf(d1)*d2/ σ

    def get_charm(self): ...


    def get_vomma(self): ...


    def get_veta(self): ...

    # uses math I don't know how to derive
    def get_vera(self): ...


    def get_phi(self): ...


    def get_speed(self): ...


    def get_zomma(self): ...


    def get_color(self): ...


    def get_ultima(self): ...


    def get_dual_delta(self): ...


    def get_dual_gamma(self): ...


    def call_epsilone(self):
        s = self.s
        tau = self.tau
        r = self.r
        q = self.q
        d1 = self.d1
        return -s * tau * exp(-q * tau) * normcdf(d1)


    def put_epsilone(self):
        s= self.s
        tau = self.tau
        q = self.q
        d1 = self.d1
        
        # S*τ*exp(-q*τ)*Φ(-d1)
        return s * tau * exp(-q * tau) * normcdf(-d1)
    

    def call_delta(self):
        q = self.q
        tau = self.tau
        d1 = self.d1
        # exp(-q*τ)*Φ(d1)
        return exp(-q * tau) * normcdf(d1)
        

    def put_delta(self):
        q = self.q
        tau = self.tau
        d1 = self.d1
        # exp(-q*τ)*Φ(d1
        return exp(-q * tau) * normcdf(d1)
    
    
    def get_action(action:str):
        match action:
            case "put":
                ...
            case "call":
                ...
            case _:
                raise ValueError()

"""
    vol = sigma
    
    https://en.wikipedia.org/wiki/Greeks_(finance)
    
    call𝑉 = callPremium=max(0,S*exp(-q*τ)*Φ(d1)-K*exp(-rf*τ)*Φ(d2));
    put𝑉 = putPremium=max(0,K*exp(-rf*τ)*Φ(-d2)-S*exp(-q*τ)*Φ(-d1));

    callDeltaΔ = exp(-q*τ)*Φ(d1)
    putDeltaΔ = exp(-q*τ)*(Φ(d1)-1)

    callThetaθ = 1/365*(-(S*σ*exp(-q*τ)/(2*√τ)*1/(√(2*π))*exp(-d1^2/2))
        -rf*K*exp(-rf*τ)*Φ(d2)+q*S*exp(-q*τ)*Φ(d1))

    putThetaθ  = 1/365*(-(S*σ*exp(-q*τ)/(2*√τ)*1/(√(2*π))*exp(-d1^2/2))
        +rf*K*exp(-rf*τ)*Φ(-d2)-q*S*exp(-q*τ)*Φ(-d1))

    # scrV
    𝒱 = Vega𝒱 = 1/100*S*exp(-q*τ)*√τ*1/√(2*π)*exp(-d1^2/2)

    callRhoρ = 1/100*K*τ*exp(-rf*τ)*Φ(d2)
    putRhoρ = -1/100*K*τ*exp(-rf*τ)*Φ(-d2)

    .callEpsilonε = -S*τ*exp(-q*τ)*Φ(d1)
    .putEpsilonε = S*τ*exp(-q*τ)*Φ(-d1)

    callLambdaλ = callDeltaΔ*S/callPremium
    putLambdaλ = putDeltaΔ*S/putPremium

    Γ = GammaΓ = exp(-q*τ)/(S*σ*√τ)*1/√(2*π)*exp(-d1^2/2)

    Vanna = -exp(-q*τ)*𝜙(d1)*d2/σ

    callCharm = q*exp(-q*τ)*Φ(d1)-exp(-q*τ)*𝜙(d1)*(2*(rf-q)-d2*σ*√τ)/(2*τ*σ*√τ)
    putCharm = -q*exp(-q*τ)*Φ(-d1)-exp(-q*τ)*𝜙(d1)*(2*(rf-q)-d2*σ*√τ)/(2*τ*σ*√τ)

    Vomma = 𝒱*d1*d2/σ

    Veta = -S*exp(-q*τ)*𝜙(d1)*√τ*(q+(rf-q)*d1/(σ*√τ)-(1+d1*d2)/(2*τ))

    # itphi
    𝜑 = exp(-rf*τ)*1/K*1/√(2*π*σ^2*τ)*exp(-1/(2*σ^2*τ)*(log(K/S)-((rf-q)-1/2*σ^2)*τ)^2)

    Speed = -Γ/S*(d1/(σ*√τ)+1)

    Zomma = Γ*(d1*d2-1)/σ

    Color_ = -exp(-q*τ)*𝜙(d1)/(2*S*τ*σ*√τ)*(2*q*τ+1+(2*(rf-q)*τ-d2*σ*√τ)/(σ*√τ)*d1)

    Ultima = -𝒱/σ^2*(d1*d2*(1-d1*d2)+d1^2+d2^2)

    callDualDeltaΔ = -exp(-rf*τ)*Φ(d2)
    putDualDeltaΔ = exp(-rf*τ)*Φ(-d2)

    DualGammaΓ = exp(-rf*τ)*(𝜙(d2)/(K*σ*√τ))
 
 
 
 
 
"""
