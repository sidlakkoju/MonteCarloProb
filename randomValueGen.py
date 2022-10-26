import sys
sys.setrecursionlimit(1500)

# Monte Carlo Random Generator
a = 24693
c = 3517
K = 2**17

def randNumStart(final):
    x0 = 1000
    cur = 0
    return randNumRec(cur, final, x0)

def randNumRec(cur, final, x):
    if cur >= final:
        return x/K
    cur += 1
    return randNumRec(cur, final, (a*x + c)%K)



'''
# First three Monte Carlo Numbers
print("Random Number 1: " + str(randNumStart(1)))
print("Random Number 2: " + str(randNumStart(1)))
print("Random Number 3: " + str(randNumStart(1)))
print("")

# Random Numbers 51, 52, 53
print("Random Number 51: " + str(randNumStart(51)))
print("Random Number 52: " + str(randNumStart(52)))
print("Random Number 53: " + str(randNumStart(53)))
print("")
'''