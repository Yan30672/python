import random

deposit = 10
number = 0
n = 0

def f(n,number):
    return ((-1)**(1-n))*(2**number)

while n != 1:
    c = random.randint(0, 1)
    if deposit <= 0:
        deposit = 0
        print('賭徒破產了!')
        break
    else:
        if c == 0:
            n += 0
            print('第{}次賭徒輸了，剩下本金{}元'.format(number+1,deposit + f(n,number)))
        else:
            n += 1
            print('第{}次賭徒贏了，最後拿到{}元'.format(number+1,deposit + f(n,number)))
        deposit = deposit + f(n,number)
        number += 1

print('賭徒總共賭了{}次'.format(number))