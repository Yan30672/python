import random

Sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]
          ]


# 定義9個區塊，以序數作為輸出在實際Sudoku上的值
def block(i):
  if 1 <= i <= 3:
    return [(x, y) for x in range(0, 3) for y in range(3 * (i - 1), 3 * i)]
  elif 4 <= i <= 6:
    return [(x, y) for x in range(3, 6) for y in range(3 * (i - 4), 3 * (i - 3))]
  else:
    return [(x, y) for x in range(6, 9) for y in range(3 * (i - 7), 3 * (i - 6))]


# sudoku中block1,block5,block9為互相獨立互不干擾的區塊，令為basis
basis1 = sorted(block(1), key=lambda k: random.random())
basis2 = sorted(block(5), key=lambda k: random.random())
basis3 = sorted(block(9), key=lambda k: random.random())



# 檢查兩點有無同行或同列
def check(q1, q2):
  return q1[0] == q2[0] or q1[1] == q2[1]


# 檢查要生成的block是否有與其他已生成區塊check到，有重疊到則回傳true
# 如果第n個位置check後同行或同列，則希望函數回傳大於零的值
def incheck(list1, list2):
  number = 0
  for n in range(9):
    if check(list1[n], list2[n]):
      number += 1
    else:
      number += 0
  return number != 0


def row1(m):
  return [(m, 0), (m, 1), (m, 2)]


def row2(m):
  return [(m, 3), (m, 4), (m, 5)]


def row3(m):
  return [(m, 6), (m, 7), (m, 8)]


def column1(n):
  return [(0, n), (1, n), (2, n)]


def column2(n):
  return [(3, n), (4, n), (5, n)]


def column3(n):
  return [(6, n), (7, n), (8, n)]


def gen_block2(m, n, newlist):
  return {basis2.index(pt) for pt in column2(n)}.union( \
    {basis1.index(pt) for pt in row1(m)}, {newlist.index(pt) \
                                           for pt in row3(m)}) == {0, 1, 2, 3, 4, 5, 6, 7, 8}


def gen_block4(m, n, newlist):
  return {basis2.index(pt) for pt in row2(m)}.union( \
    {basis1.index(pt) for pt in column1(n)}, {newlist.index(pt) \
                                              for pt in column3(n)}) == {0, 1, 2, 3, 4, 5, 6, 7, 8}


def gen_block6(m, n, newlist):
  return {basis2.index(pt) for pt in row2(m)}.union( \
    {basis3.index(pt) for pt in column3(n)}, {newlist.index(pt) \
                                              for pt in column1(n)}) == {0, 1, 2, 3, 4, 5, 6, 7, 8}


def gen_block8(m, n, newlist):
  return {basis2.index(pt) for pt in column2(n)}.union( \
    {basis3.index(pt) for pt in row3(m)}, {newlist.index(pt) \
                                           for pt in row1(m)}) == {0, 1, 2, 3, 4, 5, 6, 7, 8}


# i == 3, 生成new3的原則
def first_generate_3(i):
  newlist = random.sample(block(i), len(block(i)))
  while incheck(newlist, basis1) == 1 or incheck(newlist, basis3) == 1 or \
          gen_block2(0, 3, newlist) == 1 or gen_block2(1, 3, newlist) == 1 or gen_block2(2, 3, newlist) == 1 \
          or gen_block2(0, 4, newlist) == 1 or gen_block2(1, 4, newlist) == 1 or gen_block2(2, 4, newlist) == 1 \
          or gen_block2(0, 5, newlist) == 1 or gen_block2(1, 5, newlist) == 1 or gen_block2(2, 5, newlist) == 1 \
          or gen_block6(3, 6, newlist) == 1 or gen_block6(3, 7, newlist) == 1 or gen_block6(3, 8, newlist) == 1 \
          or gen_block6(4, 6, newlist) == 1 or gen_block6(4, 7, newlist) == 1 or gen_block6(4, 8, newlist) == 1 \
          or gen_block6(5, 6, newlist) == 1 or gen_block6(5, 7, newlist) == 1 or gen_block6(5, 8, newlist) == 1:
    newlist = random.sample(block(i), len(block(i)))
  return newlist


# i == 7, 生成new7的原則
def first_generate_7(i):
  newlist = random.sample(block(i), len(block(i)))
  while incheck(newlist, basis1) == 1 or incheck(newlist, basis3) == 1 or \
          gen_block4(3, 0, newlist) == 1 or gen_block4(3, 1, newlist) == 1 or gen_block4(3, 2, newlist) == 1 \
          or gen_block4(4, 0, newlist) == 1 or gen_block4(4, 1, newlist) == 1 or gen_block4(4, 2, newlist) == 1 \
          or gen_block4(5, 0, newlist) == 1 or gen_block4(5, 1, newlist) == 1 or gen_block4(5, 2, newlist) == 1 \
          or gen_block8(6, 3, newlist) == 1 or gen_block8(7, 3, newlist) == 1 or gen_block8(8, 3, newlist) == 1 \
          or gen_block8(6, 4, newlist) == 1 or gen_block8(7, 4, newlist) == 1 or gen_block8(8, 4, newlist) == 1 \
          or gen_block8(6, 5, newlist) == 1 or gen_block8(7, 5, newlist) == 1 or gen_block8(8, 5, newlist) == 1:
    newlist = random.sample(block(i), len(block(i)))
  return newlist


