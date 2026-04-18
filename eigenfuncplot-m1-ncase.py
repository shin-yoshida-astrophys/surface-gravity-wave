#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:09:36 2026

@author: yoshida
eigenfunction plot for m=1 modes with different n
"""

from matplotlib import pyplot as plt
import pandas as pd

dat1 = pd.read_csv('eigenf_f8.07E-02_m1_alp9.00E-01_n0.csv', skiprows=0, \
                   header=None)
dat2 = pd.read_csv('eigenf_f8.07E-02_m1_alp9.00E-01_n1.csv', skiprows=0, \
                   header=None)
dat3 = pd.read_csv('eigenf_f8.07E-02_m1_alp9.00E-01_n2.csv', skiprows=0, \
                   header=None)
dat4 = pd.read_csv('eigenf_f8.07E-02_m1_alp9.00E-01_n3.csv', skiprows=0, \
                   header=None)

plt.plot(dat1[0], dat1[1]/2, label='n=0', lw=2, ls='-')
plt.plot(dat2[0], dat2[1], label='n=1', lw=3, ls=':')
plt.plot(dat3[0], dat3[1], label='n=2', lw=2, ls='-.')
plt.plot(dat4[0], dat4[1], label='n=3', lw=2, ls='--')
plt.legend()
plt.xlabel(r'$r/r_s$', fontsize=18)
plt.ylabel(r'$\eta$', fontsize=18)
plt.xlim(0, 1)
plt.grid()
plt.savefig('eigenfunc-m1.eps', bbox_inches='tight')
