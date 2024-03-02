#2
from math import *
y = 0.34
u = 0
u1 = 0
print("z U")
for z in range(6, 11):
    u1 = 0
    for x in range(1, 4):
        u1 += (((tan(y))**2 + 1)**x) / sqrt(x + (1/z**2))
    u += ((sin(pi/2-y/z)+e**(y/z))/(1+y/2+(y**2)/4+(y**3)/6))*u1
    print(z , "%.3f"%u)

