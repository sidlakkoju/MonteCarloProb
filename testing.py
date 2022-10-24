import math
import random
a = 24693
c = 3517
K = 2**17
kay=2**17
n=1000
xValues = [1000]
for y in range(1,kay+1):
  xValues.append((a*xValues[y-1]+c)%K)
uValues = []
for x in xValues:
  uValues.append(x/float(K))
xDist=[]
for u in uValues:
  xDist.append(-12*math.log(1-u))
w=[]
for i in range(n)
  j=0
  t=0
  while(j<4)
    l=random.randInt(1,10)
    if l <= 2:
      t+=4
      j+=1
    else if l <= 5:
      t+=26
      j+=1
    else:
      p = random.randInt(1,kay)
      x = xDist[p]
      if x>25:
        t+=26
        j+=1
      else:
        t+=x
        j=5
  w.append(t)
