import random
import time
import csv
import sys

# Use the command "python bellman_ford.py 'graph_name.csv' True" to run the program
# Substitute graph_name with the name of the graph that is in the same directory as this file (without quotes)
# The 'True' argument is optional, and will signal to the program to print the paths at the end

# Example command using the graph.csv datset: python bellman_ford.py graph.csv True

# Grab the filename from the first command argument
FILENAME = str(sys.argv[1])

random.seed()

# Class definition for a graph
class Graph :
    # Initialzies the graph, reading in edges and vertices from filename using the specified delimiter
    def __init__(self, filename) :
        # Time graph creation 
        start = time.time()
    
        # Vertices are a HashMap / Dictionary for faster vertex access
        self.vertices = {}
        # Edges are a simple list since we have to access every edge anyways
        self.edges = []
        
        # Load vertices and edges into graph from filename
        self.createGraph(filename)

        # Print graph creation time, vertex count and edge count
        print('\nGraph Created: ', time.time() - start)
        print('Vertices: ', len(self.vertices), sep='')
        print('Edges: ', len(self.edges), '\n', sep='')
    
    # Adds an edge to the graph. Edge structure is a list containing [Source, Destination, Weight]
    def addEdge(self, source, dest, weight) :
        self.edges.append([source, dest, weight])
    
    # Adds a vertex to the graph. Key/Value structure is [Vertex_Number , Index_In_List]
    def addVertex(self, vertex) :
        # Do not add duplicate vertices
        if vertex not in self.vertices :
            self.vertices[vertex] = len(self.vertices)

    # Open dataset-containing file and read data
    def createGraph(self, filename) :
        # Detect the row delimiter
        delim = ''
        with open(filename + '.csv') as file :
            line = file.readline()
            for char in line :
                if not char.isdigit() :
                    delim = char
                    file.seek(0)
                    break
            reader = csv.reader(file, delimiter = delim)
            for row in reader :
                # Add source vertex
                self.addVertex(int(row[0]))
                # Add destination vertex
                self.addVertex(int(row[1]))
                # Add the [Source, Destination, Weight] edge
                if len(row) == 2 :
                    self.addEdge(int(row[0]), int(row[1]), random.randint(-10,10))
                elif len(row) >= 3 :
                    self.addEdge(int(row[0]), int(row[1]), int(row[2]))

# Function for performing the BellmanFord algorithm on a graph from a particular source vertex
def BellmanFord(graph, source) :
    # Time the algorithm
    start = time.time()

    # Get vertices and edges
    vertices = graph.vertices
    edges = graph.edges
    
    # Step 1: Initialize distance and predecessor HashMaps / Dictionaries
    
    # Contains total path distance from source vertex to index-vertex
    # Example: Entry [50 : -9] menas the total path distance from source vertex to vertex 50 is -9
    distance = {}

    # Contains predecessor information for tracing path from a vertex to source node
    # Example" Entry [45 : 36] means the predecessor of vertex 45 is vertex 36
    predecessor = {}
    
    # Initialize distances to Infinity and predecessors to None
    for key in vertices.keys() :
        distance[key] = float('Inf')
        predecessor[key] = None

    # Distance to source node is 0
    distance[source] = 0

    # Step 2: Relax all edges |Vertices| - 1 times
    for i in range(len(vertices) - 1) :
        # Print current vertex progress
        sys.stdout.write('\rProgress [' + str(int(i+1)) + '/' + str(int(len(vertices))) + ']')
        sys.stdout.flush()
        
        # Iterate through all edges
        for u,v,w in edges :
            # If an edge has a cheaper edge weight to destination vertex
            if distance[u] != float('Inf') and distance[u] + w < distance[v] :
                # Update distance and predecessor to destination vertex v
                distance[v] = distance[u] + w
                predecessor[v] = u

    # Print complete message
    sys.stdout.write('\rProgress [' + str(int(len(vertices))) + '/' + str(int(len(vertices))) + '] - Complete')
    sys.stdout.flush()            
    
    # Step 3: Check for negative-weight cycle.
    for u,v,w in edges :
        # If a shorter path is found, graph contains a negative-weight cycle
        if distance[u] + w < distance[v] :
            print('\n\nGraph contains a negative-weight cycle\n\n')
            
            # Return distances, predecessors, and False signaling graph contains negative-weight cycle
            return False, distance, predecessor
    
    # Print algorithm running time
    print('\n\nBellmanFord [Vertices: ', len(vertices), '][Edges: ', len(edges), '] in ', time.time() - start, '\n', sep='')
    
    # Graph does not contain a negative weight cycle
    return True, distance, predecessor
    
# Print the paths and distance from source vertex to all other vertices
def PrintPaths(distance, vertices, predecessor, source) :
    file = open(FILENAME + '_paths.txt', 'w')
    print('|\tTo\t|\tWeight\t|\tPath\n|\t\t|\t\t|\t')
    file.write('|\tTo\t|\tWeight\t|\tPath\n|\t\t|\t\t|\t\n')
    for key in sorted(vertices.keys()) :
        path = [key]
        node = predecessor[key]
        while node != None:
            path += [node]
            node = predecessor[node]
        path.reverse()
        
        line_to_print = ''
        
        # No path exists from source vertices to vertex i
        if distance[key] == float('Inf'):
            line_to_print = ('|\t' + str(key) + '\t|\t' + str(distance[key]) + '\t|\t' + '[No path exists]')
        # Print path and distance
        else :
            line_to_print = ('|\t' + str(key) + '\t|\t' + str(distance[key]) + '\t|\t' + str(path))
            
        print(line_to_print)
        file.write(line_to_print + '\n')
        
    file.close()

def main() :
    # Create graph
    graph = Graph(FILENAME)

    # Run the algorithm on the graph
    result, distance, predecessor = BellmanFord(graph, 1)

    # Print paths
    if result and len(sys.argv) > 2 and str(sys.argv[2]) == 'True':
        PrintPaths(distance, graph.vertices, predecessor, 1)
        
if __name__ == "__main__" :
    main()