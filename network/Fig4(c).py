# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:38:35 2022

@author: 86150
"""
import networkx as nx
import random
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
        if tnow>=1000:
            ns.append(len(G.nodes))
    counter={}
    for i in ns:
        if i not in counter.keys():
            counter[i]=1
        else:
            counter[i]+=1
    for i in counter.keys():
        counter[i]/=len(ns)
    for i in counter.keys():
        plt.scatter(i,counter[i],s=110,marker='s',color='white',edgecolors=cs[LAM.index(lam)])
    for i in counter.keys():
        plt.scatter(i,counter[i],s=110,marker='s',color='white',edgecolors=cs[LAM.index(lam)],label='$\lambda={:d}$'.format(lam))
        break
for lam in LAM:
    plt.plot([lam/mu,lam/mu],[0,0.03],color=cs[LAM.index(lam)],lw=2.5,linestyle='--')
plt.xlabel("$N$",font)
plt.ylabel("$P_N$",font)
plt.xlim([140,610])
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(fontsize=20)
plt.grid()
plt.savefig(".\\saves\\fig4(c).pdf",dpi=500,bbox_inches='tight')
plt.show()