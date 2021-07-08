#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from numba import njit
from scipy.linalg import eigh_tridiagonal

# definir MODELO DE DESORDEM:
@njit(parallel=True)
def laco(A,N):
    Y = []
    z = np.random.random(N)*2-1
    for i in range(1,(N+1)):
        y = 0
        for j in range(1,(N+1)):
            y += z[j-1]/((1+abs(i-j)/A)**(2))
        Y.append(y)
        
    return Y


def rand(A,N):
    Y = laco(A,N)
    e = []
    for l in range(N):
        E = (Y[l] - np.average(Y))/np.std(Y)
        e.append(E)
    return e

# definir AUTOVALORES(W) e AUTOVETORES(V) no intervalo [-0.05, 0.05]:
    
def eigen_v(A,N):
    d_p = rand(A, N)
    d_s = np.ones(N-1)
    V = eigh_tridiagonal(d_p, d_s, select='v', select_range=(-0.05,0.05))
    return V[1] #retorna os autovetores

# definir a PARTICIPACAO MEDIA no centro da banda:

def particip(V):
    part = []
    V    = V.T
    for l in range(len(V)):
        f_n = []
        for c in V[l]:
            f_n.append(abs(c**4))
        p = 1/sum(f_n)
        part.append(p)            
    return np.average(part)

# definir PARTICIPACAO versus N:
    
def part_x_N(A,N):
    eixo_x = []
    eixo_y = []
    M = [3200,1600,800,400,200,100]
    i = 0
    while N <= 32000:
        y = []
        for j in range(M[i]): 
            part = particip(eigen_v(A,N))
            y.append(part)
        eixo_x.append(N)
        eixo_y.append(np.average(y))
        i += 1
        N *= 2
    return eixo_x, eixo_y
        
# salvar os dados em um .dat

A       = 400
N       = 1000
F = False
while A <=  800:
    x , y   = part_x_N(A,N)
    df      = pd.DataFrame({'x':x,'y':y})
    df.to_csv('part_x_N_A%d.dat' %(A), index=F, header=F, sep=' ' )
    A *= 2

