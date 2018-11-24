import bellman_ford as bf
import time
import sys

def BellmanFord(graph, source) :
    # Move the source node to the beginning of vertex list
    vertices = list(graph.vertices).copy()
    vertices.remove(source)
    vertices.insert(0, source)
    
    edges = graph.edges
    
    distance = {}
    predecessor = {}
    
    for key in vertices :
        distance[key] = float('Inf')
        predecessor[key] = None

    distance[source] = 0

    # Create G+ and G- lists
    edgesF = []
    edgesB = []
    for edge in edges :
        if edge[0] < edge[1] :
            edgesF.append(edge)
        else :
            edgesB.append(edge)

    changedVerts = [source]
    container = []
    
    iterations = 0
    edgesProcessed = 0
    verticesUpdated = 0
    
    while len(changedVerts) > 0 :
        
        # Iterate through all vertices
        for vertex in vertices :
        
            if vertex in changedVerts :
                iterations += 1
                sys.stdout.write('\r\tIterations: [' + str(iterations) + ']')
                sys.stdout.flush()
                    
                # Iterate through all F edges
                for u,v,w in edgesF :
                    edgesProcessed += 1
                
                    if u == vertex and distance[u] != float('Inf') and distance[u] + w < distance[v] : 
                        distance[v] = distance[u] + w
                        predecessor[v] = u
                        verticesUpdated += 1

                        if v not in container :
                            container.append(v)
        
        # Iterate through reversed vertices
        for vertex in reversed(vertices) :
        
            if vertex in changedVerts :
                iterations += 1
                sys.stdout.write('\r\tIterations: [' + str(iterations) + ']')
                sys.stdout.flush()
            
                # Iterate through all B edges
                for u,v,w in edgesB :    
                    edgesProcessed += 1
                    
                    if u == vertex and distance[u] != float('Inf') and distance[u] + w < distance[v] : 
                        distance[v] = distance[u] + w
                        predecessor[v] = u
                        verticesUpdated += 1

                        if v not in container :
                            container.append(v)
            
        changedVerts.clear()
        changedVerts = container.copy()
        container.clear()         
    
    for u,v,w in edges :
        if distance[u] + w < distance[v] :
            sys.stdout.write('\r\tBellman-Ford (Yen\'s 2nd Improvement) - Graph contains a negative-weight cycle\n')
            sys.stdout.flush()
            
            return False, distance, predecessor, iterations, edgesProcessed, verticesUpdated
    
    sys.stdout.write('\r\tBellman-Ford (Yen\'s 2nd Improvement) - Complete\n')
    sys.stdout.flush()
    
    return True, distance, predecessor, iterations, edgesProcessed, verticesUpdated

def main() :
    graph = bf.Graph(bf.FILENAME)
    
    result, distance, predecessor, _, _, _ = BellmanFord(graph, 0)

    if result and len(sys.argv) > 2 and str(sys.argv[2]) == 'True':
        bf.PrintPaths(distance, graph.vertices, predecessor, 0)
        
if __name__ == "__main__" :
    main()