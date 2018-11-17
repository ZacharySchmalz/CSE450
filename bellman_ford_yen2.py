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

    edgesF = []
    edgesB = []
    
    for edge in edges :
        if edge[0] < edge[1] :
            edgesF.append(edge)
        else :
            edgesB.append(edge)
    
    changedVerts = [source]
    container = []
    
    while len(changedVerts) > 0 :
        index = 0
        
        # Step 2A: Relax all edges in edgesF in ascending sorted order from vertex 1 to |V|
        for key in sorted(changedVerts) :
            earlyTermination = True
            
            #index += 1
            #sys.stdout.write('\rEdgesF Progress [' + str(index) + '/' + str(int(len(vertices))) + '][' + str(len(edgesF)) + ']')
            #sys.stdout.flush()
            
            # Iterate through all edges
            for u,v,w in edgesF :
                # If an edge has a cheaper edge weight to destination vertex
                if distance[u] != float('Inf') and distance[u] + w < distance[v] :
                    # Update distance and predecessor to destination vertex v
                    distance[v] = distance[u] + w
                    predecessor[v] = u
                    earlyTermination = False
                    if v not in container :
                        container.append(v)

                    
            if earlyTermination :
                break        
            
        index = 0
        # Step 2B: Relax all edges in edgesB in descending sorted order from vertex |V| to 1
        for key in sorted(changedVerts, reverse=True) :
            earlyTermination = True
            
            #index += 1
            #sys.stdout.write('\rEdgesB Progress [' + str(index) + '/' + str(int(len(vertices))) + '][' + str(len(edgesB)) + ']')
            #sys.stdout.flush()
            
            # Iterate through all B edges
            for u,v,w in edgesB :                
                # If an edge has a cheaper edge weight to destination vertex
                if distance[u] != float('Inf') and distance[u] + w < distance[v] :
                    # Update distance and predecessor to destination vertex v
                    distance[v] = distance[u] + w
                    predecessor[v] = u
                    earlyTermination = False
                    if v not in container :
                        container.append(v)
                        
            if earlyTermination :
                break
            
        changedVerts.clear()
        changedVerts = container.copy()
        container.clear()         
    
    # Step 3: Check for negative-weight cycle.
    for u,v,w in edges :
        # If a shorter path is found, graph contains a negative-weight cycle
        if distance[u] + w < distance[v] :
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