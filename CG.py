import math
import numpy as np


# Returns whether M is in diagonal shape or not
# input: matrix M
# output: boolean

def is_diagonal(M):
    A = np.zeros(M.shape)
    np.fill_diagonal(A, M.diagonal())
    return np.all(A == M)


# Solves Ax = b if A is in diagonal shape
# input: matrix A, vector b
# output: vector x solving Ax = b

def solve_AIsDiag(A, b):
    x = np.copy(np.diag(A))
    for i in range(len(b)):
        x[i] = b[i] / x[i]
    return x


# CG algorithm to solve an equotion like A*x = b
# input: matrix s.p.d. A , n x 1 vector b, iteration maximum itmax, tolerance eps, startpoint x
# output: vector x solving the equotion

def CG(A, b, itmax, eps, x):
    if is_diagonal(A):
        return solve_AIsDiag(A, b)

    it = 0
    r = np.subtract(b, A.dot(x))
    r_norm = np.dot(r, r)
    r_new_norm = np.dot(r, r)
    p = np.zeros(b.size)
    beta = 0
    r_old = np.copy(r) + np.ones_like(b)

    while (math.sqrt(r_new_norm) > eps) and (np.linalg.norm(r_old - r) > eps * (1 + np.linalg.norm(r))):

        if(it == itmax):
            print("Maximale Iteration erreicht!")
            return x
        if it > 0:                                 # erst ab zweiter Iteration
            beta = r_new_norm/r_norm                # beta = r*r / r_alt*r_alt
            r_norm = r_new_norm
        p = np.add(r, beta*p)                       # p = r + bata*p

        if np.dot(p, np.dot(A, p)) <= 0:            # Abbruch der Schleife, falls A nicht pos. def.
            x = x + (np.dot(b - np.dot(A, x), p) / np.dot(p, np.dot(A, p))) * p
            return x
        alpha = r_norm/(np.dot(p, np.dot(A, p)))    # alpha = r*r/(p*A*p)
        x = np.add(x, alpha*p)                      # x = x + alpha*p
        r_old = np.copy(r)                          # r sichern
        r = np.subtract(r, alpha*np.dot(A, p))      # r = r - alpha*A*p
        r_new_norm = np.dot(r, r)                   # r*r
        it = it + 1
    return x
