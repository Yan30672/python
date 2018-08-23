p=int(input('請輸入p值:'))

import math

def ncr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)

def L(p,i):
    return ncr(2*p+1,2*i)*(361**(p-i))*(360**i)

def R(p,i):
    return ncr(2*p+1,2*i+1)*(361**(p-i))*(360**i)

S = sum(L(p,i) for i in range(0,p+1))

T = sum(R(p,i) for i in range(0,p+1))

print('19S+9T={}'.format(int(19*S+9*T)))
print('19S-9T={}'.format(int(19*S-9*T)))