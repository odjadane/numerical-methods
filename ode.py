import numpy as np
import matplotlib.pyplot as plt


def f(tn, yn):
    return yn * np.sin(tn)**2


def euler(t, y0):
    n = len(t)
    y = np.zeros(n)
    y[0] = y0
    for i in range(n-1):
        y[i+1] = y[i] + (t[i+1] - t[i]) * f(t[i], y[i])
    return y


def rk4(t, y0):
    n = len(t)
    y = np.zeros(n)
    y[0] = y0
    for i in range(n-1):
        h = t[i+1] - t[i]
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h/2, y[i] + (h/2) * k1)
        k3 = f(t[i] + h/2, y[i] + (h/2) * k2)
        k4 = f(t[i] + h, y[i] + h * k3)
        y[i+1] = y[i] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    return y

t = np.linspace(0, 1, 10)
y = np.exp(0.5*(t - np.sin(t) * np.cos(t)))
ye = euler(t, y0=1)
ys = rk4(t, y0=1)

plt.plot(t, y, c='red', label='Exact solution')
plt.scatter(t, ye, s=75, c='green', marker='^', label="Euler's method")
plt.scatter(t, ys, s=75, c='blue', marker='X', label="RK4's method")
plt.title('Solutions of ODE')
plt.legend(loc='best')
plt.grid()
plt.show()
