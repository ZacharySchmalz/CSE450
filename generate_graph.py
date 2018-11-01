import os
import random
from graphviz import Digraph

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

MIN_PER_RANK = 10
MAX_PER_RANK = 50
MIN_RANKS = 30
MAX_RANKS = 50
PERCENT = 30
RAND_MAX = 32767
EDGE_WEIGHTS = 10
RENDER_GRAPH = False

random.seed()

def GenerateGraph() :
    i = j = k = nodes = 0
    edges = []
    ranks = MIN_RANKS + (random.randint(0,RAND_MAX) % (MAX_RANKS - MIN_RANKS + 1))

    for i in range(0, ranks) :
        new_nodes = MIN_PER_RANK + (random.randint(0, RAND_MAX) % (MAX_PER_RANK - MIN_PER_RANK + 1))
        for j in range(0, nodes) :
            for k in range(0, new_nodes) :
                if random.randint(0, RAND_MAX) % 100 < PERCENT :
                    edges.append((j, k + nodes))
                    
        nodes += new_nodes
    
    # Render the graph using graphviz software
    if RENDER_GRAPH :
        dot = Digraph()
        for x in range(0, new_nodes) :
            dot.node(str(x), str(x))
        for edge in edges :
            dot.edge(str(edge[0]), str(edge[1]))
        dot.render('out.gv', view=True)
        
    return nodes, edges
    
def WriteToFile(edges) :
    file = open('graph.csv', 'w')
    for edge in edges :
        file.write(str(edge[0]) + ',' + str(edge[1]) + ',' + str(random.randint(-EDGE_WEIGHTS, EDGE_WEIGHTS)) + '\n')
    file.close()
    
nodes, edges = GenerateGraph()
WriteToFile(edges)