#modular inverse calculator

a=int(input('請輸入乘數:'))
n=int(input('請輸入模數:'))

for i in range(1,n):
    if (a*i-1) % n == 0:
        print('{}對同餘{}的模反元素為:{}'.format(a,n,i))
        break
else:
    print('模反元素不存在')