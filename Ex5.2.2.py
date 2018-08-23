#Transformation

import numpy as np

#矩陣的拓樸
def unit_circle(pt):
    return [(x,y) for y in range(0,len(a)) for x in range(0,len(a[0])) if abs(x-pt[0])+abs(y-pt[1]) == 1]


maze = [[2, 2, 2, 2, 2, 2, 2],
        [0, 0, 0, 2, 0, 0, 2],
        [2, 0, 2, 0, 2, 0, 2],
        [2, 2, 0, 2, 0, 2, 2],
        [2, 2, 2, 2, 0, 2, 2],
        [2, 0, 0, 0, 2, 0, 2],
        [2, 2, 2, 2, 2, 0, 2]]

for row in maze:
    for block in row:
        {
            0 : lambda: print('　', end=''),
            1 : lambda: print('口', end=''),
            2 : lambda: print('口', end=''),
        }[block]()
    print()

print('與以下迷宮等價')

a = np.array(maze)
zeros = [(x,y) for y in range(0,len(a)) for x in range(0,len(a[0])) if maze[x][y] == 0]
dim = [(x,y) for y in range(0,len(a)) for x in range(0,len(a[0]))]

#找出未更動的座標點
route = []
for pt in zeros:
    route += unit_circle(pt)

final_list = list(set(dim).difference(route))

for N in final_list:
    maze[N[0]][N[1]] = 1


for row in maze:
    for block in row:
        {
            0 : lambda: print('　', end=''),
            1 : lambda: print('口', end=''),
            2 : lambda: print('口', end=''),
        }[block]()
    print()