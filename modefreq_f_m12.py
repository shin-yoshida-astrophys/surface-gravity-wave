#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:59:56 2026

@author: yoshida
fixing alpha=0.9, compare \tilde{f} dependence of \sigma/m
"""

from matplotlib import pyplot as plt
import pandas as pd

dat1 = pd.read_csv('eigen_m1_n0_alp0.9.txt', skiprows=2, \
                   header=None, delim_whitespace=True)
dat2 = pd.read_csv('eigen_m1_n1_alp0.9.txt', skiprows=2, \
                   header=None, delim_whitespace=True)
dat3 = pd.read_csv('eigen_m1_n2_alp0.9.txt', skiprows=2, \
                   header=None, delim_whitespace=True)
dat4 = pd.read_csv('eigen_m2_n0_alp0.9.txt', skiprows=2, \
                   header=None, delim_whitespace=True)
dat5 = pd.read_csv('eigen_m2_n1_alp0.9.txt', skiprows=2, \
                   header=None, delim_whitespace=True)
dat6 = pd.read_csv('eigen_m2_n2_alp0.9.txt', skiprows=2, \
                   header=None, delim_whitespace=True)
    
plt.plot(dat1[3], dat1[1], label='n=0', color='blue', lw=3)
plt.plot(dat2[3], dat2[1], label='n=1', color='red', lw=3, ls=':')
plt.plot(dat3[3], dat3[1], label='n=2', color='black', lw=3, ls='--')
plt.plot(dat4[3], dat4[1]/2, linestyle='-', color='blue')
plt.plot(dat5[3], dat5[1]/2, linestyle=':', color='red', lw=2)
plt.plot(dat6[3], dat6[1]/2, linestyle='--', color='black')
#
plt.xlabel(r'$\tilde{f} $', fontsize=18)
plt.ylabel(r'$\tilde{\sigma} / m$', fontsize=18)
plt.xscale('log')
#plt.grid()
plt.legend()
plt.savefig('eigen_f-dependence-m12.eps', bbox_inches='tight')
plt.show()

