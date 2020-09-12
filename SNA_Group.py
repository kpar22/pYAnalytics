# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:29:21 2020

@author: kshitij
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('SNA.txt', delim_whitespace = True, header = None, names =['n1', 'n2', 'distance','value']) 
  
G = nx.from_pandas_edgelist(df, 'n1', 'n2', create_using= nx.MultiDiGraph(), edge_attr =['distance','value']) 
  
# The Graph diagram does not show the edge weights.  
# However, we can get the weights by printing all the 
# edges along with the weights by the command below 
print(list(G.edges(data = True))) 

pos=nx.circular_layout(G)
#nx.draw(G)
#nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_color=df['distance'], width=10.0, edge_cmap=plt.cm.Blues)
nx.draw(G,pos, with_labels=True, node_color='skyblue', node_size=1500)
nx.draw_networkx_edges(G,pos, edge_attr='value' , edge_color='blue', style='dashed',connectionstyle='arc3,rad=1')
nx.draw_networkx_edges(G,pos, edge_attr='distance', edge_color='black')
plt.show()
