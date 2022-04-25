from src.models.BlackScholes import BlackScholes
from typing import Union
from math import log, sqrt, exp
from src.distribution.standard_normal_dist import normcdf, normpdf
from src.enumerations.QueryGreekAction import QueryGreekAction
from src.models.errors.ContinuousModelException import InvalidAction


numeric = Union[int, float]


class BSM_Greeks(BlackScholes):

    # instantiated TODO pass in mod parameter so right can be used as a sign for methods to obtain that require
    #  knowing whether to return a call or put

    # TODO so the idea for these greeks, or the way I'm envisioning it is we can store them in a dataclass or
    #  whatever as a get method and then we create 5 more classes that depend upon BSM_Greeks that simply call the
    #  methods with a self function that is one of these five: Common_Greeks, First_Order_Greeks,
    #  Second_Order_Greeks, Third_Order_Greeks, All_Greeks

    # the common greeks include delta, gamma, theta, vega, and rho
    # the first order greeks ... sorry ran out of time, the link below shows it

    def get_delta(self, action: int) -> float:
        """Get delta put/call based on action [0, 1]"""

        action = self.validate_action(action)

        match action:
            case "Put":
                return -exp(self.q * -1 * self.tau) * normcdf(self.d1 * -1)
            case "Call":
                return exp(-self.q * self.tau)*normcdf(self.d1)
            case _:
                raise ValueError("Unexpected action")

    def get_theta(self): ...

    def get_vega(self): ...

    def get_rho(self): ...

    def get_epsilon(self): ...

    def get_lambda(self): ...

    def get_gamma(self): ...

    def get_vanna(self):
        q = self.q
        vol = self.vol
        tau = self.tau
        d1 = self.d1
        d2 = self.d2
        return -exp(-q * tau) * normcdf(d1) * d2 / vol

    def get_charm(self): ...

    def get_vomma(self): ...

    def get_veta(self):
        S = self.S
        q = self.q
        vol = self.vol
        tau = self.tau
        d1 = self.d1
        d2 = self.d2
        S * exp(-q * tau) * normpdf(d1) * sqrt(tau) * (d1 * d2) / vol

    # uses math I don't know how to derive
    def get_vera(self): ...

    def get_phi(self): ...

    def get_speed(self): ...

    def get_zomma(self): ...

    def get_color(self): ...

    def get_ultima(self): ...

    def get_dual_delta(self): ...

    def get_dual_gamma(self): ...

    @staticmethod
    def validate_action(action: int) -> Union[Exception, str]:
        """Check if action is valid and return str repr of action"""
        if not (isinstance(action, int) and 0 <= action <= 1):
            raise InvalidAction(action, "action parameter should be either 1 or 0")
        return QueryGreekAction(action).name


model = BSM_Greeks(100, 34, 23, 12, 432)
print(model.get_delta(1))

"""
    vol = sigma
    
    https://en.wikipedia.org/wiki/Greeks_(finance)
    
    call𝑉 = callPremium=max(0,S*exp(-q*τ)*Φ(d1)-K*exp(-rf*τ)*Φ(d2));
    put𝑉 = putPremium=max(0,K*exp(-rf*τ)*Φ(-d2)-S*exp(-q*τ)*Φ(-d1));

    .callDeltaΔ = exp(-q*τ)*Φ(d1)
    .putDeltaΔ = -exp(-q*τ)*Φ(-d1)

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
