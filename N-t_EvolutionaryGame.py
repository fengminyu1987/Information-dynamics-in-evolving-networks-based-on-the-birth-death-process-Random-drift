# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:50:58 2022

@author: 86150
"""
import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
#参数列
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 20}
plt.rc('font', **font)
#更新规则
update='absorption'
#update='expansion'
#update='imitation'
#update='pairwise_comparison'
invader=0
#博弈参数
#B=np.arange(1,20,1)
B=np.array([5,15])
c=1
#网络参数
lam=3
mu=0.01
m=4
n0=30
#模拟参数
avg=1500
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
def absorption(connect,G,pom,strategy):
    neis=connect
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
    fa=0
    fb=0
    f=0
    for i in neis:
        if strategy[i]==0:
            fa+=fitness(i,G,pom,strategy)
        if strategy[i]==1:
            fb+=fitness(i,G,pom,strategy)
        f+=fitness(i,G,pom,strategy)
    probaa=(1/fa+1/fb)/(1/f)
    if probaa>=random.uniform(0,1):
        return 0
    else:
        return 1
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
    plt.figure(figsize=(10,5))
    for avg_ in range(avg):
        nt=[]
        t=[]
        G=nx.complete_graph(n0)
        tnow=0
        strategy={}
        next_death={}
        for i in G.nodes:
            strategy[i]=abs(invader-1)
            next_death[i]=random.expovariate(mu)
        strategy[random.choice(list(G.nodes))]=invader
        next_birth=random.expovariate(lam)
        nodes=[]
        while True:
            t.append(tnow)
            nt.append(len(strategy)-sum(strategy.values()))
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
                if update=='absorption':
                    strategy[nodename]=absorption(connect, G, pom, strategy)
                if update=='expansion':
                    strategy[nodename]=expansion(nodename, G, pom, strategy)
                if update=='imitation':
                    strategy[nodename]=imitation(nodename, G, pom, strategy)
                if update=='pairwise_comparison':
                    strategy[nodename]=pairwise_comparison(nodename, G, pom, strategy)
                for i in connect:
                    G.add_edge(nodename,i)
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
                plt.plot(t,nt,color='#EB6133',alpha=0.25)
                break
            if fc==1:
                Nc+=1
                plt.plot(t,nt,color='#5C7FB3',alpha=0.25)
                break
            print("\r b: {:.2f}, avg: {:d}, fc: {:.2f}, t: {:.2f}, Nc: {:d}".format(b,avg_,fc,tnow,Nc),end="   ")
    plt.xscale("log")
    plt.xlabel("$t$",font)
    plt.ylabel("$C(t)$",font)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid()
    if b==5:
        plt.savefig('.\imgs\fig8(a).pdf',bbox_inches='tight',dpi=500)
    if b==15:
        plt.savefig('.\imgs\fig8(a).pdf',bbox_inches='tight',dpi=500)