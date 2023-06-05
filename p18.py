#!/usr/bin/env python

"""Programa p18.py"""

import numpy as np

A = np.array(object=[[2, -1, 0, 7],
                     [1, 0, 1, 3],
                     [2, 7, 7, 7]],
             dtype=float)

b = np.array(object=[[-1, 0, 1]],
             dtype=float).T

if __name__ == "__main__":
  print(f"A=\n{A}\n")
  print(f"b=\n{b}\n")