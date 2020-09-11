# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:33:54 2020

@author: kshitij
"""


import networkx as nx
#pip install EoN
#import EoN
import matplotlib.pyplot as plt
import random

def display_graph(G,i,ne):
    pos=nx.circular_layout(G)
    if i == '' and ne == '':
        new_node = []
        rest_nodes =G.nodes()
        new_edges = []
        rest_edges = G.edges()
        #plt.show()
    elif i== '' :
        #new_node = [i]
        #rest_nodes = list(set(G.nodes)-set(new_node))
        rest_nodes =G.nodes()
        new_edges = ne
        rest_edges = list(set(G.edges)-set(new_edges) - set([(b,a) for (a,b) in new_edges]))
        #nx.draw_networkx_nodes(G,pos, nodelist = new_nodes, node_color='red')
        nx.draw_networkx_nodes(G,pos, nodelist = rest_nodes, node_color='red')
        nx.draw_networkx_edges(G,pos, edgelist = new_edges, edge_color='blue', style='dashed')
        nx.draw_networkx_edges(G,pos, edgelist = rest_edges, edge_color='black')
        plt.show()

def algo(G,p):
    for i in G.nodes():
        for j in G.nodes():
            if i!=j:
                r=random.random()
                if r<=p:
                    G.add_edge(i,j)
                    ne = [(i,j)]
                    display_graph(G,'',ne)
                else:
                    ne =[(i,j)]
                    display_graph(G,'',ne)
                    continue
    

def main():
    N = 3
    p = 0.6
    G = nx.Graph()
    G.add_nodes_from([i for i in range(N)])
    display_graph(G,'','')
    algo(G,p)
    
main()

#N = 10**2 #number of individuals
#k = 5 #expected number of partners

#print("generating graph G with {} nodes".format(N))

#G = nx.gnp_random_graph(N, k/(N-1)) 

#print(F.nodes())
#print(F.edges())
#nx.draw_networkx_edges(G)
#display_graph(F)