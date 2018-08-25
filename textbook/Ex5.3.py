start = (x,y)
x = int(input('請輸入x座標'))
y = int(input('請輸入y座標'))

class Knight:
    @staticmethod
    def possible(route, step):
        dirs = [(-2, 1), (-1, 2), (1, 2), (2, 1),
                (2, -1), (1, -2), (-1, -2), (-2, -1)]
        steps = [(step[0] + dir[0], step[1] + dir[1]) for dir in dirs]
        return [step for step in steps if Knight.isVisitable(route, step)]

    @staticmethod
    def isVisitable(route, step):
        return step[0] > -1 and step[0] < 8 and \
               step[1] > -1 and step[1] < 8 and \
               not step in route


board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]