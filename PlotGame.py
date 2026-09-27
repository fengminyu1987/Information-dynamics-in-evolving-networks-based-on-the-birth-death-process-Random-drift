# -*- coding: utf-8 -*-
"""
Created on Fri May 13 19:30:37 2022

@author: 86150
"""
mode='game'
import json
import numpy as np
import matplotlib.pyplot as plt
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 20}
plt.rc('font', **font)
LAM=[2,3,4,5]
invader=0
mu=0.01
m=4
plt.figure(figsize=(10,8))
update='absorption'
cs=['blue','red','green','black']
B=np.arange(2,20,1)
for lam in LAM:
    N=lam/mu
    f=open(".\\saves\\{}_{}_{:.2f}_{:.2f}_{:d}.json".format(invader,update,lam,mu,m))
    data=json.load(f)
    rho=data.values()
    plt.scatter(B,rho,c=cs[LAM.index(lam)],s=150,marker='^',label='$\lambda = {:.2f}$'.format(lam))
    plt.axvline((N-2)/((N/m)-2), c=cs[LAM.index(lam)], alpha=1, linestyle='-.',lw=3)
plt.xlim([1, 20])
plt.ylim([-0.03,0.53])
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('$b$',font)
plt.ylabel('$\\rho_{C}(1)$',font)
plt.legend(fontsize=20)
plt.grid()
#plt.savefig('.\\imgs\\fpns_{:d}.pdf'.format(m),bbox_inches='tight',dpi=500)
if m==4:
    plt.savefig('.\\imgs\\fig9(a).pdf',bbox_inches='tight',dpi=500)
if m==6:
    plt.savefig('.\\imgs\\fig9(b).pdf',bbox_inches='tight',dpi=500)
if m==8:
    plt.savefig('.\\imgs\\fig9(c).pdf',bbox_inches='tight',dpi=500)
plt.show()