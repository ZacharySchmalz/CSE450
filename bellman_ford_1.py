import bellman_ford as bf
import time
import sys

def BellmanFord(graph, source) :
    start = time.time()

    vertices = graph.vertices
    edges = graph.edges
    
    distance = {}
    predecessor = {}

    for key in vertices.keys() :
        distance[key] = float('Inf')
        predecessor[key] = None

    distance[source] = 0

    # Step 2: Relax all edges |Vertices| - 1 times
    for i in range(len(vertices) - 1) :
        earlyTermination = True
    
        sys.stdout.write('\rProgress [' + str(int(i+1)) + '/' + str(int(len(vertices))) + ']')
        sys.stdout.flush()
        
        for u,v,w in edges :
            # If an edge has a cheaper edge weight to destination vertex
            if distance[u] != float('Inf') and distance[u] + w < distance[v] :
                # Update distance and predecessor to destination vertex v
                distance[v] = distance[u] + w
                predecessor[v] = u
                earlyTermination = False
                
        if earlyTermination :
            break

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

def main() :
    # Create graph
    graph = bf.Graph(bf.FILENAME)

    # Run the algorithm on the graph
    result, distance, predecessor = BellmanFord(graph, 1)

    # Print paths
    if result and len(sys.argv) > 2 and str(sys.argv[2]) == 'True':
        bf.PrintPaths(distance, graph.vertices, predecessor, 1)
        
if __name__ == "__main__" :
    main()