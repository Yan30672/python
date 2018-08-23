from functools import reduce

e = int(input('請輸入公鑰:'))
n = int(input('請輸入大數:'))
RSA = str(input('請輸入欲加密的英文:'))

ascii = map(ord, RSA)
encrypted = map(lambda elem: elem ** e % n, ascii)
a = list(encrypted)
print('加密:{}'.format(a))