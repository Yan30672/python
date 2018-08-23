import sys

d1=float(sys.argv[1])
d2=2*d1
d3=d2**0.5
d4=int(d3)
d5=d4*(d4+1)/2

if d1 != d5:
    print('{}不是三角形數'.format(sys.argv[1]))
else:
    print('{}是三角形數，序數是{}'.format(sys.argv[1],d4))