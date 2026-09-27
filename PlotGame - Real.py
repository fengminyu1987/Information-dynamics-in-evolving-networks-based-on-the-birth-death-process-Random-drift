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
Ms=[4,6,8,10]
plt.figure(figsize=(10,8))
cs=['blue','red','green','black']
B=np.arange(1,20,1)
for m in Ms:
    f=open(".\\saves_real\\game_bn-mouse_visual-cortex_1_{:d}.json".format(m))
    data=json.load(f)
    rho=data.values()
    plt.scatter(B,rho,c=cs[Ms.index(m)],s=150,marker='^',label='$m = {:d}$'.format(m))
plt.xlim([1, 20])
plt.ylim([-0.03,0.65])
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('$b$',font)
plt.ylabel('$\\rho_{C}(1)$',font)
plt.legend(fontsize=20)
plt.grid()
plt.savefig('.\\saves_real\\fig10(a).pdf',bbox_inches='tight',dpi=500)
plt.show()