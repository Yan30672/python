d=float(input('請輸入度數:'))
d1=7.35*d
d2=7.35*20+9.45*(d-20)
d3=7.35*20+9.45*40+11.55*(d-60)
d4=7.35*20+9.45*40+11.55*40+12.075*(d-100)

if d<=20:
    print('{}元'.format(d1))
elif 20<d<=60:
    print('{}元'.format(d2))
elif 60<d<=100:
    print('{}元'.format(d3))
else:
    print('{}元'.format(d4))