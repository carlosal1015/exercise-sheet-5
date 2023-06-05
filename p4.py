#!/usr/bin/env python

"""Programa p4.py"""

import numpy as np
from sor import get_D, get_L, get_U, get_M_sor, spectral_radius, is_spectral_radius_less_1, is_positive_definite, is_symmetric, w_opt

A = np.array(object=[[1, 1, 1],
                     [-1, 1, 0],
                     [-1, 0, 2]],
             dtype=float)

b = np.array(object=[[80, 1, -22]],
             dtype=float).T

D = get_D(A)
L = get_L(A)
U = get_U(A)

A_tilde = A.T @ A
b_tilde = A.T @ b

if __name__ == "__main__":
  print(f"A=\n{A}\n")
  print(f"D=\n{D}\n")
  print(f"L=\n{L}\n")
  print(f"U=\n{U}\n")
  assert (A == D - L - U).all()
  print(f"M_sor=\n{get_M_sor(A, 1)}\n")
  print(f"rho(M_sor)=\n{spectral_radius(get_M_sor(A, 1))}\n")
  print(f"{is_spectral_radius_less_1(get_M_sor(A, 1))}")
  print(f"A.T @ A=\n{A_tilde}\n")
  print(f"¿A.T @ A es simétrica? {is_symmetric(A_tilde)}")
  print(f"¿A.T @ A es definida positiva? {is_positive_definite(A_tilde)}")
  print(f"w_opt= {w_opt(A_tilde)}")
  # print(f"b=\n{b}\n")