#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 14:29:24 2018

@author: apple
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x)
def Trap(func, a, b, N) :
    h = float(b - a)/float(N)
    X = np.linspace(a,b,num=N+1)
    ITrap = h * ((np.sum( f(X))-(f(a)/2)-(f(b)/2)))
    Traperr= np.e -1-ITrap
    plt.plot( N, Traperr,'bo')
    return ITrap

def Simp(func, a, b, N) :
    h = float(b - a)/float(N)
    end=np.linspace(a,b,num=(N/2)+1)
    mid=np.linspace(a+h, b-h, num=(N/2))
    ISimp = (h/float(3))*((2*np.sum(f(end))+ 4*np.sum(f(mid)))-f(a)-f(b))
    Simperr = np.e -1-ISimp
    plt.plot( N, Simperr, 'ro')
    return ISimp

cnt = 0
reldiff = 1
accu = 1e-10
N0= 1
while abs(reldiff) > accu:
    old = Simp(f,0,1,(2**cnt)*N0)
    cnt += 1
    new = Simp(f,0,1,(2**cnt)*N0)
    reldiff = (old-new)/old
print cnt
plt.close()
plt.figure(1)
for i in range(500,5000,10):
    Trap(f,0,1,i)
    Simp(f,0,1,i)
plt.semilogx()
plt.xlabel('number of subintervals, N')
plt.ylabel('Error')
plt.title('Global Error Comparison')
plt.savefig('globalerrorcomparison.pdf')
plt.close()
plt.figure(2)
for i in range(500,3000,10):
    Simp(f,0,1,i)
plt.semilogx()
plt.xlabel('number of subintervals, N')
plt.ylabel('Error')
plt.title('Global Error Comparison')
plt.savefig('globalerrorcomparison2.pdf')
plt.close()
