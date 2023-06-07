#!/usr/bin/env python

"""Programa p32.py"""

import sympy as sp

A = sp.Matrix([[1, 0, 0], [2, 1, -1]])
Q, R = A.QRdecomposition()
G = A.T * A  # .cholesky()
sigma = G.eigenvals()

if __name__ == "__main__":
    print("A=")
    sp.pprint(A)
    print(f"rank(A)={A.rank()}")
    print("Q=")
    sp.pprint(Q)
    print("R=")
    sp.pprint(R)
    assert (Q * Q.T).equals(sp.Identity(2))
    print("G=")
    sp.pprint(G)
    sp.pprint()
    # assert (A.T * A).equals(G * G.T)
