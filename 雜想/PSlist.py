import math

def f(x):
    return math.sqrt(x) % 1 == 0


print(list(filter(f, range(101))))