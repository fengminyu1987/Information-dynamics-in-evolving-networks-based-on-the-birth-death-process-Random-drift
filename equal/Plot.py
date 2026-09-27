# -*- coding: utf-8 -*-
"""
Created on Fri May 13 19:30:37 2022

@author: 86150
"""
mode='spread'
import json
import numpy as np
import matplotlib.pyplot as plt
lam=5
mu=0.01
m=5
plt.figure(figsize=(8,6))
mode='game'
update='expansion'
if mode=='spread':
    f=open(".\\saves\\{}_{:.2f}_{:.2f}_{:d}.json".format(mode,lam,mu,5))
    data=json.load(f)
    ALPHA=np.arange(0,1.01,0.02)
    rhoi=data.values()
    plt.scatter(ALPHA,rhoi,c='red',s=20,marker='s',label='$\lambda = 5, \mu = 0.01, m = 5$')
    plt.ylim([-0.1,1.1])
    plt.xlim([-0.1,1.1])
    plt.show()
if mode=='game':
    f=open(".\\saves\\{}_{:.2f}_{:.2f}_{:d}.json".format(update,lam,mu,5))
    data=json.load(f)
    B=np.arange(1,10,0.5)
    rhoc=data.values()
    plt.scatter(B,rhoc,c='white',edgecolors='blue',s=30,marker='s',label='$\lambda = 5, \mu = 0.01, m = 5$')
    plt.show()