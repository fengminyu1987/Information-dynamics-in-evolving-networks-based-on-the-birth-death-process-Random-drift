# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:38:35 2022

@author: 86150
"""
import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 20}
plt.rc('font', **font)
#网络参数
lam=5
LAM=[2,3,4,5]
mu=0.01
m=5
n0=30
cs=['red','blue','green','purple']
plt.figure(figsize=(10,8))
for lam in LAM:
    #主程序
    tnows=[]
    ns=[]
    G=nx.complete_graph(n0)
    tnow=0
    next_death={}
    for i in G.nodes:
        next_death[i]=random.expovariate(mu)
    next_birth=random.expovariate(lam)
    nodes=[]
    while True:
        death_node=min(next_death.items(),key=lambda x: x[1])[0]
        birth=next_birth
        death=next_death[death_node]
        if birth<death:
            tnow=birth
            connect=random.sample(list(G.nodes),m)
            if nodes==[]:
                nodename=len(G.nodes)
            else:
                nodename=nodes[0]
                nodes.pop(0)
            for i in connect:
                G.add_edge(nodename,i)
            next_death[nodename]=(tnow+random.expovariate(mu))
        if death<birth:
            tnow=death
            nodes.append(death_node)
            G.remove_node(death_node)
            next_death.pop(death_node)
        if birth<death:
            next_birth+=random.expovariate(lam)
        if tnow>=10000:
            break
        tnows.append(tnow)
        ns.append(len(G.nodes))
    plt.plot(tnows,ns,color=cs[LAM.index(lam)],lw=2,label='$\lambda={:d}$'.format(lam))
    print("E[N]=",np.mean(ns[-2000:]))
for lam in LAM:
    plt.plot([0,10000],[lam/mu,lam/mu],linestyle='--',color=cs[LAM.index(lam)])
plt.ylim([0,600])
plt.xlabel("$t$",font)
plt.ylabel("$N(t)$",font)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(fontsize=25)
plt.xscale("log")
plt.grid()
plt.savefig(".\\saves\\fig4(a).pdf",dpi=500,bbox_inches='tight')
plt.show()