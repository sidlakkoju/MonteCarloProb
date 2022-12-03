import sys
sys.setrecursionlimit(1000)

# Monte Carlo Random Generator
a = 24693
c = 3967
K = 2**18

def randNumStart(final):
    x0 = 1000
    cur = 0
    return randNumRec(cur, final, x0)

def randNumRec(cur, final, x):
    if cur >= final:
        return x/K
    cur += 1
    return randNumRec(cur, final, (a*x + c)%K)



class randNumGenerator :
    def __init__(self):
        self.a = 24693
        self.c = 3967
        self.K = 2**18
        self.x0 = 1000
        self.final = 1
        self.cur = 0
    
    def getRandNum(self):
        self.cur += 1

        self.x0 = (self.a*self.x0 + self.c)%self.K

        #if self.cur >= self.final:
        return self.x0/self.K
        
        
            
        



gen = randNumGenerator()
print(gen.getRandNum())
print(gen.getRandNum())
print(gen.getRandNum())