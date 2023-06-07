import numpy as np

A = np.array(object=[[1, 1, 1], [-1, 1, 0], [-1, 0, 2]], dtype=float)
At = np.transpose(A)
A = At @ A
b = np.array(object=[[80], [1], [-22]], dtype=float)
b = At @ b
print("A:\n", A)
print("b:\n", b)


def residuo(x):
    r = b - A @ x
    return r


def tk(v, r):
    tk = (v.T @ r) / (v.T @ (A @ v))
    return tk


def xk(x, tk, v):
    xk = x + (tk * v)
    return xk


from tabulate import tabulate

x = np.array(object=[[0], [0], [0]], dtype=float)
i = 0
r = residuo(x)
datos = [["k", "residuo(k-1)", "v(k)", "t(k)", "x(k)"]]

while not np.all(r < 0.00000001):
    i = i + 1
    r = residuo(x)
    v = r
    t = tk(v, r)
    x = xk(x, t, v)
    nueva_iteracion = [i, r, v, t, x]
    datos.append(nueva_iteracion)


tabla = tabulate(datos,
    headers="firstrow",
    tablefmt="fancy_grid",
    stralign="center")
print(tabla)

print("Edad de la Madre:", x[0])
print("Edad del Padre:", x[1])
print("Edad del Hijo:", x[2])
