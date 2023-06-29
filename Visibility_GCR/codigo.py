import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from visibility_graph import visibility_graph
import networkx as nx
import sys

archivo = sys.argv[1]
data=np.loadtxt(archivo)
g = visibility_graph(data)
nx.write_edgelist(g, archivo+"_vis_results")