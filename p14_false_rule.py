# -*- coding: utf-8 -*-
from math import exp

def false_rule(func, x0: float, x1: float, kmax: int = 300, eps:float = 1e-5) ->  float:
    x = 0 # Nuevo punto intermedio
    i = 1 # Iteración
    eval = 100 # Valor arbitrario mayor que 'eps'
    while abs(eval) > eps and i < kmax: # criterio de parada
        x = x1 -func(x1) * ((x1 -x0) / (func(x1) -func(x0)))
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

# Function
func = lambda x:  exp(x) + x

# Interval
x0, x1 = -1, 0

if is_valid_interval(func, x0, x1):
    print(f"El intervalo [{x0}, {x1}] es válido para el método de regla falsa.")
    print("Iter.\t[x0, x1]")
    false_rule(func, -1, 0)

    

