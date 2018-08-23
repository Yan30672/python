import math

# x的從右邊開始數第i位數
def g(x,i):
    return int(x/10**(i-1))-10*int(x/10**i)

# x有幾位數
def num(x):
    return int(math.log(x,10))+1

# 計算x每個位數與個位數之差總和
def rp(x):
    return sum(abs(g(x,i)-g(x,1)) for i in range(2,num(x)+1))

def n(x):
    return int(math.sqrt(2*x))

def f(x):
    return n(x)*(n(x)+1)/2 == x and rp(x) == 0

print(list(filter(f,range(1,10000001))))