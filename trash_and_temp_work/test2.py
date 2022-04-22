from collections import namedtuple
from math import exp, log, sqrt
from scipy.stats import norm
from dataclasses import dataclass
from typing import NamedTuple
from itertools import dropwhile
from difflib import get_close_matches
import numpy as np
import fuzzywuzzy as fw
from enum import Enum
#alias for norm.pdf and norm.cdf functions


"""
	Fuzzy Matching is a process I learned at while working as a data
	analyst intern at an accounting firm. The process uses the Levenshtein distance between matching characters within two strings. The formula is


				 {max(i,j)				            if min(i,j)==0
	lev_a,b(i,j)={{   {lev_a,b(i-1,j)+1
				 {{min{lev_a,b(i,j-1)+1               otherwise
				 {{   {lev_a,b(i-1,j-1)+1_(a_1<>b_1)

	https://www.datacamp.com/community/tutorials/fuzzy-string-python
"""





def match_arg(s:str, tup, default):
	#Case0: validation
	exception_checks_validation_match_arg(s:str,tup,default)

	#FuzzyWuzzy Process Extract One ... fwpeo
	#uses Levenshtein distance to extract the closest match
	fwpeo = fw.process.extractOne(s, tup)
	#quick check to see if a perfect match exists before proceeding
	if fwpeo[2] == 100:
		return s





def exception_checks_match_arg(s:str, tup, default):
	#checks for non-ASCII string
	if s.isascii() == False or len(s) == 0 or len(s) > 50:
		return Exception("ArgumentError", "Invalid Argument, must be ASCII")










	itr = [[ch for ch in s if ch.isupper()] for s in tup]  # UPPER CHARs
	v = []  # Python converts appended Reals to floats on empty vectors*
	for x in range(0, len(itr)):  # size of vector
		itr[x] = ''.join(itr[x])  # Vector{join(Vector{Char})}

		"""
		appends bool value to vector, Python autoconverts to float... so annoying... anyone know how to set it to Vector{Bool} before hand so it doesn't change typing?*
		"""

		v = np.append(v, (s == itr[x]))
		v = np.array(v, dtype="bool")*1  # changes typing to bitvector
	# numpy.extract function requires bitvector to filter for true values in a second vector
	v = np.extract(v, tup) #
	if (len(v) > 1):  # checks to make sure vector isn't empty
		return (tup, "Exit")



def acroynm_input_match_arg(s, tup, thresh=100, fwpeo = fwpeo):#exact CASE match
	if s.isupper() and fwpeo[2] >= thresh:
		foo = [[ch for ch in s if ch.isupper()] for s in tup]
		bar = fw.process.extract(s, tup)
		highest = []
		for i in bar:
			highest = np.append(highest, (i, bar[i, 2]))
		highest = filter(lambda h: max(h[:, 1]), highest)
		return highest[1]
	if len(s) < 10 and s.islower():  # incase user enters acronym as lowercase
		s2 = s.upper()
		s2 = case_levDis_match(s2, tup)



def match_arg(s: str, tup, default):
	#checks for non-ASCII string
	if s.isascii() == False or len(s) == 0 or len(s) > 50:
		return Exception("ArgumentError", "Invalid Argument, must be ASCII")
	#uses Levenshtein distance to extract the closest match
	fwpeo = fw.process.extractOne(s, tup)
	#Case 0: measures for perfect match between s and tup
	#s returned because list item is already equivalent to s
	if fwpeo[2] == 100:
		return s
	#defined a function to reuse inside of the parent function

	if s != case_levDis_match(s, tup):  # upper case acronym 100% match
		return case_levDis_match(s, tup)
	if len(s) < 10 and s.islower():  # incase user enters acronym as lowercase
		s2 = s.upper()
		s2 = case_levDis_match(s2, tup)
	if s.strip != s:  # testing for spaces
		s2 = s.title()  # user string First Letters Capitalized Others Lower
		s2 = s.strip()  # user
		if fw.process.extractOne(s2, tup)[2] == 100:
			return fw.process.extractOne(s2, tup)[1]
	lenS = len(s)  # final test is looking for just the first several letters
	for (i, v) in enumerate(tup):
		if s.lower() == v.word[:lenS].lower():  # chops the tup string
			return tup[i]
	print("No matches were found, the default is used: %(default)")
	if default in tup:
		return default
	else: return Exception("No default value and no matches")
#end of function

