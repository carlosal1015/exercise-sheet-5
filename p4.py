#!/usr/bin/env python

"""Programa p4.py"""

import numpy as np

A = np.array(object=[[1, 1, 1],
                     [-1, 1, 0],
                     [-1, 0, 2]],
             dtype=float)

b = np.array(object=[[80, 1, -22]],
             dtype=float).T

if __name__ == "__main__":
  print(f"A=\n{A}\n")
  print(f"b=\n{b}\n")