#!/usr/bin/env python

"""Programa p14.py"""

import numpy as np
import matplotlib.pyplot as plt

nx = 101
x = np.linspace(start=-5.0, stop=5.0, num=nx)
y = np.exp(x) + x

@np.vectorize
def constant_function(x):
    return 0

if __name__ == "__main__":
  fig, ax = plt.subplots()
  ax.plot(x, y, label="Curve")
  ax.plot(x, constant_function(x), label="Line")
  ax.legend()
  # plt.show()
  fig.savefig('p14.pdf')