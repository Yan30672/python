# perfect square checker

d=float(input('請輸入正整數:'))
for i in range(int(d**0.5)+1):
    if i**2 ==d:
        print('d是一個完全平方數')
        break
else:
    print('d不是一個完全平方數')