d=float(input('請輸入度數:'))
d1=2.12*d
d2=2.12*330+2.91*(d-330)
d3=2.12*330+2.91*370+3.44*(d-700)
d4=2.12*330+2.91*370+3.44*800+5.05*(d-1500)

if d<=330:
    print('{}元'.format(d1))
elif 330<d<=700:
    print('{}元'.format(d2))
elif 700<d<=1500:
    print('{}元'.format(d3))
else:
    print('{}元'.format(d4))