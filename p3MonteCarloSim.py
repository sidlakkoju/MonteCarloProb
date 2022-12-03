import math
import random
import numpy as np

import randomValueGen as rvg


# importing the libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


import random

import scipy.stats as ss






#-------------- RANDOM VALUE GENERATOR TESTING --------------#

# First three Monte Carlo Numbers
print("Random Number 1: " + str(rvg.randNumStart(1)))
print("Random Number 2: " + str(rvg.randNumStart(2)))
print("Random Number 3: " + str(rvg.randNumStart(3)))
print("")

# Random Numbers 51, 52, 53
print("Random Number 51: " + str(rvg.randNumStart(51)))
print("Random Number 52: " + str(rvg.randNumStart(52)))
print("Random Number 53: " + str(rvg.randNumStart(53)))
print("")

#---------------- MONTE CARLO SIMULATION ----------------#



gen = rvg.randNumGenerator()



trial_num = 110

# Rayleigh Random Variable Parameter
a = 1/57

# RV M variables
sample_sizes = [10, 30, 50, 100, 250, 500, 1000]
#sample_sizes = [1, 2, 3]
results = []

part4_x = []
part4_y = []



counter = 1
sample_count = 0

'''
for sample_size in sample_sizes:

    # Add list for current sample
    results.append([])

    trial_count = 0
    for i in range(trial_num):
        
        # Add list for current trial
        results[sample_count].append([])


        for t in range(sample_size):

            #uniform_rand_num = rvg.randNumStart(trial_count)
            #uniform_rand_num = random.random()
            uniform_rand_num = gen.getRandNum()
            counter += 1
            
            x = math.sqrt((-2 * np.log(1 - uniform_rand_num)) / (a**2))
            results[sample_count][trial_count].append(x)

        

        part4_x.append(sample_size)
        part4_y.append(np.average(results[sample_count][trial_count]))

        trial_count += 1
    sample_count += 1


#print(part4_coordinates)
#print(results)
plt.xscale("log")
plt.plot([0, 1000], [71.44, 71.44], color='k', linestyle='-', linewidth=2)
plt.scatter(part4_x, part4_y, s=10)
plt.xlabel("Number of Samples")
plt.ylabel("Mean Estimate (in)")
plt.show()
'''



nk_pairs = [(3,5), (9,25), (27,110), (81,550)]


# 5.2.1

M_vals = []
means = []
for nk in nk_pairs:
    n = nk[0]
    k = nk[1]
    cur_sample = []
    for trial in range(k):
        cur_trial_sum = 0
        for i in range(n):
            uniform_rand_num = gen.getRandNum()
            x = math.sqrt((-2 * np.log(1 - uniform_rand_num)) / (a**2))
            cur_trial_sum += x

        cur_sample.append(cur_trial_sum/n)
    
    means.append(np.average(cur_sample))
    M_vals.append(cur_sample)



SDs = []
for i in range(len(means)):
    sum = 0
    for val in M_vals[i]:
        sum += (val**2) - (means[i]**2)
    SD = sum/len(M_vals[i])
    SDs.append(SD)


print("means")
print(means)

print("SDs")
print(SDs)

print("")

# 5.2.2

Z_vals = []
for i in range(len(M_vals)):
    cur_Z_sample = []
    for val in M_vals[i]:
        Z_val = (val - means[i])/math.sqrt(SDs[i])
        cur_Z_sample.append(Z_val)
    Z_vals.append(cur_Z_sample)




# 5.2.3
j_vals = [-1.4, -1.0, -0.5, 0, 0.5, 1.0, 1.4]
j_probs = []
for i in range(len(Z_vals)):
    j_prob = []
    for j_val in j_vals:
        count = 0
        for z_val in Z_vals[i]:
            if (z_val <= j_val):
                count += 1
        j_prob.append(count/len(Z_vals[i]))
    j_probs.append(j_prob)

print("j_probs")
print(j_probs)
print("")


        


# 5.2.4
actual_probs = [0.08075666, 0.15865525, 0.30853754, 0.5, 0.69146246, 0.84134475, 0.91924334]
MADn_x = []
MADn = []
for i in range(len(j_probs)):
    max_dif = 0
    max_x = 0
    for e in range(len(j_probs[i])):
        difference = abs(j_probs[i][e] - actual_probs[e])
        if difference > max_dif:
            max_x = j_vals[e]
            max_dif = difference
    MADn_x.append(max_x)    
    MADn.append(max_dif)

print(MADn)


# 5.2.5
i = 3   # ranges from 0 to 3


x = np.linspace(-5, 5, 5000)
mu = 0
sigma = 1

y_pdf = ss.norm.pdf(x, mu, sigma) # the normal pdf
y_cdf = ss.norm.cdf(x, mu, sigma) # the normal cdf


plt.plot(x, y_cdf, label='cdf')
plt.xlim([-2.5, 2.5])

plt.scatter(j_vals, j_probs[i], s=10)
plt.scatter(MADn_x[i], MADn[i], s=20, label='MADn')

plt.xlabel("SD")
plt.ylabel("Probability")

'''
plt.legend()
plt.show()
'''
print(j_vals)
print(j_probs[i])




