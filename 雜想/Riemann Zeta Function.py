import matplotlib.pyplot as plt
import numpy as np

def R(s,t,n):
  return -np.sin(t*np.log(n))/n**s

def L(s,t,n):
  return np.cos(t*np.log(n))/n**s

def zeta_real(s,t, m):
  return sum(L(s,t,n) for n in range(1,m+1))

def zeta_img(s,t,m):
  return sum(R(s,t,n) for n in range(1,m+1))

def zeta(s,t, m):
  return zeta_real(s,t,m)+1j*zeta_img(s,t,m)

#All vertical lines
S1 = np.arange(2, 10, 1)
S2 = 1+1/S1
Y = np.arange(-5, 5, 0.01)
points1 = [(s,t) for s in S1 for t in Y] + [(s,t) for s in S2 for t in Y]
domain1 = [s+t*1j for (s,t) in points1]

VX = [x.real for x in domain1]
VY = [x.imag for x in domain1]

plt.scatter(VX,VY,color = 'c', s=1**2)

#All horizontal lines
T1 = np.arange(1,5,1)
T2 = -T1
T3 = 1/T1
T4 = 1/T2
X = np.arange(1.01, 10, 0.01)
points2 = [(s,t) for s in X for t in T1] + [(s, t) for s in X for t in T2] +\
          [(s, t) for s in X for t in T3] + [(s, t) for s in X for t in T4]
domain2 = [s+t*1j for (s,t) in points2]
HX = [x.real for x in domain2]
HY = [x.imag for x in domain2]
plt.scatter(HX,HY,color = 'm', s=1**2)



plt.savefig("Riemann Zeta.png")
plt.show()