import numpy as np
tolerance = 1e-3
omega = 1.3


def solver(M, N, x0):
    G = np.matmul(np.linalg.inv(M), N)
    c = np.matmul(np.linalg.inv(M), B)
    i = 0
    while True:
        x1 = np.matmul(G, x0) + c
        i += 1
        error = np.linalg.norm(x1 - x0, np.inf) / np.linalg.norm(x1, np.inf)
        if error > tolerance:
            x0 = x1
        else:
            return x1, i

A = np.array([(26, -1, 3), (-1, 1, -2), (3, -2, 6)])
B = np.array([-9, 7, -18])
x0 = np.array([0, 0, 0])

I = np.eye(3)
D = np.diag(np.diag(A))
E = -(np.tril(A) - D)
F = -(np.triu(A) - D)

print("Methods \t\tSolutions \tIterations")
with np.printoptions(formatter={'float': '{: 0.3f}'.format}):
    print("Jacobi \t\t{} \t{}".format(*solver(D, E+F, x0)))
    print("GS \t\t{} \t{}".format(*solver(D-E, F, x0)))
    print("SOR \t\t{} \t{}".format(*solver((1/omega)*D-E, ((1-omega)/omega)*D+F, x0)))
