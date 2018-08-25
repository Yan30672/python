def honai(n,A,B,C):
    if n == 1:
        return [(A,C)]
    else:
        return honai(n-1,A,C,B)+honai(1,A,B,C)+honai(n-1,B,A,C)

n = int(input('請輸入盤數:'))
for move in honai(n,'A','B','C'):
    print('盤由 %c 移到 %c' % move)