class OptionModifiers():
	PRICE_MODEL: tuple = (
		"BlackScholes", 
		"BlackScholesMerton", 
		"Binomial", 
		"Trinomial", 
		"Heston",
		)
	OPT_TYPE: tuple = (
		"European", 
		"American", 
		"Asian",
		"Bermudan",
		)
	OPT_STYLE: tuple = (
		"Vanilla",
		"Asian",
		"Barrier",
		"Digital",
		"Lookback"
		)
	VOL_MODEL: tuple = (
		"Historic",
		"EWMA",
		"GARCH",
		"T-GARCH"
		)
	DIST_MODEL: tuple = (
		"Standard Normal",
		"Student t",
		"Laplace",
		"Johnson SU",
		"Uniform",
	)
	#defaults 
	price_model:str = "BlackScholesMerton"
	opt_type:str = "European"
	opt_style:str = "Vanilla"
	vol_model:str = "Historic"
	dist_model:str = "Standard Normal"

	#instantiated OptionModifiers
		#default values for OptionModifiers is None unless entry given
	def __init__(self, price_model = None, opt_type = None, opt_style = None, vol_model = None, dist_model = None):
		#or is a short-circuit logic gate. Thus None, or entry... where None is meaning if no entry, then use default
		self.price_model = price_model or self.price_model
		self.opt_type = opt_type or self.opt_type
		self.opt_style = opt_style or self.opt_style
		self.vol_model = vol_model or self.vol_model 
		self.dist_model = dist_model or self.dist_model


#alias for OptionModifier calls
PRICE_MODEL = OptionModifiers.PRICE_MODEL
OPT_TYPE = OptionModifiers.OPT_TYPE
OPT_STYLE = OptionModifiers.OPT_STYLE
VOL_MODEL = OptionModifiers.VOL_MODEL
DIST_MODEL = OptionModifiers.DIST_MODEL

class OptionRight(Enum):
	CALL = 1
	PUT = -1
	NULL = 0

#alias for OptionRight(Enum) calls
CALL = OptionRight.CALL
PUT = OptionRight.PUT
NULL = OptionRight.NULL


@dataclass
class Option():
	right: OptionRight = CALL #CALL, PUT, NULL
	#I opted to include a default value for rf and q, but if one attribute has a default value, then all require a default value
	S: float = 0.0 #spot price of the underlying - required entry
	K: float = 0.0 #strike required entry
	rf: float = 0.0 #domestic continuously compounded risk-free rate - optional
	q: float = 0.0 #dividend yield - optional entry
	σ: float = 0.0 #volatility - required entry, unless using VOL_MODEL
	τ: float = 0.0 #tau = time remaining to maturity - required entry
	mod: OptionModifiers = OptionModifiers() #OptionModifiers instantiated into mod attribute

	#methods placed here to standardize code
	def _discount_factor(self):
		raise NotImplementedError  # Base class Option() lacks method

	# methods generally desired for return
	def _price_calculation(self): #underscore means don't call the method
		raise NotImplementedError #Base class Option() lacks method

	#Greeks
	def _delta(self):  # underscore means don't call the method
		raise NotImplementedError  # Base class Option() lacks method

	def _vega(self):  # underscore means don't call the method
		raise NotImplementedError  # Base class Option() lacks method



@dataclass
class BlackScholesMerton(Option):
	@property
	def spot_discount_factor(self):
		q = self.q
		τ = self.τ
		return exp(-q*τ)

	@property
	def strike_discount_factor(self):
		rf = self.rf
		τ = self.τ
		return exp(-rf*τ)

	@property
	def d1(self): #z-score
		S = self.S
		K = self.K
		rf = self.rf
		q = self.q
		σ = self.σ
		τ = self.τ
		return (log(S/K)+(rf - q + (σ**2) / 2) * τ)

	@property
	def d2(self): #z-score
		d1 = self.d1
		σ = self.σ
		τ = self.τ
		return d1 - σ * sqrt(τ)

	def _price_calculation(self):
		# adj toggles the equation between put and call
		right = self.opt.value
		d1 = self.d1
		d2 = self.d2
		S = self.S
		K = self.K
		df_S = self.spot_discount_factor
		df_K = self.strike_discount_factor

		adj_S = S * df_S * norm.cdf(right*d1) #right determines the sign
		adj_K = K * df_K * norm.cdf(right*d2)

		return (adj_S - adj_K) * right

		#formulas as is if it's easier for you to read this way
		#self.d1 = (log(S/K) + (rf - q + 1/2*σ ** 2)*τ)/(σ*sqrt(τ))
		#self.d2 = (log(S/K) + (rf - q - 1/2*σ ** 2)*τ)/(σ*sqrt(τ))
		#call = S*exp(-q*τ)*Φ(self.d1)-K*exp(-rf*τ)*Φ(self.d2)
		#put = -S*exp(-q*τ)*Φ(-self.d2)+K*exp(-rf*τ)*Φ(-self.d1)



φ = norm.pdf  # phi
Φ = norm.cdf  # Phi











#proof of concept from tutoring session

Option(..., mod=OptionModifiers(os="Student t",,,))

kwargs = {"os": "Student"}
Option(mod=OptionModifiers(**kwargs))




opt = Option(mod="BlackScholes")
opt.price


opt1 = Option(S=100.0, K=100.0, rf=0.01, σ=0.2, τ=0.5)
opt1.mod.pm = 500
opt1.mod.pm = OptionModifiers.pm
opt1.mod.pm
