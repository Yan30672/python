# 找出所有阿姆斯壯數 a^3+b^3+c^3=abc_10

# 右邊數來第i位之值
def f(x,i):
    return int(x/10**(i-1))-10*int(x/10**i)

def is_amu(x):
    return f(x,1)**3+f(x,2)**3+f(x,3)**3 == x

print(list(filter(is_amu, range(100,1000))))