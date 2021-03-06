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
    
    call???? = callPremium=max(0,S*exp(-q*??)*??(d1)-K*exp(-rf*??)*??(d2));
    put???? = putPremium=max(0,K*exp(-rf*??)*??(-d2)-S*exp(-q*??)*??(-d1));

    .callDelta?? = exp(-q*??)*??(d1)
    .putDelta?? = -exp(-q*??)*??(-d1)

    callTheta?? = 1/365*(-(S*??*exp(-q*??)/(2*?????)*1/(???(2*??))*exp(-d1^2/2))
        -rf*K*exp(-rf*??)*??(d2)+q*S*exp(-q*??)*??(d1))

    putTheta??  = 1/365*(-(S*??*exp(-q*??)/(2*?????)*1/(???(2*??))*exp(-d1^2/2))
        +rf*K*exp(-rf*??)*??(-d2)-q*S*exp(-q*??)*??(-d1))

    # scrV
    ???? = Vega???? = 1/100*S*exp(-q*??)*?????*1/???(2*??)*exp(-d1^2/2)

    callRho?? = 1/100*K*??*exp(-rf*??)*??(d2)
    putRho?? = -1/100*K*??*exp(-rf*??)*??(-d2)

    .callEpsilon?? = -S*??*exp(-q*??)*??(d1)
    .putEpsilon?? = S*??*exp(-q*??)*??(-d1)

    callLambda?? = callDelta??*S/callPremium
    putLambda?? = putDelta??*S/putPremium

    ?? = Gamma?? = exp(-q*??)/(S*??*?????)*1/???(2*??)*exp(-d1^2/2)

    Vanna = -exp(-q*??)*????(d1)*d2/??

    callCharm = q*exp(-q*??)*??(d1)-exp(-q*??)*????(d1)*(2*(rf-q)-d2*??*?????)/(2*??*??*?????)
    putCharm = -q*exp(-q*??)*??(-d1)-exp(-q*??)*????(d1)*(2*(rf-q)-d2*??*?????)/(2*??*??*?????)

    Vomma = ????*d1*d2/??

    Veta = -S*exp(-q*??)*????(d1)*?????*(q+(rf-q)*d1/(??*?????)-(1+d1*d2)/(2*??))

    # itphi
    ???? = exp(-rf*??)*1/K*1/???(2*??*??^2*??)*exp(-1/(2*??^2*??)*(log(K/S)-((rf-q)-1/2*??^2)*??)^2)

    Speed = -??/S*(d1/(??*?????)+1)

    Zomma = ??*(d1*d2-1)/??

    Color_ = -exp(-q*??)*????(d1)/(2*S*??*??*?????)*(2*q*??+1+(2*(rf-q)*??-d2*??*?????)/(??*?????)*d1)

    Ultima = -????/??^2*(d1*d2*(1-d1*d2)+d1^2+d2^2)

    callDualDelta?? = -exp(-rf*??)*??(d2)
    putDualDelta?? = exp(-rf*??)*??(-d2)

    DualGamma?? = exp(-rf*??)*(????(d2)/(K*??*?????))
"""
