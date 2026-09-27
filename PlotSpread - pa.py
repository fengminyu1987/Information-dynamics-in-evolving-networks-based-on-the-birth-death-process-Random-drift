# -*- coding: utf-8 -*-
"""
Created on Fri May 13 19:30:37 2022

@author: 86150
"""
mode='spread'
import json
import numpy as np
import matplotlib.pyplot as plt
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 20}
plt.rc('font', **font)
LAM=[2,3,4,5]
mu=0.01
m=8
plt.figure(figsize=(10,8))
mode='spread'
cs=['blue','red','green','black']
for lam in LAM:
    f=open(".\\saves\\pa\\{}_{:.2f}_{:.2f}_{:d}_pa.json".format(mode,lam,mu,m))
    data=json.load(f)
    ALPHA=np.arange(0,1.01,0.02)
    rhoi=data.values()
    #plt.scatter(ALPHA,rhoi,c='white',edgecolors=cs[LAM.index(lam)],s=60,marker='s',label='$\lambda = {:.2f}$'.format(lam))
    plt.scatter(ALPHA,rhoi,c=cs[LAM.index(lam)],s=150,marker='^',label='$\lambda = {:.2f}$'.format(lam))
plt.ylim([-0.03,1.03])
#plt.xlim([-0.1,1.1])
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xscale('log')
plt.xlabel('$\\alpha$',font)
plt.ylabel('$\\rho_{A}(1)$',font)
plt.legend(fontsize=20)
plt.grid()
if m==4:
    plt.savefig('.\\imgs\\fig7(d).pdf',bbox_inches='tight',dpi=500)
if m==6:
    plt.savefig('.\\imgs\\fig7(e).pdf',bbox_inches='tight',dpi=500)
if m==8:
    plt.savefig('.\\imgs\\fig7(f).pdf',bbox_inches='tight',dpi=500)
plt.show()