new3 = first_generate_3(3)
new7 = first_generate_7(7)


def sub_possible_4(pt):
  S = []
  for k in range(9):
    if check(pt, basis1[k]) == 0 and check(pt, basis2[k]) == 0 and check(pt, new7[k]) == 0:
      S.append(k)
  return S


def sub_possible_2(pt):
  S = []
  for k in range(9):
    if check(pt, basis1[k]) == 0 and check(pt, basis2[k]) == 0 and check(pt, new3[k]) == 0:
      S.append(k)
  return S


def sub_possible_6(pt):
  S = []
  for k in range(9):
    if check(pt, basis3[k]) == 0 and check(pt, basis2[k]) == 0 and check(pt, new3[k]) == 0:
      S.append(k)
  return S


def sub_possible_8(pt):
  S = []
  for k in range(9):
    if check(pt, basis3[k]) == 0 and check(pt, basis2[k]) == 0 and check(pt, new7[k]) == 0:
      S.append(k)
  return S


sub_new2 = [(pt, value) for pt in block(2) for value in sub_possible_2(pt)]
sub_new4 = [(pt, value) for pt in block(4) for value in sub_possible_4(pt)]
sub_new6 = [(pt, value) for pt in block(6) for value in sub_possible_6(pt)]
sub_new8 = [(pt, value) for pt in block(8) for value in sub_possible_8(pt)]

sub_column = sub_new2 + sub_new8
sub_row = sub_new4 + sub_new6

def possible_value(pt, family):
  S = []
  for k in range(len(family)):
    if family[k][0] == pt:
      S.append(family[k][1])
    else:
      pass
  return S


def possible_pair(family, block):
  S = []
  for pt in block:
    S.append((pt, possible_value(pt, family)))
  return S


def left_points(family):
  S = []
  for k in range(len(family)):
    if family[k][0] in S:
      pass
    else:
      S.append(family[k][0])
  return S

#family = possible_pair(sub_column, left_points(sub_column))
def unique_value(family):
  S = []
  for k in range(len(family)):
    if len(family[k][1]) == 1:
      S.append((family[k][0], family[k][1][0]))
    else:
      pass
  return S

def new_column(i):
  S = []
  if i == 1:
    rem = [1]
    while len(rem) != 0:
      Del = unique_value(possible_pair(sub_column, left_points(sub_column)))
      for elem in Del:
        sub_column.remove(elem)
        S.append(elem)
      rem = []
      for elem in Del:
        for v in sub_column:
          if elem[1] == v[1] and check(elem[0], v[0]) == 1:
            rem.append(v)
          else:
            pass
      for elem in rem:
        if elem in sub_column:
          sub_column.remove(elem)
        else:
          pass
  else:
    pass
  return S

def new_row(i):
  S = []
  if i == 1:
    rem1 = [1]
    while len(rem1) != 0:
      Del = unique_value(possible_pair(sub_row, left_points(sub_row)))
      for elem in Del:
        sub_row.remove(elem)
        S.append(elem)
      rem1 = []
      for elem in Del:
        for v in sub_row:
          if elem[1] == v[1] and check(elem[0], v[0]) == 1:
            rem1.append(v)
          else:
            pass
      for elem in rem1:
        if elem in sub_row:
          sub_row.remove(elem)
        else:
          pass
  else:
    pass
  return S

block28 = new_column(1)
block46 = new_row(1)

while len(block28) != 18 or len(block46) != 18:
  basis1 = sorted(block(1), key=lambda k: random.random())
  basis2 = sorted(block(5), key=lambda k: random.random())
  basis3 = sorted(block(9), key=lambda k: random.random())
  new3 = first_generate_3(3)
  new7 = first_generate_7(7)
  sub_new2 = [(pt, value) for pt in block(2) for value in sub_possible_2(pt)]
  sub_new4 = [(pt, value) for pt in block(4) for value in sub_possible_4(pt)]
  sub_new6 = [(pt, value) for pt in block(6) for value in sub_possible_6(pt)]
  sub_new8 = [(pt, value) for pt in block(8) for value in sub_possible_8(pt)]
  sub_column = sub_new2 + sub_new8
  sub_row = sub_new4 + sub_new6
  block28 = new_column(1)
  block46 = new_row(1)

SP = []
for n in range(9):
  SP.append((basis1[n],n+1))
for n in range(9):
  SP.append((basis2[n],n+1))
for n in range(9):
  SP.append((basis3[n],n+1))
for n in range(9):
  SP.append((new3[n],n+1))
for n in range(9):
  SP.append((new7[n],n+1))
for n in range(len(block28)):
  SP.append((block28[n][0],block28[n][1]+1))
for n in range(len(block46)):
  SP.append((block46[n][0],block46[n][1]+1))

for n in range(len(SP)):
  Sudoku[SP[n][0][0]][SP[n][0][1]] = SP[n][1]

for row in Sudoku:
  for block in row:
    {
      0: lambda: print(' 0', end=''),
      1: lambda: print(' 1', end=''),
      2: lambda: print(' 2', end=''),
      3: lambda: print(' 3', end=''),
      4: lambda: print(' 4', end=''),
      5: lambda: print(' 5', end=''),
      6: lambda: print(' 6', end=''),
      7: lambda: print(' 7', end=''),
      8: lambda: print(' 8', end=''),
      9: lambda: print(' 9', end=''),
    }[block]()
  print()