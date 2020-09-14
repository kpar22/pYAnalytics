# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:29:21 2020

@author: kshitij
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import random

global infected_list
global recovered_list
global not_infected_list

def algo(G,p):
    for i in G.nodes():
        for j in G.nodes():
            if i!=j:
                r=random.random()
                if r<=p:
                    
                    ne = [(i,j)]
                #else:
                    #ne =[(i,j)]
                    #continue

def display_graph(G,pos):
    nodes_g = nx.draw_networkx_nodes(G,pos,node_color='red', nodelist=infected_list)
    nodes_g = nx.draw_networkx_nodes(G,pos,node_color='green', nodelist=recovered_list)
    nodes_g = nx.draw_networkx_nodes(G,pos,node_color='grey', nodelist=not_infected_list)
   

def main():
    
    df = pd.read_csv('SNA.txt', delim_whitespace = True, header = None, names =['n1', 'n2', 'distance','value']) 
    G = nx.from_pandas_edgelist(df, 'n1', 'n2', create_using= nx.MultiDiGraph(), edge_attr =['distance','value']) 
    state = dict((i, 1 ) for i in G.nodes())
    state[4]=0
    pos=nx.circular_layout(G)

    nx.set_node_attributes(G,state,'state')
    print(state)
    print(list(G.edges(data = True))) 
    print(state.values())

    infected_list = [n for (n,d) in G.nodes(data = True) if d['state'] == 0]
    recovered_list = [n for (n,d) in G.nodes(data=True) if d['state'] == 1]
    not_infected_list = [n for (n,d) in G.nodes(data = True) if d['state'] == 2]
    
    #economic = [(u, v) for (u, v, d) in G.edges(data=True) if d["distance"] = 1]
    family = [(u, v) for (u, v, d) in G.edges(data=True) if d["distance"] >= 0.8]
    print(family)
    print(infected_list)
    
    display_graph(G,pos)
    
    nx.draw_networkx_edges(G,pos, edge_attr='distance' , edge_color='black')
    nx.draw_networkx_edges(G,pos, edgelist=family, edge_attr='distance' , edge_color='blue')
    plt.show()
    plt.figure()

main()
    




