# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:38:35 2022

@author: 86150
"""
import networkx as nx
import random
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import json
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 20}
plt.rc('font', **font)
def pa(G,m):
    degrees=dict(G.degree())
    choice_list=[]
    result=[]
    for i in degrees.keys():
        choice_list+=[i]*degrees[i]
    for j in range(m):
        temp=random.choice(choice_list)
        if temp not in result:
            result+=[temp]
        else:
            j=j-1
    return result
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
plt.figure(figsize=(10,8))
cs=['red','blue','green','purple']
lam=3
LAM=np.arange(2,5.1,0.2)
mu=0.01
m=5
M=[4,6,8,10]
n0=30
#模拟参数
RS={}
for m in M:
    rs=[]
    for lam in LAM:
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
            print("\r m: {:d}, lam: {:.2f}".format(m,lam),end='     ')
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
                '''    
                for k in range(m):
                    rand_v = random.random() * sum(j[1] for j in nx.degree(G))
                    for j in nx.degree(G):
                        rand_v = rand_v - j[1]
                        if rand_v <= 0:
                            if nodename!=j[0]:
                                G.add_edge(nodename, j[0])
                            # if j[0] in nodes_time.keys():
                            # 	nodes_time[j[0]][time_pass] = time_y(j[0])
                            break
                    # 如果连接重复,重roll
                    if G.degree(nodename) < k+1:
                        k = k - 1
                connect=list(G.neighbors(nodename))'''
                connect=pa(G,m)
                for node in connect:
                    G.add_edge(node,nodename)
                next_death[nodename]=(tnow+random.expovariate(mu))
            if death<birth:
                tnow=death
                nodes.append(death_node)
                G.remove_node(death_node)
                next_death.pop(death_node)
            if birth<death:
                next_birth+=random.expovariate(lam)
            if tnow>=30000:
                break
            if tnow>=10000:
                meandegree.append(k_mean(G))
        rs.append(np.mean(meandegree))
    RS["{:d}".format(m)]=rs
json_str=json.dumps(RS)
with open('.\\saves\\Fig5(f).json','w') as json_file:
    json_file.write(json_str)
#Fig5(c)
#Simulation
f=open(".\\saves\\Fig5(f).json")
data=json.load(f)
plt.figure(figsize=(10,8))
for m in M:
    plt.scatter(LAM,data["{:d}".format(m)],color=cs[M.index(m)], edgecolors='k',s=150,marker='^',label='$m={:d}$'.format(m))
    plt.plot([LAM[0],LAM[-1]],[m,m],color=cs[M.index(m)],linestyle="--",lw=2)
plt.grid()
plt.ylim([3,12])
plt.xlabel("$\lambda$",font)
plt.ylabel("$<k>$",font)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(fontsize=25)
plt.savefig(".\\saves\\fig5(f).pdf",dpi=500,bbox_inches='tight')
plt.show()