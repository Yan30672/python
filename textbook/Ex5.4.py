def queenss(n):
    def placeq(k):
        if k == 0:
            return  [[]]
        else:
            return [[(k,column)] + queens for queens in placeq(k-1) for column in range(1,n+1) if isSafe((k, column), queens)]
    return placeq(n)

def inCheck(q1, q2):
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0]-q2[0]) == abs(q1[1]-q2[1])

def isSafe(queen, queens):
    return all(not inCheck(queen, q) for q in queens)

def printQueens(qs):
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

    for q in qs:
        board[q[0] - 1][q[1] - 1] = 1

    for row in board:
        for p in row:
            print(' Q' if p else ' .', end = '')
        print()

for qs in queenss(8):
    printQueens(qs)
    print()