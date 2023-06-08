#!/usr/bin/env python

"""Programa p4.py"""

import numpy as np
from sor import (
    get_D,
    get_L,
    get_U,
    get_M_sor,
    get_M_jac,
    spectral_radius,
    is_spectral_radius_less_1,
    is_positive_definite,
    is_symmetric,
    w_opt,
)

# Create matrix permutation
e_1 = np.zeros(shape=(3, 1), dtype=float)
e_1[0] = 1.0

e_2 = np.zeros(shape=(3, 1), dtype=float)
e_2[1] = 1.0

e_3 = np.zeros(shape=(3, 1), dtype=float)
e_3[2] = 1.0

P = np.concatenate([e_1, e_3, e_2], axis=1)

A = np.array(object=[[1, 1, 1], [-1, 1, 0], [-1, 0, 2]], dtype=float)
A = A @ P
b = np.array(object=[[80, 1, -22]], dtype=float).T

A_tilde = A.T @ A
b_tilde = A.T @ b

print(f"¿A.T @ A es simétrica? {is_symmetric(A_tilde)}")
print(f"¿A.T @ A es definida positiva? {is_positive_definite(A_tilde)}")

D = get_D(A_tilde)
L = get_L(A_tilde)
U = get_U(A_tilde)

M_jac = get_M_jac(A_tilde)
omega_opt = 2 / (1 + np.sqrt(1 - spectral_radius(M_jac) ** 2))


if __name__ == "__main__":
    print(f"A.T @ A=\n{A_tilde}\n")
    print(f"A.T @ b=\n{b_tilde}\n")
    print(f"D=\n{D}\n")
    print(f"L=\n{L}\n")
    print(f"U=\n{U}\n")
    assert (A_tilde == D - L - U).all()
    # TODO: Check tridiagonal matrix
    # assert (
    #     np.diag(v=A_tilde, k=-1) + np.diag(A_tilde, 0) + np.diag(A_tilde, 1) == A_tilde
    # ).all()
    print(f"M_jac=\n{M_jac}\n")
    print(f"rho(M_jac) = {spectral_radius(M_jac)}\n")
    print(f"omega_opt = {omega_opt}\n")
    print(f"M_sor=\n{get_M_sor(A, omega_opt)}\n")
    # print(f"rho(M_sor)=\n{spectral_radius(get_M_sor(A, 1))}\n")
    # print(f"{is_spectral_radius_less_1(get_M_sor(A, 1))}")
    # print(f"A.T @ A=\n{A_tilde}\n")
    # print(f"A.T @ b=\n{b_tilde}\n")
    # print(f"w_opt= {w_opt(A_tilde)}")
    # print(f"x=\n{x}\n")

# x = np.linalg.solve(A, b)
