tolerance = 1e-6


def f(x):
    return x**2 + x - 3


def df(x):
    return 2*x + 1


def g(x):
    return 3 / (x + 1)


def bisection(a, b):
    iterations = 0
    while abs(b - a) / 2 > tolerance:
        c = (a + b)/2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return c, iterations


def fixed_point(x0):
    iterations = 0
    while True:
        x1 = g(x0)
        iterations += 1
        if abs(x1 - x0) > tolerance:
            x0 = x1
        else:
            return x1, iterations


def newton_raphson(x0):
    iterations = 0
    while True:
        x1 = x0 - f(x0) / df(x0)
        iterations += 1
        if abs(x1 - x0) > tolerance:
            x0 = x1
        else:
            return x1, iterations

print("Methods \tSolutions \tIterations")
print("Bisection \t{:f} \t{}".format(*bisection(a=1, b=2)))
print("Fixed point \t{:f} \t{}".format(*fixed_point(x0=1)))
print("Newton Raphson \t{:f} \t{}".format(*newton_raphson(x0=1)))
