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
def ddf_theo(xx,m):
    result=[]
    for k in xx:
        result.append(np.power(m,k)*np.exp(-m)/np.math.factorial(k))
    return result
#网络参数
lam=5
mu=0.01
m=5
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
    if tnow>=6000:
        break
xx,yy=ddf(G)
plt.figure(figsize=(8,8))
plt.scatter(xx,yy,color='white',marker='s',edgecolors='blue',s=50)
theo=ddf_theo(xx,m)
plt.scatter(xx,theo,color='red',marker='s',s=50)
print(theo)
plt.title("{:.2f}".format(k_mean(G)),fontsize=20)
plt.show()