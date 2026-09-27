# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:38:35 2022

@author: 86150
"""
import networkx as nx
import numpy as np
import random
import json
#传播参数
ALPHA=np.arange(0,1.01,0.02)
#网络参数
lam=10
mu=0.01
m=4
n0=30
#模拟参数
avg=1000
#主程序列
Irs={}
for alpha in ALPHA:
    Ni=0
    Ns=0
    for avg_ in range(avg):
        G=nx.complete_graph(n0)
        tnow=0
        state={}#0代表S，1代表I
        next_death={}
        for i in G.nodes:
            state[i]=0
            next_death[i]=random.expovariate(mu)
        state[random.choice(list(G.nodes))]=1
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
                next_death[nodename]=(tnow+random.expovariate(mu))
                state[nodename]=0
                for node in connect:
                    if state[node]==1:
                        if random.uniform(0,1)<alpha:
                            state[nodename]=1
                            break
                for i in connect:
                    G.add_edge(nodename,i)
            if death<birth:
                tnow=death
                nodes.append(death_node)
                G.remove_node(death_node)
                state.pop(death_node)
                next_death.pop(death_node)
            if birth<death:
                next_birth+=random.expovariate(lam)
            fi=sum(state.values())/len(G.nodes)
            if fi==0:
                Ns+=1
                break
            if fi==1:
                Ni+=1
                break
            print("\r {}: {:.2f}, avg: {:d}, fc: {:.2f}, t: {:.2f}, N: {:d}".format(chr(945),alpha,avg_,fi,tnow,len(G.nodes)),end="   ")
    Irs['{:.2f}'.format(alpha)]=Ni/avg
json_str=json.dumps(Irs)
with open('.\\saves\\spread_{:.2f}_{:.2f}_{:d}.json'.format(lam,mu,m), 'w') as json_file:
    json_file.write(json_str)