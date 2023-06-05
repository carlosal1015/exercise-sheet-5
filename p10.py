#!/usr/bin/env python

"""Programa p10.py"""

import numpy as np
import matplotlib.pyplot as plt

nx = 101
x = np.linspace(start=0.1, stop=2.0, num=nx)
y = x * np.log(x)

@np.vectorize
def constant_function(x):
    return 1

if __name__ == "__main__":
  fig, ax = plt.subplots()
  ax.plot(x, y, label="Curve")
  ax.plot(x, constant_function(x), label="Line")
  ax.legend()
  # plt.show()
  fig.savefig('p10.pdf')