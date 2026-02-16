import numpy as np
import matplotlib.pyplot as plt

S0 = 100
K = 105
r = 0.05
sigma = 0.2
T = 1.0

n = 20000

Z = np.random.normal(size = n)

ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) *Z)
payoff = np.maximum(ST-K,0)
price = np.exp(-r*T)*np.mean(payoff)
print("European Call Option Price:", price)
std_error = np.std(payoff)/np.sqrt(n)
print("Standard Error:", std_error)
for sigma in [0.1,0.2,0.3,0.4]:
    Z = np.random.normal(size=n)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(ST - K, 0)
    price = np.exp(-r * T) * np.mean(payoff)

    print("Volatility:", sigma, "Option Price:", price)