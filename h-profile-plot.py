#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:43:01 2026

@author: yoshida
h-profile
"""

from matplotlib import pyplot as plt
import numpy as np

######### background h
### this profile has zero gradient at both r=0 and r=1
### The profile is normalized by h0, but the argument
### of it, 'r', is normalized by r0.
h0 = 1 # normalized by the average depth
#alpha = 0.9

def h(x, alpha):
    a0 = 6*(1-alpha)*h0
    y = a0*(x**2/2 - x**3/3) + alpha*h0
    return y
## x = r/r0

x = np.linspace(0, 1, 100)
y1 = h(x, 0.1)
y2 = h(x, 0.5)
y3 = h(x, 0.99)

plt.plot(x, y1, label=r'$\alpha = 0.1$', lw=3, ls='-')
plt.plot(x, y2, label=r'$\alpha = 0.5$', lw=4, ls=':')
plt.plot(x, y3, label=r'$\alpha = 0.99$', lw=3, ls='--')
plt.xlabel(r'$r/r_s$', fontsize=18)
plt.ylabel(r'$\bar{h}/h_{out}$', fontsize=18)
plt.xlim(0, 1)
plt.legend()
plt.savefig('h-profile.eps', bbox_inches='tight')
plt.show()
