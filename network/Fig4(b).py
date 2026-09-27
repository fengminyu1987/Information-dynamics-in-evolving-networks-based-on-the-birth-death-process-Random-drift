# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:38:35 2022

@author: 86150
"""
import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
import json
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 20}
plt.rc('font', **font)
#网络参数
lam=5
LAM=[2,3,4,5]
mu=0.01
MU=np.arange(0.005,0.021,0.001)
m=5
n0=30
cs=['red','blue','green','purple']
#Simulation
'''
RS={}
for lam in LAM:
    rs=[]
    for mu in MU:
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
            if tnow>=7000:
                ns.append(len(G.nodes))
        rs.append(np.mean(ns))
        print("\r {}: {:.2f}, {}: {:.3f}".format(chr(955),lam,chr(956),mu),end='       ')
    RS["{:d}".format(lam)]=rs
json_str=json.dumps(RS)
with open('.\\saves\\Fig4(b).json','w') as json_file:
    json_file.write(json_str)
'''
#Fig4(b)
#Simulation
f=open(".\\saves\\Fig4(b).json")
data=json.load(f)
plt.figure(figsize=(10,8))
for lam in LAM:
    plt.scatter(MU,data["{:d}".format(lam)],color=cs[LAM.index(lam)], edgecolors='k',s=150,marker='^',label='$\lambda={:d}$'.format(lam))
#Theoretical Solution
MU=np.arange(0.005,0.021,0.0005)
for lam in LAM:
    plt.plot(MU, lam/MU,color=cs[LAM.index(lam)],linestyle='-.')
plt.xlabel("$\mu$",font)
plt.ylabel("$N$",font)
plt.xlim([0.004,0.021])
plt.ylim([0,1100])
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(fontsize=25)
plt.grid()
plt.savefig(".\\saves\\fig4(b).pdf",dpi=500,bbox_inches='tight')
plt.show()