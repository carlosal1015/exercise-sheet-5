#!/usr/bin/env python

"""Programa p25.py"""

import sympy as sp

alpha = sp.Symbol("alpha", real=True)

A = sp.Matrix([[5, -5, -6], [-5, 3, -1], [0, alpha, 7]])
b = sp.Matrix([-1, 1, -2])

if __name__ == "__main__":
    print(f"A=\n{A}\n")
    print(f"b=\n{b}\n")
    print(f"Rango de A es {A.rank()}")
    print(A.subs(alpha, 0))
