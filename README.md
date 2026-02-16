# Monte Carlo Quant Simulations (Python, NumPy)

This project implements Monte Carlo simulation techniques used in quantitative trading and probabilistic modeling.

It includes:
- Probability estimation via stochastic simulation  
- Convergence verification against analytical results  
- European call option pricing under Geometric Brownian Motion  
- Volatility sensitivity analysis and uncertainty estimation  

---

## Project Structure

Monte Carlo Simulation
│── dice_probability.py
│── option_pricing.py
│── README.md


---

## 1. Dice Probability Simulation

Estimates:

P(sum of 2 dies >=9)

using Monte Carlo sampling, and compares against the exact analytical probability.

### Example Output

- Estimated Probability ≈ 0.277  
- Exact Probability = 5/18  
- Error decreases as simulations increase

---

## 2. Monte Carlo Option Pricing

Implements a Monte Carlo pricer for a European call option:

### Features
- Vectorized simulation using NumPy  
- Discounted expected payoff computation  
- Standard error estimation  
- Volatility sensitivity study  

---

## Sample Result: Volatility vs Option Price

| Volatility (σ) | Call Option Price |
|--------------|------------------|
| 0.1          | ~4.1             |
| 0.2          | ~8.2             |
| 0.3          | ~12.0            |
| 0.4          | ~15.9            |

Higher volatility increases option value, consistent with derivatives pricing theory.

---

## Tech Stack

- Python  
- NumPy  
- Matplotlib (optional for convergence plots)

---

## Motivation

This project was built to strengthen foundations in:
- stochastic simulation  
- probability theory  
- quantitative finance modeling  
- algorithmic implementation skills relevant to HFT and trading roles  

---

## Author

Hardik Cheran  
B.Tech Electrical Engineering, IIT Madras
