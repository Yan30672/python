import random
import math

def isPrime(n):
  S = 1
  for num in range(2, n):
    if n % num == 0:
      S *= 0
    else:
      S *= 1
  return S

def Primelist(n):
  S = []
  for num in range(2, n):
    if isPrime(num) == 1:
      S.append(num)
    else:
      pass
  return S

def egcd(a, b):
   if a == 0:
     return (b, 0, 1)
   g, y, x = egcd(b % a, a)
   return (g, x - (b // a) * y, y)


def modinv(a, m):
  g, x, y = egcd(a, m)
  if g != 1:
    raise Exception('No modular inverse')
  return x % m

p = random.choice(Primelist(5000))
q = random.choice(Primelist(5000))

while q == p:
  q = random.choice(Primelist(5000))

n = p*q
phi = (p-1)*(q-1)

print('大數n:{}'.format(n))

e = random.choice(range(2,phi))
while math.gcd(e, phi) != 1:
  e = random.choice(range(2,phi))
print('Public key:{}'.format(e))

d = modinv(e, phi)
print('Private key:{}'.format(d))