#!/usr/bin/env python

"""Programa p31.py"""

import sympy as sp

R = sp.Matrix([[1, 1], [0, 1]])
D = sp.eye(2)
R_1 = D * R

if __name__ == "__main__":
  print("R=")
  sp.pprint(R)
  print(f"¿R es triangular superior? {R.is_upper}.")
  print(f"|R|={R.det()}.")
  print("D=")
  sp.pprint(D)
  print("R_1=")
  sp.pprint(R_1)
  print(f"¿R_1 es triangular superior? {R_1.is_upper}.")
  print(f"|R_1|={R_1.det()}.")