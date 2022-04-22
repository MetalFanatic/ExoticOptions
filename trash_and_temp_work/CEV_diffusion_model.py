"""

Local Volatility Models:
dS_t/S_t = μ(S_t, t)dt + σ(S_t, t)dW_t

Constant Elasticity of Variance (CEV) diffussion model:
X_t = stock price S_t
Cox and Ross (1976)
dX_t = μX_tdt + σX_t**(θ/2)dW_t

Call_Price_CEV for X_t = x

Call_CEV(t,x) = exp(-r*τ)*x*Integral(



"""