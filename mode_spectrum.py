#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 16:24:01 2026

@author: yoshida
Plotting the pattern speed as a function of mode number
\tilde{\sigma} = \sigma / (f/2) ; f=2\Omega\cos\theta
"""

from matplotlib import pyplot as plt
import pandas as pd

dat1 = pd.read_csv('freq_m1_alp0.98_gam10_f0.08.txt', skiprows=3, \
                   header=None, delim_whitespace=True)
dat2 = pd.read_csv('freq_m2_alp0.98_gam10_f0.08.txt', skiprows=3, \
                   header=None, delim_whitespace=True)
dat3 = pd.read_csv('freq_m3_alp0.98_gam10_f0.08.txt', skiprows=3, \
                   header=None, delim_whitespace=True)

plt.scatter(dat1[0], dat1[1], marker='o', label='m=1', s=100)
plt.scatter(dat2[0], dat2[1]/2, marker='x', label='m=2', s=100)
plt.scatter(dat3[0], dat3[1]/3, marker='+', label='m=3', s=120)
plt.xlabel('n', fontsize=18)
plt.ylabel(r'$\tilde{\sigma} / m$', fontsize=18)
plt.yscale('log')
#plt.grid()
plt.legend()
plt.savefig('eigen_spectrum.eps', bbox_inches='tight')
plt.show()
