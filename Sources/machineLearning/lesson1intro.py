# Pandas is used for reading data and data manipulation,
# numpy is used for computations of numerical data,
# matplotlib is used for graphing data,
# and scikit-learn is used for machine learning models

# Supervised learning is when we have a known target based on past data (for example, predicting what price a house will sell for) and 
# unsupervised learning is when there isn't a known past answer (for example, determining the topics discussed in restaurant reviews).

# Besides supervised and unsupervised, there are two further types known as Reinforcement and Semisupervised Learning.
# Semisupervised Learning is when you're dealing with a partially labeled data, usually a large amount of unlabeled and a little bit of labeled ones. Google Photos is the best example of this. With only a few of "your" pictures it will recognize "you" in the future images. It can involve a combination of both supervised and unsupervised techniques.
# Reinforcement Learning is quite different, it goes around building the best possible model(experts also call it the best feasible strategy) to reward your system(agent, robot, machine, etc.) whenever it predicts well and penalize it after making wrong actions.

# Within supervised learning, there are classification and regression problems.
# Regression is predicting a numerical value (for example, predicting what price a house will sell for) and
# classification is predicting what class something belongs to (for example, predicting if a borrower will default on their loan).

from math import sqrt
import numpy as np
data = [15, 16, 18, 19, 22, 24, 29, 30, 34]
print("Mean:", np.mean(data))
print("Median:", np.median(data)) # The median can also be thought of as the 50th percentile.
print("50th percentile (median):", np.percentile(data, 50))
print("25th percentile (median):", np.percentile(data, 25))
print("75th percentile (median):", np.percentile(data, 75))
# If there is an even number of datapoints, to find the median (or 50th percentile), you take the mean of the two values in the middle.

# = variance = sum(Distance with means ** 2) / total number
var = sum([int(abs(x - np.mean(data))) ** 2 for x in data]) / len(data)
# standard deviation
std = sqrt(var)
print("Standard deviation:", std)
print("Standard deviation:", np.std(data))
print("Variance:", var)
print("Variance:", np.var(data))