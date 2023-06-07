import numpy as np

A = np.array(object=[[1, 1, 1], [-1, 0, 1], [-1, 2, 0]], dtype=float)
At = np.transpose(A)
A = At @ A
b = np.array(object=[[80], [1], [-22]], dtype=float)
b = At @ b
print("A:\n", A)
print("b:\n", b)

diagonal = np.diag(A)
D = np.diag(diagonal)
print("D:\n", D)
L = np.tril(-A, k=-1)
print("L:\n", L)
U = np.triu(-A, k=1)
print("U:\n", U)

TJ = np.linalg.inv(D) @ (L + U)
print("TJ:\n", TJ)
autovalores = np.linalg.eigvals(TJ)
print("Autovalores:\n", autovalores)
radio_espectral = np.max(np.abs(autovalores))
print("Radio Espectral:\n", radio_espectral)

import math

w = 2 / (1 + math.sqrt(1 - radio_espectral**2))
print("w: ", w)

from tabulate import tabulate

x = np.array(object=[[0], [0], [0]], dtype=float)

datos = [["i", "x0", "x1", "x2"]]
for i in range(9):
    x0 = (1 - w) * x[0] + (w / 3) * (101 + x[1])
    x[0] = x0
    x1 = (1 - w) * x[1] + (w / 5) * (36 + x[0] - x[2])
    x[1] = x1
    x2 = (1 - w) * x[2] + (w / 2) * (81 - x[1])
    x[2] = x2
    nueva_iteracion = [i + 1, x0, x1, x2]
    datos.append(nueva_iteracion)
tabla = tabulate(datos,
    headers="firstrow",
    tablefmt="fancy_grid",
    stralign="center")
print(tabla)
print("Edad de la Madre:", x[0])
print("Edad del Padre:", x[2])
print("Edad del Hijo:", x[1])
