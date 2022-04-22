from scipy.stats import norm
from math import sqrt, exp, log
from collections import namedtuple

φ = norm.pdf
Φ = norm.cdf


"""
Base class for Options.

Args:
S : underlying asset price (aka spot price)
K : strike price
rf : risk free rate (LIBOR, T-bill, etc)
q : continuously compounded divided yield 
tau(τ) : time to expiry (i.e. τ = (T - t)**(1/252) trading days)
sigma(σ) : underlying asset volatility
Style: See Style named tuple
Model: See Model Named tuple
Process: Analytic, Simulation

Args default values:
S: none, error check that it cannot be negative
K: none, error check that it cannot be negative
rf: float(0) (can be negative)
q: float(0) (technically possible to be negative)
τ: none (option expires at 0.)
σ: none (zero volatility is impossible unless it's a risk free security)
Style: "European"
Model: "BlackScholesMerton"
Process: "Analytic"

Required Inputs:
S, K, τ, σ
"""

Style = namedtuple("Style",[
	"European",
	"American",
	"Asian",
	"Digital",
])
Model = namedtuple("PricingModel", [
	"BlackScholes",
	"BlackScholesMerton",
	"Heston",
	"Digital",
])
Volatility = namedtuple("VolModel", [
	"Historical",
	"GARCH",
	"EWMA",
])

class Option:
	def __new__(cls):
		inst = object.__new__(cls)
		return inst
	def __init__(self, S:float, K:float, rf:float=0., q:float=0., σ:float, τ:float=0., Style:str="European", Model:str="BlackScholesMerton", process:str = "Analytic", **kwargs):
		if (S or K) < 0 or (σ or τ) <= 0.0:
			ValueError("S, K, σ, and τ must be positive")
		elif 
		self.S = S
		self.K = K
		self.rf = rf
		self.q = q
		self.σ = σ
		self.τ = τ
		self.Style = Style
		self.Model = Model
		self.process = process
		if Style ==  "European" and Model == "BlackScholesMerton":
			self.d1 = (log(S/K) + (rf - q + 1/2*σ ** 2)*τ)/(σ*sqrt(τ))
			self.d2 = (log(S/K) + (rf - q - 1/2*σ ** 2)*τ)/(σ*sqrt(τ))
			call = S*exp(-q*τ)*Φ(self.d1)-K*exp(-rf*τ)*Φ(self.d2)
			put = -S*exp(-q*τ)*Φ(-self.d2)+K*exp(-rf*τ)*Φ(-self.d1)





opt_nt = namedtuple('Option', [S, K, rf, q, σ, τ, Style, Model])






	

class Style(Option):
	def __new__(cls):
		inst = object.__new__(cls)
		return inst
	def __init__(self, Style:str):
		self.Style = Style
		if Style in list(
			"European",
			"American",
			"Asian",
			"Binary",
		):
			return Style
		else: Style = "European"
		
class Model(Option):
	def __new__(cls):
		inst = object.__new__(cls)
		return inst
	def __init__(self, Model: str):
		self.Model = Model
		if Model in list(
			"BlackScholes",
			"BlackScholesMerton",
			"Binomial",
			"Trinomial",
			"Heston"
		):
			return Model
		else: Model = "BlackScholesMerton"

	super().Option(Option.S, Option.K, Option.rf, Option.q, Option.σ, Option.τ)
	def BlackScholesMerton(cls, Style, Model):
		cls.Style = Style
		cls.Model = Model
		if Style == "European" and Model == "BlackScholesMerton":
			d1 = (log(S/K) + (rf - q + 1/2*σ^2)*τ)/(σ*sqrt(τ))
			d2 = (log(S/K) + (rf - q - 1/2*σ^2)*τ)/(σ*sqrt(τ))
			call = S*exp(-q*τ)*norm.cdf(d1) - K*exp(-rf*τ)*norm.cdf(d2)
			put = -S*exp(-q*τ)*norm.cdf(-d2) + K*exp(-rf*τ)*norm.cdf(-d1)
			return (S, K, rf, q, σ, τ, d1, d2, call, put)

args = Αrgs(S, K, rf, q, σ, τ)
class BlackScholesMertonModel(Model):
	def _init_(args):
		d1 = (log(S/K) + (rf - q + 1/2*σ^2)*τ)/(σ*sqrt(τ))
		d2 = (log(S/K) + (rf - q - 1/2*σ^2)*τ)/(σ*sqrt(τ))
		return (d1, d2)
args_bsm = (args, BlackScholesMertonModel(args))
	
class Vanilla_European:
	def _self_(args_bsm):

		return (args_bsm,call,put)			
            
			
			
#super().Option(S, K, rf, q, σ, τ)
