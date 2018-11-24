from PrettyTable import prettytable as pt
import bellman_ford as bf
import bellman_ford_1 as bf_early
import bellman_ford_yen1 as bf_yen1
import bellman_ford_yen2 as bf_yen2
import bellman_ford_random as bf_random
import generate_graph as generator
import random
import time

ALGORITHM_COUNT = 5
SOURCE = 2115173
#SOURCE = 0

GRAPHS = []
TIME = []
ITERATIONS = []
EDGES_PROCESSED = []
VERTICES_UPDATED = []

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
    for i in range(ALGORITHM_COUNT) :
        TIME.append([])
        ITERATIONS.append([])
        EDGES_PROCESSED.append([])
        VERTICES_UPDATED.append([])

    local_random = random.Random()
    graph = bf.Graph('patents')
    for i in range(10) :
        #graph = Graph(generator.GenerateGraph(), local_random)

        GRAPHS.append((len(graph.vertices),len(graph.edges)))
        
        print('Executing on Graph [', GRAPHS[i][0], '][', GRAPHS[i][1], ']', sep='') 
        
        for algorithm in range(ALGORITHM_COUNT) :
            iterations = edges_processed = vertices_updated = 0
            start = time.time()
            
            if algorithm == 0 :
                #_, _, _, iterations, edges_processed, vertices_updated = bf.BellmanFord(graph, SOURCE)
                print('\tBellman-Ford (Original) - Complete')
            elif algorithm == 1 : 
                _, _, _, iterations, edges_processed, vertices_updated = bf_early.BellmanFord(graph, SOURCE)
            elif algorithm == 2 : 
                _, _, _, iterations, edges_processed, vertices_updated = bf_yen1.BellmanFord(graph, SOURCE)
            elif algorithm == 3 : 
                _, _, _, iterations, edges_processed, vertices_updated = bf_yen2.BellmanFord(graph, SOURCE)
            elif algorithm == 4 : 
                _, _, _, iterations, edges_processed, vertices_updated = bf_random.BellmanFord(graph, SOURCE)
       
            TIME[algorithm].append(time.time() - start)
            ITERATIONS[algorithm].append(iterations)
            EDGES_PROCESSED[algorithm].append(edges_processed)
            VERTICES_UPDATED[algorithm].append(vertices_updated)
        print('\n')
         
    file = open('testing_results_patents.txt', 'w')
         
    table = pt.PrettyTable(['Algorithm', 'Graph Vertices', 'Graph Edges', 'Time', 'Iterations', 'Edges Processed', 'Vertices Updated'])    
    for x in range(len(GRAPHS)) :
        for y in range(ALGORITHM_COUNT) :
            table.add_row(['Bellman-Ford ' + str(y), GRAPHS[x][0], GRAPHS[x][1], '%.4f' % TIME[y][x], ITERATIONS[y][x], EDGES_PROCESSED[y][x], VERTICES_UPDATED[y][x]])
        table.add_row(['','','','','', '', ''])
    table.del_row(len(table._rows)-1)
    
    print(table)
    file.write(table.get_string() + '\n')
    
    
    table = pt.PrettyTable(['Averages', 'Belllman-Ford 0', 'Belllman-Ford 1', 'Belllman-Ford 2', 'Belllman-Ford 3', 'Bellman-Ford 4'])
    table.add_row(['Time', '%.4f' % (sum(TIME[0]) / len(TIME[0])), '%.4f' % (sum(TIME[1]) / len(TIME[1])), '%.4f' % (sum(TIME[2]) / len(TIME[2])), '%.4f' % (sum(TIME[3]) / len(TIME[3])), '%.4f' % (sum(TIME[4]) / len(TIME[4]))])
    table.add_row(['Iterations', sum(ITERATIONS[0]) / len(ITERATIONS[0]), sum(ITERATIONS[1]) / len(ITERATIONS[1]), sum(ITERATIONS[2]) / len(ITERATIONS[2]), sum(ITERATIONS[3]) / len(ITERATIONS[3]), sum(ITERATIONS[4]) / len(ITERATIONS[4])])
    table.add_row(['Edges Processed', sum(EDGES_PROCESSED[0]) / len(EDGES_PROCESSED[0]), sum(EDGES_PROCESSED[1]) / len(EDGES_PROCESSED[1]), sum(EDGES_PROCESSED[2]) / len(EDGES_PROCESSED[2]), sum(EDGES_PROCESSED[3]) / len(EDGES_PROCESSED[3]), sum(EDGES_PROCESSED[4]) / len(EDGES_PROCESSED[4])])
    table.add_row(['Vertices Updated', sum(VERTICES_UPDATED[0]) / len(VERTICES_UPDATED[0]), sum(VERTICES_UPDATED[1]) / len(VERTICES_UPDATED[1]), sum(VERTICES_UPDATED[2]) / len(VERTICES_UPDATED[2]), sum(VERTICES_UPDATED[3]) / len(VERTICES_UPDATED[3]), sum(VERTICES_UPDATED[4]) / len(VERTICES_UPDATED[4])])
    
    print(table)
    file.write(table.get_string() + '\n')
    
    file.close()
        
if __name__ == "__main__" :
    main()