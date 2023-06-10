# -*- coding: utf-8 -*-
# Pregunta 14. Método de bisección

from math import exp

def bisection(func, x0: float, x1: float, kmax: int = 300, tol: float = 1e-5) ->  float:
    x = 0 # Nuevo punto intermedio
    i = 1 # Iteración
    while abs(x1 -x0) >= tol and i < kmax: # criterio de parada
        x = x0 + (x1 - x0) / 2
        eval = func(x)
        print(f"{i}\t[{x0:.5f}, {x1:.5f}]")
        if eval < 0:
            x0 = x
        else:
            x1 = x
        i += 1
    print(f"Solución: {x}")
    return x

def is_valid_interval(func, x0, x1):
    return func(x0) * func(x1) < 0

# Función
func = lambda x:  exp(x) + x

# Intervalo
x0, x1 = -1, 0

if is_valid_interval(func, x0, x1):
    print(f"El intervalo [{x0}, {x1}] es válido para el método de bisección.")
    print("Iter.\t[x0, x1]")
    bisection(func, -1, 0)

    