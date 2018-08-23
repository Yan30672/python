x=input('請輸入正整數:')
name=set(x)

if len(name)==1:
    print('{} is a rep-digits number.'.format(x))
else:
    print('{} is not a rep-digits number.'.format(x))