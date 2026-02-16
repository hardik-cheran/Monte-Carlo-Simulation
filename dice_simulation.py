import numpy as np
import matplotlib.pyplot as plt
n = 100000
die1 = np.random.randint(1,7,size=n)
die2 = np.random.randint(1,7,size=n)
total = die1 + die2
event = (total >= 9)
probability = np.mean(event)
print("Estimated probability of rolling a total of 9 or more with two dice:", probability)
print("Exact Probability:", 5/18)
print("Error:", abs(probability - 5/18))
trials = np.arange(1,n+1)
running_prob = np.cumsum(event)/trials
plt.plot(running_prob)
plt.axhline(5/18, color = 'red', linestyle = '--', label = 'Exact Probability')
plt.xlabel('Number of simulations')
plt.ylabel('Estimated Probability')
plt.title('Monte Carlo Convergence : P(sum) >= 9')
plt.show()