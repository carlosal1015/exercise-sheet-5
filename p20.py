#!/usr/bin/env python

"""Programa p20.py"""

import numpy as np

A = np.array(object=[[1, 1, 1, 1],
                     [2, 1, -1, 3],
                     [1, -2, 1, 1]],
             dtype=float)

b = np.array(object=[[1, 0, -1]],
             dtype=float).T

if __name__ == "__main__":
  print(f"A=\n{A}\n")
  print(f"b=\n{b}\n")