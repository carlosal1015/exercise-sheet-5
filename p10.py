#!/usr/bin/env python

"""Programa p10.py"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]

nx = 101
x = np.linspace(start=0.1, stop=2.0, num=nx)
y = x * np.log(x) - 1


@np.vectorize
def constant_function(x):
    return 0


if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.plot(x, y, label=r"$x\ln(x)-1$", lw=0.5)
    ax.plot(x, constant_function(x), label=r"$0$", lw=0.5)
    ax.legend(shadow=True, title="Leyenda", fancybox=True)
    # plt.show()
    fig.savefig("p10.pdf", transparent=True, bbox_inches="tight")
