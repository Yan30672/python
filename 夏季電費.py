d=float(input('請輸入度數:'))
d1=2.53*d
d2=2.53*330+3.55*(d-330)
d3=2.53*330+3.55*370+4.25*(d-700)
d4=2.53*330+3.55*370+4.25*800+6.43*(d-1500)

if d<=330:
    print('{}元'.format(d1))
elif 330<d<=700:
    print('{}元'.format(d2))
elif 700<d<=1500:
    print('{}元'.format(d3))
else:
    print('{}元'.format(d4))