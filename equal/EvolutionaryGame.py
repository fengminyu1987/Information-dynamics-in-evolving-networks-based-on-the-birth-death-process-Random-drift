# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:50:58 2022

@author: 86150
"""
import random
import networkx as nx
import numpy as np
import json
#参数列
#更新规则
#update='absorption'
update='expansion'
#update='imitation'
#update='pairwise_comparison'
#博弈参数
B=np.arange(1,10,0.5)
c=1
#网络参数
lam=5
mu=0.01
m=5
n0=30
#模拟参数
avg=1000
#函数列
def payoff(i,G,pom,strategy):
    neis=G.neighbors(i)
    result=0
    for nei in neis:
        result+=pom[strategy[i]][strategy[nei]]
    return result
def fitness(i,G,pom,strategy):
    delta=0.01
    return 1-delta+delta*payoff(i,G,pom,strategy)
def absorption(node,G,pom,strategy):
    neis=list(G.neighbors(node))
    fa=0
    fb=0
    f=0
    for i in neis:
        if strategy[i]==0:
            fa+=fitness(i,G,pom,strategy)
        if strategy[i]==1:
            fb+=fitness(i,G,pom,strategy)
        f+=fitness(i,G,pom,strategy)
    probaa=fa/f
    if probaa>=random.uniform(0,1):
        return 0
    else:
        return 1
def expansion(node,G,pom,strategy):
    neis=list(G.neighbors(node))
    neisfitness=[]
    for nei in neis:
        neisfitness.append(1/fitness(nei,G,pom,strategy))
    sum_neis=sum(neisfitness)
    neis_fitness_proba=np.array(neisfitness)/sum_neis
    begin=0
    end=neisfitness[0]
    proba=random.uniform(0,1)
    for i in range(len(neis_fitness_proba)):
        if (begin<=proba<=end):
            selector=neis[i]
            break
        else:
            begin+=neis_fitness_proba[i]
            if (i!=(len(neis_fitness_proba)-1)):
                end+=neis_fitness_proba[i+1]
    stra=strategy[selector]
    return stra
def imitation(node,G,pom,strategy):
    neis=list(G.neighbors(node))
    imitator=random.choice(neis)
    proba=fitness(imitator,G,pom,strategy)/(fitness(imitator,G,pom,strategy)+fitness(i,G,pom,strategy))
    if (random.random()<proba):
        stra=strategy[imitator]
    else:
        stra=strategy[i]
    return stra
def pairwise_comparison(i,G,pom,strategy):
    neis=list(G.neighbors(i))
    j=random.choice(neis)
    delta=0.01
    proba=1/(1+delta*np.exp(payoff(i,G,pom,strategy)-payoff(j,G,pom,strategy)))
    if (random.random()<proba):
        stra=strategy[j]
    else:
        stra=strategy[i]
    return stra
#主程序列
Crs={}
for b in B:
    Nd=0
    Nc=0
    R=b-c
    S=-c
    T=b
    P=0
    pom=[[R,S],[T,P]]
    for avg_ in range(avg):
        G=nx.complete_graph(n0)
        tnow=0
        strategy={}
        next_death={}
        for i in G.nodes:
            if int(i)%2==0:
                strategy[i]=0
            else:
                strategy[i]=1
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
                new_stra=strategy[random.choice(list(G.nodes))]
                if nodes==[]:
                    nodename=len(G.nodes)
                else:
                    nodename=nodes[0]
                    nodes.pop(0)
                for i in connect:
                    G.add_edge(nodename,i)
                strategy[nodename]=new_stra
                if update=='absorption':
                    new_strategy=absorption(nodename, G, pom, strategy)
                    strategy[nodename]=new_strategy
                if update=='expansion':
                    strategy[nodename]=expansion(nodename, G, pom, strategy)
                if update=='imitation':
                    strategy[nodename]=imitation(nodename, G, pom, strategy)
                if update=='pairwise_comparison':
                    strategy[nodename]=pairwise_comparison(nodename, G, pom, strategy)
                next_death[nodename]=(tnow+random.expovariate(mu))
            if death<birth:
                tnow=death
                nodes.append(death_node)
                G.remove_node(death_node)
                strategy.pop(death_node)
                next_death.pop(death_node)
            if birth<death:
                next_birth+=random.expovariate(lam)
            fc=1-sum(strategy.values())/len(G.nodes)
            if fc==0:
                Nd+=1
                break
            if fc==1:
                Nc+=1
                break
            print("\r b: {:.2f}, avg: {:d}, fc: {:.2f}, t: {:.2f}, N: {:d}".format(b,avg_,fc,tnow,len(G.nodes)),end="   ")
    Crs['{:.2f}'.format(b)]=Nc/avg
json_str=json.dumps(Crs)
with open('.\\saves\\{}_{:.2f}_{:.2f}_{:d}.json'.format(update,lam,mu,m), 'w') as json_file:
    json_file.write(json_str)