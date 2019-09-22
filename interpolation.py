import numpy as np
import matplotlib.pyplot as plt


def newton_coefficients(px, py):
    n = len(px)
    d = np.zeros((n, n))
    c = np.zeros(n)

    for i in range(n):
        d[i, 0] = py[i]
    for i in range(1, n):
        for j in range(n - i):
            d[j, i] = (d[j, i - 1] - d[j + 1, i - 1]) / (px[j] - px[i + j])
    for i in range(n):
        c[i] = d[0, i]

    return c


def newton_interpolation(x, px, c):
    n = len(px)
    p = c[-1]
    for i in range(n - 1, 0, -1):
        p = c[i - 1] + (x - px[i - 1]) * p
    return p


def lagrange_interpolation(x, px, py):
    n = len(px)
    p = 0
    for i in range(0, n):
        L = 1
        for j in range(0, n):
            if i != j:
                L = L * (x - px[j])/(px[i]-px[j])
        p = p + py[i] * L
    return p

px = [1, 2, 3, 4]
py = [9, 36, 67, 90]

x = np.linspace(-1, 5, 1000)
c = newton_coefficients(px, py)
yn = [newton_interpolation(pt, px, c) for pt in x]
yl = [lagrange_interpolation(pt, px, py) for pt in x]

plt.scatter(px, py, s=75, c='green', marker='o', label='Samples')
plt.plot(x, yn, c='red', linestyle='solid', label="Newton's interpolation")
plt.plot(x, yl, c='blue', linestyle='dotted', label="Lagrange's interpolation")
plt.title('Polynomial interpolation')
plt.legend(loc='best')
plt.grid()
plt.show()
