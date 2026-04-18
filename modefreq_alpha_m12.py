#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:57:06 2026

@author: yoshida

eigenfrequency m=1 for f=0.807
fixing f compare \alpha dependence of \sigma/m
"""

from matplotlib import pyplot as plt
import pandas as pd

dat1 = pd.read_csv('eigen_m1_n0_f0.0807.txt', skiprows=2, \
                   header=None, delim_whitespace=True)
dat2 = pd.read_csv('eigen_m1_n1_f0.0807.txt', skiprows=2, \
                   header=None, delim_whitespace=True)
dat3 = pd.read_csv('eigen_m1_n2_f0.0807.txt', skiprows=2, \
                   header=None, delim_whitespace=True)
dat4 = pd.read_csv('eigen_m2_n0_f0.0807.txt', skiprows=2, \
                   header=None, delim_whitespace=True)
dat5 = pd.read_csv('eigen_m2_n1_f0.0807.txt', skiprows=2, \
                   header=None, delim_whitespace=True)
dat6 = pd.read_csv('eigen_m2_n2_f0.0807.txt', skiprows=2, \
                   header=None, delim_whitespace=True)
    
plt.plot(dat1[2], dat1[1], label='n=0', color='blue', lw=3)
plt.plot(dat2[2], dat2[1], label='n=1', color='black', lw=3, ls=':')
plt.plot(dat3[2], dat3[1], label='n=2', color='magenta', lw=3, ls='--')
plt.plot(dat4[2], dat4[1]/2, linestyle='solid', color='blue')
plt.plot(dat5[2], dat5[1]/2, linestyle=':', color='black')
plt.plot(dat6[2], dat6[1]/2, linestyle='--', color='magenta')
#
plt.xlabel(r'$\alpha $', fontsize=18)
plt.ylabel(r'$\tilde{\sigma} / m$', fontsize=18)
plt.yscale('log')
#plt.xscale('log')
#plt.grid()
plt.legend()
plt.savefig('eigen_alpha-dependence-m12.eps', bbox_inches='tight')
plt.show()

