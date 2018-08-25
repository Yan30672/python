class Mouse:
    @staticmethod #能使用Mouse.go(maze, start, end)型式的語法
    def go(maze, start, end): #回傳visit後的route(路徑集合)
        route = [] #什麼都還沒走
        Mouse.visit(maze, start, end, route) #訪問過的點
        return route

    @staticmethod
    def visit(maze, pt, end, route):
        if Mouse.isVisitable(maze, pt, route):
            route.append(pt) #visitable則增加pt
            if not Mouse.isEnd(route, end) and not Mouse.tryOneOut(maze, pt, end, route):
                route.pop()
        return Mouse.isEnd(route, end)

    @staticmethod
    def isVisitable(maze, pt, route):
        return maze[pt[0]][pt[1]] == 0 and pt not in route
        # pt是道路而且還不在route裡

    @staticmethod
    def isEnd(route, end):
        return end in route #route走到尾巴了沒

    @staticmethod
    def tryOneOut(maze, pt, end, route): #maze中pt鄰近四點
        return Mouse.visit(maze, (pt[0], pt[1] + 1), end, route) or \
               Mouse.visit(maze, (pt[0] + 1, pt[1]), end, route) or \
               Mouse.visit(maze, (pt[0], pt[1] - 1), end, route) or \
               Mouse.visit(maze, (pt[0] - 1, pt[1]), end, route)

maze = [[2, 2, 2, 2, 2, 2, 2],
        [0, 0, 0, 0, 0, 0, 2],
        [2, 0, 2, 0, 2, 0, 2],
        [2, 0, 0, 2, 0, 2, 2],
        [2, 2, 0, 2, 0, 2, 2],
        [2, 0, 0, 0, 0, 0, 2],
        [2, 2, 2, 2, 2, 0, 2]]

print(maze)

for pt in Mouse.go(maze, (1, 0), (6, 5)):
    maze[pt[0]][pt[1]] = 1

if maze[5][5] == 0:
    print("找不到出口")

for row in maze:
    for block in row:
        {
            0 : lambda: print('　', end=''),
            1 : lambda: print('Ｏ', end=''),
            2 : lambda: print('口', end=''),
        }[block]()
    print()