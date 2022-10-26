import math
import random
import numpy as np

import randomValueGen as rvg


#-------------- RANDOM VALUE GENERATOR TESTING --------------#

# First three Monte Carlo Numbers
print("Random Number 1: " + str(rvg.randNumStart(1)))
print("Random Number 2: " + str(rvg.randNumStart(1)))
print("Random Number 3: " + str(rvg.randNumStart(1)))
print("")

# Random Numbers 51, 52, 53
print("Random Number 51: " + str(rvg.randNumStart(51)))
print("Random Number 52: " + str(rvg.randNumStart(52)))
print("Random Number 53: " + str(rvg.randNumStart(53)))
print("")




#---------------- MONTE CARLO SIMULATION ----------------#

TRIAL_COUNT = 1000


# Store call duration for each trial
wValues = []

# Run simulation for 1000 trials
for i in range(TRIAL_COUNT):
    time = 0
    call_count = 0

    # Run simulation
    while (call_count < 4):

        # Time for dialing your phone number
        time += 6
        prob = random.random()

        # Busy Line 
        if prob < 0.2:
            time += 3
        
        # Unavailable Customer
        elif prob < 0.5:
            time += 25
        
        # Customer picks up
        else:
            x = float(np.random.exponential(12, 1))
            if x >= 25:
                time += 25
            
            # They Pick up call so end simulation
            else:
                time += x
                break
        
        call_count += 1
        time += 1   # Time to End Call
    wValues.append(time)

mean = np.mean(wValues)

firstQuartile = np.quantile(wValues, 0.25)
median = np.median(wValues)
secondQuartile = np.quantile(wValues, 0.50)
thirdQuartile = np.quantile(wValues, 0.75)

print("MONTE CARLO SIMULATION RESULTS")
print("Mean: " + str(mean))
print("firstQuartile: " + str(firstQuartile))
print("Median: " + str(median))
print("thirdQuartile: " + str(thirdQuartile))
print("")



count_15 = 0
count_20 = 0
count_30 = 0

count_40 = 0

count_50 = 0
count_60 = 0
count_65 = 0

for w in wValues:
    if w <= 15:
        count_15 += 1
    if w <= 20:
        count_20 += 1
    if w <= 30:
        count_30 += 1
    if w > 40:
        count_40 += 1
    if w > 50:
        count_50 += 1
    if w > 60:
        count_60 += 1
    if w > 65:
        count_65 += 1


print("Prob W <= 15: " + str(count_15 / TRIAL_COUNT))
print("Prob W <= 20: " + str(count_20 / TRIAL_COUNT))
print("Prob W <= 30: " + str(count_30 / TRIAL_COUNT))
print("Prob W > 40: " + str(count_40 / TRIAL_COUNT))
print("Prob W > 50: " + str(count_50 / TRIAL_COUNT))
print("Prob W > 60: " + str(count_60 / TRIAL_COUNT))
print("Prob W > 65: " + str(count_65 / TRIAL_COUNT))