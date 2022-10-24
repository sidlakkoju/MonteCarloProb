a = 24693
c = 3517
K = 2**17
n=53
xValues = [1000]
for y in range(1,n+1):
  xValues.append((a*xValues[y-1]+c)%K)
uValues = []
for x in xValues:
  uValues.append(a/float(K))
print("u1: "+uValues[1])
print("u2: "+uValues[1])
print("u3: "+uValues[1])
print("u51: "+uValues[1])
print("u52: "+uValues[1])
print("u53: "+uValues[1])
