from functools import reduce

d = int(input('請輸入私鑰:'))
n = int(input('請輸入大數:'))
str = input('請輸入欲解密的文:')
target_list = [int(x) for x in str.split(',')]
decoded = map(lambda x: x ** d % n, target_list)
b = list(decoded)

c = list(map(chr, b))
def f(x,y):
  return x+y

messege = reduce(f, c)
print('解密:{}'.format(messege))