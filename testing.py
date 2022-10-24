a = 24693
c = 3517
K = 2**17
n=53
xValues = [1000]
for y in range(1,n+1):
  xValues.append((a*xValues[y-1]+c)%K)
uValues = []
for x in xValues:
  uValues.append(x/float(K))
print(f'u1: {uValues[1]}')
print(f'u2: {uValues[2]}')
print(f'u3: {uValues[3]}')
print(f'u51: {uValues[51]}')
print(f'u52: {uValues[52]}')
print(f'u53: {uValues[53]}')
