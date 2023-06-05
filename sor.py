#!/usr/bin/env python

"""Programa p4.py"""

import numpy as np

get_D = lambda M: np.diag(np.diag(M))
get_U = lambda M: -np.triu(M, k=1)
get_L = lambda M: -np.tril(M, k=-1)
get_D_inv = lambda M: np.diag(np.reciprocal(np.diag(M)))
# FIXME: implement inverse of upper matrix
get_M_sor = lambda M, w: -np.linalg.inv(1/w * get_D(M) - get_L(M)) @ get_D(M) * (w - 1) / w - get_U(M)
spectral_radius = lambda M: np.max(a=np.absolute(np.linalg.eigvals(a=M)))
is_spectral_radius_less_1 = lambda M: np.all(spectral_radius(M)) < 1

def is_symmetric(A, rtol=1e-5, atol=1e-8):
    """Retorna verdadero si la matriz A es simétrica."""
    return np.allclose(A, A.T, rtol=rtol, atol=atol)


def is_positive_definite(A):
    """Retorna verdadero si la matriz A es definida positiva."""
    return np.all(np.linalg.eigvals(A) > 0)


get_M_jac = lambda M: get_D_inv(M) @ (get_L(M) + get_U(M))

w_opt = lambda M: 2 / (1 + np.sqrt(1 - spectral_radius(get_M_jac(M))**2))