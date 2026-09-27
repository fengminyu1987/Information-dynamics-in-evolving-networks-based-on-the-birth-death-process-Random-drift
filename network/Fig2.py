# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:38:35 2022

@author: 86150
"""
import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
def ddf(G):
    degree=nx.degree_histogram(G)
    x=range(len(degree))
    y=[z/float(sum(degree)) for z in degree]
    return x,y
def k_mean(G):
    result=0
    for i in G.nodes:
        result+=G.degree(i)
    return result/G.number_of_nodes()
def degreetheo(xx,m):
    result=[]
    for k in xx:
        result.append(np.power(m,k)*np.exp(-m)/np.math.factorial(k))
    return result
def degreecount(l):
    result={}
    for i in l:
        if i not in result.keys():
            result[i]=1
        else:
            result[i]+=1
    sum_=sum(result.values())
    for i in result.keys():
        result[i]/=sum_
    return result
#网络参数
lam=5
mu=0.01
m=10
n0=30
#模拟参数
#主程序
G=nx.complete_graph(n0)
tnow=0
next_death={}
for i in G.nodes:
    next_death[i]=random.expovariate(mu)
next_birth=random.expovariate(lam)
nodes=[]
meandegree=[]
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
    if tnow>=400:
        meandegree.append(k_mean(G))
    if tnow>=2000:
        break
print(np.mean(meandegree))
plt.figure(figsize=(8,8))
x=range(0,20)
y=degreetheo(x,m)
plt.scatter(x,y,color='red',label='Theoretical')
x,y=ddf(G)
plt.scatter(x,y,color='white',edgecolors='blue',linewidths=2,label='Statistical')
plt.legend(fontsize=20)
plt.show()