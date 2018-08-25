import matplotlib.pyplot as plt
import random

number = 0
a1 = 3
a2 = 2
plt.scatter(3, 2)
plt.scatter(0, 0)
plt.scatter(5, 0)
plt.scatter(3, 4)


def midpoint(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)


while number != 1000:
    c = random.randint(1, 6)
    if 1 <= c <= 2:
        (a1, a2) = midpoint(a1, a2, 3, 4)
        plt.scatter(a1, a2)
        number += 1
    elif 3 <= c <= 4:
        (a1, a2) = midpoint(a1, a2, 5, 0)
        plt.scatter(a1, a2)
        number += 1
    else:
        (a1, a2) = midpoint(a1, a2, 0, 0)
        plt.scatter(a1, a2)
        number += 1
plt.show()
