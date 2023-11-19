import math


def f(x):
    return 4 * 1 / math.e ** (0.5 * x) - x


def ft(x):
    return -2 * 1 / math.e ** (0.5 * x) - 1


x0 = 2
for i in range(4):
    x1 = x0 - f(x0) / ft(x0)
    x0 = x1

print(x1)
print(f(x1))