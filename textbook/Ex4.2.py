# 求n個費氏數

n = int(input('求幾個費氏數?'))

def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print(list(fib(x) for x in range(0, n)))