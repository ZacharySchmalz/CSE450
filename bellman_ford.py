import time
import csv
import sys

# Use the command "python bellman_ford.py 'graph_name.csv' True" to run the program
# Substitute graph_name with the name of the graph that is in the same directory as this file (without quotes)
# The 'True' argument is optional, and will signal to the program to print the paths at the end

# Example command using the graph.csv datset: python bellman_ford.py graph.csv True

# Grab the filename from the first command argument
FILENAME = str(sys.argv[1])
# Set the delimiter for the file (graph.csv and other generated graphs will use commas)
DELIMITER = ','

# Class definition for a graph
class Graph :
    # Initialzies the graph, reading in edges and vertices from filename using the specified delimiter
    def __init__(self, filename, delim) :
        # Time graph creation 
        start = time.time()
    
        # Vertices are a HashMap / Dictionary for faster vertex access
        self.vertices = {}
        # Edges are a simple list since we have to access every edge anyways
        self.edges = []
        
        # Load vertices and edges into graph from filename
        self.createGraph(filename, delim)

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
    def createGraph(self, filename, delim) :
        with open(filename) as file :
            reader = csv.reader(file, delimiter = delim)
            for row in reader :
                # Add source vertex
                self.addVertex(int(row[0]))
                # Add destination vertex
                self.addVertex(int(row[1]))
                # Add the [Source, Destination, Weight] edge
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
    for i in range(len(vertices)) :
        distance[i] = float('Inf')
        predecessor[i] = None
    
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
    print('|\tTo\t|\tWeight\t|\tPath\n|\t\t|\t\t|\t')
    for i in range(0, len(vertices)) :
        path = [i]
        pred = predecessor[i]
        while pred != None:
            path += [pred]
            pred = predecessor[pred]
        path.reverse()
        
        # No path exists from source vertices to vertex i
        if distance[i] == float('Inf'):
            print('|\t', i, '\t|\t', distance[i], '\t|\t', '[No path exists]', sep='')
            
        # Print path and distance
        else :
            print('|\t', i, '\t|\t', distance[i], '\t|\t', path, sep='')

# Create graph
graph = Graph(FILENAME, DELIMITER)

# Run the algorithm on the graph
result, distance, predecessor = BellmanFord(graph, 0)

# Print paths
if result and len(sys.argv) > 2 and str(sys.argv[2]) == 'True':
    PrintPaths(distance, graph.vertices, predecessor, 0)