import matplotlib.pyplot as plt
import numpy as np

def R(s,t,n):
  return -np.sin(t*np.log(n))/n**s

def L(s,t, n):
  return np.cos(t*np.log(n))/n**s

def zeta_real(s,t, m):
  return sum(L(s,t,n) for n in range(1,m+1))

def zeta_img(s,t,m):
  return sum(R(s,t,n) for n in range(1,m+1))

def zeta(s,t, m):
  return zeta_real(s,t,m)+1j*zeta_img(s,t,m)

S = np.arange(2, 10, 1)
T = np.arange(-5, 5, 0.01)

points = [(s,t) for s in S for t in T]
output = [zeta(s,t,100) for (s,t) in points]
domain = [s+t*1j for (s,t) in points]
plt.axvline(x=1/2)
X1 = [x.real for x in domain]
Y1 = [x.imag for x in domain]
plt.scatter(X1,Y1,color = 'c', s=1**2)
X2 = [x.real for x in output]
Y2 = [x.imag for x in output]
plt.scatter(X2,Y2, color = 'm', s=1**2)
plt.savefig("filename.png")
plt.show()