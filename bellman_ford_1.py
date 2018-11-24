import bellman_ford as bf
import time
import sys

def BellmanFord(graph, source) :
    vertices = graph.vertices
    edges = graph.edges
    
    distance = {}
    predecessor = {}

    for key in vertices.keys() :
        distance[key] = float('Inf')
        predecessor[key] = None

    distance[source] = 0

    # Stats
    iterations = 0
    edgesProcessed = 0
    verticesUpdated = 0

    for _ in range(len(vertices) - 1) :
        # Early termination condition
        earlyTermination = True
    
        iterations += 1
        sys.stdout.write('\r\tIterations: [' + str(iterations) + ']')
        sys.stdout.flush()
        
        for u,v,w in edges :
            edgesProcessed += 1
            if distance[u] != float('Inf') and distance[u] + w < distance[v] :
                distance[v] = distance[u] + w
                predecessor[v] = u
                verticesUpdated += 1
                
                # A distance was updated
                earlyTermination = False
                
        # No distances were updated. break out of the loop
        if earlyTermination :
            break         
    
    for u,v,w in edges :
        if distance[u] + w < distance[v] :
            sys.stdout.write('\r\tBellman-Ford (Early Termination) - Graph contains a negative-weight cycle\n')
            sys.stdout.flush()
            
            return False, distance, predecessor, iterations, edgesProcessed, verticesUpdated
    
    sys.stdout.write('\r\tBellman-Ford (Early Termination) - Complete\n')
    sys.stdout.flush()
    
    return True, distance, predecessor, iterations, edgesProcessed, verticesUpdated

def main() :
    graph = bf.Graph(bf.FILENAME)

    result, distance, predecessor, _, _, _ = BellmanFord(graph, 0)

    if result and len(sys.argv) > 2 and str(sys.argv[2]) == 'True':
        bf.PrintPaths(distance, graph.vertices, predecessor, 0)
        
if __name__ == "__main__" :
    main()