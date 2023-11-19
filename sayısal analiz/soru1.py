def f(x):
    return x * x * x - 2 * x * x - 5


x1 = 2
x2 = 4
a = f(x1)
b = f(x2)

for i in range(4):
    if a * b < 0:
        x0 = (x1 + x2)/2
        y0 = f(x0)
        if y0 * a < 0:
            x2 = x0
        elif y0 * b < 0:
            x1 = x0


print(x0)
print(y0)