import random
import numpy as np

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
    
    def add_edge(self, u, v):
        if v not in self.graph[u] and u != v:
            self.graph[u].append(v)
            self.graph[v].append(u)
    
    def print_graph(self):
        for i in range(self.V):
            print(f"{i} --> {' '.join(map(str, self.graph[i]))}")

def generate_uniform(graph, E):
    added_edges = set()
    while E > 0:
        u, v = random.randint(0, graph.V - 1), random.randint(0, graph.V - 1)
        if u != v and (u, v) not in added_edges and (v, u) not in added_edges:
            graph.add_edge(u, v)
            added_edges.add((u, v))
            E -= 1

def generate_skewed(graph, E):
    added_edges = set()
    while E > 0:
        u, v = int(graph.V * (1 - np.sqrt(1 - random.uniform(0, 1)))), int(graph.V * (1 - np.sqrt(1 - random.uniform(0, 1))))
        if u != v and (u, v) not in added_edges and (v, u) not in added_edges:
            graph.add_edge(u, v)
            added_edges.add((u, v))
            E -= 1

def generate_custom(graph, E):
    # Implement your custom distribution here. This is just a placeholder.
    pass

def generate_cycle_graph(graph, E):
    # Generates a cycle graph
    if (E != graph.V):
        print ('ERROR: Cycle max number of edges must be: ', graph.V, ' not ', E)
        E = graph.V
        print('E set to: ', E)

    for i in range(graph.V):
        startNode, destNode = -1, -1  # initialization
        if (i == graph.V - 1):  # this is the last node, wrap around to start
            startNode, destNode = i, 0
        else:  # This is a non-terminal node, so just connect to adjacent node
            startNode, destNode = i, i + 1
        graph.add_edge(startNode, destNode)

def generate_complete_graph (graph, E):
    # Generates a complete graph
    expectedEdgeCount = (graph.V * (graph.V - 1) / 2)
    expectedEdgeCount = int(expectedEdgeCount)

    if(E != expectedEdgeCount):
        print ('ERROR: Complete graph must have ', expectedEdgeCount, 'edges not ', E, ' edges')
        E = expectedEdgeCount
        print('E set to: ', E)
    for i in range(graph.V):
        for j in range(graph.V):
            if(j != i):
                graph.add_edge(i, j)

def save_graph_to_file(graph, filename):
    with open(filename, 'w') as file:
        for u in range(graph.V):
            file.write(f"{u}: {' '.join(map(str, graph.graph[u]))}\n")

def main(V, E, G, DIST):
    graph = Graph(V)
    if G == 'RANDOM':
        if DIST == 'UNIFORM':
            generate_uniform(graph, E)
        elif DIST == 'SKEWED':
            generate_skewed(graph, E)
        elif DIST == 'YOURS':
            generate_custom(graph, E)
    # Implementations for COMPLETE or CYCLE graphs can be added here
    elif G == 'CYCLE':
        if DIST == 'UNIFORM':  # Must be uniform
            generate_cycle_graph(graph, E)

    elif G == 'COMPLETE':
        if DIST == 'UNIFORM':  # Must be uniform
            generate_complete_graph(graph, E)

    graph.print_graph()
    save_graph_to_file(graph, "output_complete_graph.txt")

# Example Usage
# main(V=10, E=20, G='RANDOM', DIST='UNIFORM')

# Cycle testing
# main(V=10, E=10, G='CYCLE', DIST='UNIFORM')

# Complete testing
main(V=10, E=10, G='COMPLETE', DIST='UNIFORM')

