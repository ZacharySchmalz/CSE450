from PrettyTable import prettytable as pt
import bellman_ford as bf
import bellman_ford_1 as bf1
import bellman_ford_yen1 as bfYen1
import bellman_ford_yen2 as bfYen2
import bellman_ford_random as bf_random
import generate_graph as generator
import random
import time

ALGORITHM_COUNT = 5

GRAPHS = []
TIME = []
EDGES_PROCESSED = []

class Graph :
    def __init__(self, edges, rng) :
        self.vertices = {}
        self.edges = []
        
        self.createGraph(edges, rng)
    
    def addEdge(self, source, dest, weight) :
        self.edges.append([source, dest, weight])
    
    def addVertex(self, vertex) :
        if vertex not in self.vertices :
            self.vertices[vertex] = len(self.vertices)

    def createGraph(self, edges, rng) :
        for edge in edges :
            self.addVertex(edge[0])
            self.addVertex(edge[1])
            self.addEdge(edge[0], edge[1], rng.randint(-10, 10))

def main() :
    for i in range(0, ALGORITHM_COUNT) :
        TIME.append([])
        EDGES_PROCESSED.append([])

    local_random = random.Random()
    
    for i in range(0,1) :
        #graph = Graph(generator.GenerateGraph(), local_random)
        graph = bf.Graph('patents')

        GRAPHS.append((len(graph.vertices),len(graph.edges)))
        
        start = time.time()
        #bf.BellmanFord(graph, 0)
        TIME[0].append(time.time() - start)
        EDGES_PROCESSED[0].append(i)
        
        start = time.time()
        bf1.BellmanFord(graph, 0)
        TIME[1].append(time.time() - start)
        EDGES_PROCESSED[1].append(i)
        
        start = time.time()
        bfYen1.BellmanFord(graph, 0)
        TIME[2].append(time.time() - start)
        EDGES_PROCESSED[2].append(i)
        
        start = time.time()
        bfYen2.BellmanFord(graph, 0)
        TIME[3].append(time.time() - start)
        EDGES_PROCESSED[3].append(i)
        
        start = time.time()
        bf_random.BellmanFord(graph, 0)
        TIME[4].append(time.time() - start)
        EDGES_PROCESSED[4].append(i)
    
    table = pt.PrettyTable(['Algorithm', 'Graph Vertices', 'Graph Edges', 'Time', 'Edges Processed'])
    
    for x in range(0, len(GRAPHS)) :
        table.add_row(['Bellman-Ford 0', GRAPHS[x][0], GRAPHS[x][1], '%.4f' % TIME[0][x], EDGES_PROCESSED[0][x]])
        table.add_row(['Bellman-Ford 1', GRAPHS[x][0], GRAPHS[x][1], '%.4f' % TIME[1][x], EDGES_PROCESSED[1][x]])
        table.add_row(['Bellman-Ford 2', GRAPHS[x][0], GRAPHS[x][1], '%.4f' % TIME[2][x], EDGES_PROCESSED[2][x]])
        table.add_row(['Bellman-Ford 3', GRAPHS[x][0], GRAPHS[x][1], '%.4f' % TIME[3][x], EDGES_PROCESSED[3][x]])
        table.add_row(['Bellman-Ford 4', GRAPHS[x][0], GRAPHS[x][1], '%.4f' % TIME[4][x], EDGES_PROCESSED[4][x]])
        table.add_row(['','','','',''])
    table.del_row(len(table._rows)-1)
    print(table)
    
    table = pt.PrettyTable(['', 'Belllman-Ford 0', 'Belllman-Ford 1', 'Belllman-Ford 2', 'Belllman-Ford 3'])
    table.add_row(['Average Time', sum(TIME[0]) / len(TIME[0]), sum(TIME[1]) / len(TIME[1]), sum(TIME[2]) / len(TIME[2]), sum(TIME[3]) / len(TIME[3]), sum(TIME[4]) / len(TIME[4])])
    table.add_row(['Average Edge', sum(EDGES_PROCESSED[0]) / len(EDGES_PROCESSED[0]), sum(EDGES_PROCESSED[1]) / len(EDGES_PROCESSED[1]), sum(EDGES_PROCESSED[2]) / len(EDGES_PROCESSED[2]), sum(EDGES_PROCESSED[3]) / len(EDGES_PROCESSED[3]), sum(EDGES_PROCESSED[4]) / len(EDGES_PROCESSED[4])])
    print(table)
        
if __name__ == "__main__" :
    main()