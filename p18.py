#!/usr/bin/env python

"""Programa p18.py"""

import numpy as np

A = np.array(object=[[2, -1, 0, 7],
                     [1, 0, 1, 3],
                     [3, 2, 7, 7]],
             dtype=float)

b = np.array(object=[[-1, 0, 1]],
             dtype=float).T

A_tilde = A.T @ A
b_tilde = A.T @ b

if __name__ == "__main__":
  print(f"A=\n{A}\n")
  print(f"b=\n{b}\n")
  print(f"A.T @ A=\n{A_tilde}\n")
  print(f"A.T @ b=\n{b_tilde}\n")
  print(f"det(A.T @ A) = {np.linalg.det(A_tilde)}")
  print(f"rank(A.T @ A) = {np.linalg.matrix_rank(A_tilde)}\n")
  print(f"rank(A.T @ A | A.T @ b) = {np.linalg.matrix_rank(np.concatenate((A_tilde, b_tilde), axis=1))}\n")