# 找出周長為24，三邊長都是整數的直角三角形

num = range(1,24)

edge = [(a,b,c) for a in num for b in num for c in num if a+b+c == 24 if a**2+b**2 == c**2]

print(edge)