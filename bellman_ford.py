import time
import csv
import sys

#vertices = [0,1,2,3,4]
#edges = [[0,1,-1],[0,2,4],[1,2,3],[1,3,2],[1,4,2],[3,2,5],[3,1,1],[4,3,-3]]

class Graph :
    def __init__(self, filename, delim) :
        self.vertices = {}
        self.edges = []
        
        start = time.time()
        self.createGraph(filename, delim)

        print('Graph Created: ', time.time() - start)
        print('Vertices: ', len(self.vertices), sep='')
        print('Edges: ', len(self.edges), '\n', sep='')
        
    def addEdge(self, source, dest, weight) :
        self.edges.append([source, dest, weight])
        
    def addVertex(self, vertex) :
        if vertex not in self.vertices :
            self.vertices[vertex] = len(self.vertices)

    def createGraph(self, filename, delim) :
        with open(filename) as file :
            reader = csv.reader(file, delimiter = delim)
            for row in reader :
                self.addVertex(int(row[0]))
                self.addVertex(int(row[1]))
                self.addEdge(int(row[0]), int(row[1]), int(row[2]))

def BellmanFord(vertices, edges, source) :
    # Step 1: Initialize graph
    distance = {}
    predecessor = {}
    for i in range(len(vertices)) :
        distance[i] = float('Inf')
        predecessor[i] = None
    
    distance[vertices[source]] = 0
    
    # Step 2: Calculate shortest distances
    for i in range(len(vertices)) :
        sys.stdout.write('\rProgress [' + str(int(i+1)) + '/' + str(int(len(vertices))) + ']')
        sys.stdout.flush()
        for u,v,w in edges :
            uIndex = vertices[u]
            vIndex = vertices[v]
            if distance[uIndex] != float('Inf') and distance[uIndex] + w < distance[vIndex] :
                distance[vIndex] = distance[uIndex] + w
                predecessor[vIndex] = vertices[u]
    print(distance)
    # Step 3: Check for negative-weight cycle
    for u,v,w in edges :
        if distance[vertices[u]] != float('Inf') and distance[vertices[u]] + w < distance[vertices[v]] :
            print('\n\nGraph contains a negative-weight cycle\n\n')
            return False, distance, predecessor
    
    return True, distance, predecessor
    
def PrintPaths(distance, vertices, predecessor, source) :
    print('Paths and Weights from Source: ', source, '\n')
    for i in range(0, len(vertices)) :
        if i == source :
            continue
        path = [i]
        pred = predecessor[i]
        while pred != None :
            path += [pred]
            pred = predecessor[pred]
        path.reverse()
        print('To[', i, '] | Weight[', distance[i], ']\t', path, sep='')
    
graph = Graph('monk.csv', ' ')

result, distance, predecessor = BellmanFord(graph.vertices, graph.edges, 1)

#PrintPaths(distance, graph.vertices, predecessor, 1)