import bellman_ford as bf
import bellman_ford_1 as bf1
import bellman_ford_yen1 as bfYen1
import bellman_ford_yen2 as bfYen2
import generate_graph as generator
import random

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
    local_random = random.Random()
    graph = Graph(generator.GenerateGraph(), local_random)
    print(graph.edges)
        
if __name__ == "__main__" :
    main()