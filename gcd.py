print('請輸入兩個數字:')

m=int(input('數字1:'))
n=int(input('數字2:'))

while n!=0:
    r = m % n
    m=n
    n=r
    if m == 1:
        print('coprime')
        break
else:
    print('gcd:',m)