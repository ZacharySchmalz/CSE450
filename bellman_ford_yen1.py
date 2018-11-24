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
    
    changedVerts = [source]
    container = []
    
    while len(changedVerts) > 0:

        # Iterate through only changed vertices
        for key in changedVerts:
            
            # Iterate through all edges out of key            
            for u,v,w in edges:
            
                # If an edge has a cheaper edge weight to destination vertex
                if u == key and distance[u] != float('Inf') and distance[u] + w < distance[v] :
                
                    # Update distance and predecessor to destination vertex v
                    distance[v] = distance[u] + w
                    predecessor[v] = u
                    
                    # Check that the node is not already added
                    if v not in container :
                        container.append(v)

        changedVerts.clear()
        changedVerts = container.copy()
        container.clear()
    
    # Print complete message
    sys.stdout.write('\rProgress [' + str(int(len(vertices))) + '/' + str(int(len(vertices))) + '] - Complete\n')
    sys.stdout.flush()            
    
    # Step 3: Check for negative-weight cycle.
    for u,v,w in edges :
        # If a shorter path is found, graph contains a negative-weight cycle
        if distance[u] != float('Inf') and distance[u] + w < distance[v] :
            print('\nGraph contains a negative-weight cycle\n\n')
            
            # Return distances, predecessors, and False signaling graph contains negative-weight cycle
            return False, distance, predecessor
    
    # Print algorithm running time
    print('\nBellmanFord [Vertices: ', len(vertices), '][Edges: ', len(edges), '] in ', time.time() - start, '\n', sep='')
    
    # Graph does not contain a negative weight cycle
    return True, distance, predecessor

def main() :
    # Create graph
    graph = bf.Graph(bf.FILENAME)

    # Run the algorithm on the graph
    result, distance, predecessor = BellmanFord(graph, 0)

    # Print paths
    if result and len(sys.argv) > 2 and str(sys.argv[2]) == 'True':
        bf.PrintPaths(distance, graph.vertices, predecessor, 0)
        
if __name__ == "__main__" :
    main()
