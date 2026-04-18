#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:34:28 2026

@author: yoshida
"""
from matplotlib import pyplot as plt
import numpy as np

# [Prot(s), nuQPO1(mHz), nuQPO2(mHz), object]



obsdata = [[4.8, 33, 43, 'Cen X-3'],\
           [1.24, 5, 10, 'Her X-1'],
           [12.5, 30, 114, 'IGR J19294+1816'],
           [3.6, 1, 62.5, '4U 0115+63'],
           [18.7, 21.5, 21.5, 'KS 1947+300'],
           [358, 44, 44, 'SAX J2103.5+4545'],
           [104, 30, 70, '1A 0535+262'],
           [4.39, 51, 51, 'V 0332+53'],
           [222, 196, 196, 'XTE H1858+034'],
           [31, 1266, 1266, 'XTE J10111.2-7317'],
           [205, 200, 500, 'RX J0440.9+4431'],
           [2.76, 135, 135, '4U 1901+03'],
           [0.72, 10, 10, 'SMC X-1']]

#--------------------------------------------------
s01x=[4.8, 4.8]
s01y=[33, 43]
#
s02x=[1.24, 1.24]
s02y1=[5, 9]
s02y2=[10, 10]
#
s03x=[12.5, 12.5]
s03y1=[30, 30]
s03y2=[51, 51]
s03y3=[114, 114]
#
s04x=[3.6, 3.6]
s04y1=[1,1]
s04y2=[2,2]
s04y3=[5, 14.9]
s04y4=[31,62.5]
#
s05x=[18.7,18.7]
s05y=[21.5, 21.5]
#
s06x=[358, 358]
s06y=[44,44]
#
s07x=[104,104]
s07y=[30,70]
#
s08x=[4.39,4.39]
s08y=[51,51]
#
s09x=[222,222]
s09y=[196,196]
#
s10x=[31,31]
s10y=[1266,1266]
#
s11x=[205,205]
s11y=[200, 500]
#
s12x=[2.76,2.76]
s12y=[135,135]
#
s13x=[0.72,0.72]
s13y=[10,10]
#--------------------------------------------------
    
 
theory = [[0.001780950379228081, 19.3726927297152],
[0.006894001407553381, 74.99106795943159],
[0.0006838849460342137, 7.439114012773846],
[0.0023746005043915074, 25.83025695910628],
[0.00045714234363381374, 4.972669794946646],
[2.387866431955124e-05, 0.25974560103482786],
[8.219770986908127e-05, 0.8941242804836828],
[0.0019472805966186898, 21.181987492022177],
[3.850703525404082e-05, 0.4188690322992929],
[0.0002757600589106897, 2.9996427473742773],
[4.1700301592177715e-05, 0.4536045130265171],
[0.0030973050031869293, 33.691639483633665],
[0.01187300222015243, 129.1512814400047]]
# [nu(B=1e12), nu(B=1e14)] for hout=100m
#    alpha(B=1e13)=0.9982142857142857, alpha(B=1e14)=0.8214285714285714

#theory = [[0.17823439563851692, 19.3726927297152],
#[0.6899395899476165, 74.99106795943159],
#[0.06844200796645608, 7.439114012773846],
#[0.23764586072614788, 25.83025695910628],
#[0.045750005327990596, 4.972669794946646],
#[0.002389734915302646, 0.25974560103482786],
#[0.008226202881508184, 0.8941242804836828],
#[0.194880432562743, 21.181987492022177],
#[0.003853716665216748, 0.4188690322992929],
#[0.027597583860047365, 2.9996427473742773],
#[0.004173293169161241, 0.4536045130265171],
#[0.30997286156134857, 33.691639483633665],
#[1.188229273301246, 129.1512814400047]]
## [nu(B=1e13), nu(B=1e14)] for hout=100m
##    alpha(B=1e13)=0.9982142857142857, alpha(B=1e14)=0.8214285714285714


x = []
yobs = []
ytheo = []
yobs_range_low = []
yobs_range_high = []
ytheo_low = []
ytheo_high = []
annot = [] # for annotation
annot2 = []
for i in range(13):
    x.append(obsdata[i][0])
    yobs.append(np.sqrt(obsdata[i][1] * obsdata[i][2]))
#    ytheo.append(0.5*(theory[i][0] + theory[i][1]))
    ytheo.append(np.sqrt(theory[i][0] * theory[i][1]))
    yobs_range_low.append(obsdata[i][1])
    yobs_range_high.append(obsdata[i][2])
    ytheo_low.append(theory[i][0])
    ytheo_high.append(theory[i][1])
    annot.append(obsdata[i][3])
    annot2.append('['+str(i+1)+']')
#    annot.append(i)
#    yobs_range.append([obsdata[i][1], obsdata[i][2]])
#    ytheo.append([theory[i][0], theory[i][1]])

yobs_range_low = np.array(yobs) - np.array(yobs_range_low)
yobs_range_high = np.array(yobs_range_high) - np.array(yobs)
ytheo_low = np.array(ytheo) - np.array(ytheo_low)
ytheo_high = np.array(ytheo_high) - np.array(ytheo)
##


yobs_range = [yobs_range_low, yobs_range_high]
ytheo_range = [ytheo_low, ytheo_high]
#plt.errorbar(x, yobs, yerr=yobs_range, fmt='og', color='blue')
####
plt.errorbar(x, ytheo, yerr=ytheo_range, fmt='none', color='red', elinewidth=2, ls=':')
####
plt.plot(s01x, s01y, color='blue', linewidth=4)
plt.plot(s02x, s02y1, color='blue', linewidth=4)
plt.scatter(s02x, s02y2, color='blue', s=18)
plt.scatter(s03x, s03y1, color='blue', s=18)
plt.scatter(s03x, s03y2, color='blue', s=18)
plt.scatter(s03x, s03y3, color='blue', s=18)
plt.scatter(s04x, s04y1, color='blue', s=18)
plt.scatter(s04x, s04y2, color='blue', s=18)
plt.plot(s04x, s04y3, color='blue', linewidth=4)
plt.plot(s04x, s04y4, color='blue', linewidth=4)
plt.scatter(s05x, s05y, color='blue', s=18)
plt.scatter(s06x, s06y, color='blue', s=18)
plt.scatter(s07x, s07y, color='blue', s=18)
plt.scatter(s08x, s08y, color='blue', s=18)
plt.scatter(s09x, s09y, color='blue', s=18)
plt.scatter(s10x, s10y, color='blue', s=18)
plt.scatter(s11x, s11y, color='blue', s=18)
plt.scatter(s12x, s12y, color='blue', s=18)
plt.scatter(s13x, s13y, color='blue', s=18)

#for i, label in enumerate(annot):
#    plt.text(x[i]*1.1, yobs[i], annot2[i], fontsize=11, rotation=90)

plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$P_{rot}$ (s)', fontsize=18)
plt.ylabel(r'$\nu$ (mHz)', fontsize=18)
plt.grid()
plt.savefig('HMXB_mHz_QPOs_no_annotations.eps', bbox_inches='tight')
plt.show()
