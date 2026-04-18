#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:48:12 2026

@author: yoshida
comparing fundamental mode for different m
"""

from matplotlib import pyplot as plt
import pandas as pd

dat1 = pd.read_csv('eigenf_f8.07E-02_m1_alp9.00E-01_n0.csv', skiprows=0, \
                   header=None)
dat2 = pd.read_csv('eigenf_f8.07E-02_m2_alp9.00E-01_n0.csv', skiprows=0, \
                   header=None)
dat3 = pd.read_csv('eigenf_f8.07E-02_m3_alp9.00E-01_n0.csv', skiprows=0, \
                   header=None)


plt.plot(dat1[0], dat1[1]/2, label='m=1', lw=3, ls='-')
plt.plot(dat2[0], dat2[1]*1.4, label='m=2', lw=4, ls=':')
plt.plot(dat3[0], dat3[1]*4, label='m=3', lw=3, ls='--')
plt.legend()
plt.xlabel(r'$r/r_s$', fontsize=18)
plt.ylabel(r'$\eta$', fontsize=18)
plt.xlim(0, 1)
plt.grid()
plt.savefig('eigenfunc-n0-m123.eps', bbox_inches='tight')