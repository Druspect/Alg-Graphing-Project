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

def generate_uniform_cycle(graph, E):
    added_edges = set()
    if (E != graph.V):
        print ('ERROR: Cycle max number of edges must be: ', graph.V, ' not ', E)
        E = graph.V
        print('E set to: ', E)
    # Generages a cycle graph with uniform distribution
    for i in range(graph.V):
        startNode, destNode = -1, -1  # initialization
        if (i == graph.V - 1):  # this is the last node, wrap around to start
            startNode, destNode = i, 0
        else:  # This is a non-terminal node, so just connect to adjacent node
            startNode, destNode = i, i + 1
        graph.add_edge(startNode, destNode)
        added_edges.add((startNode, destNode))

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
        if DIST == 'UNIFORM':
            generate_uniform_cycle(graph, E)
    graph.print_graph()

# Example Usage
# main(V=10, E=20, G='RANDOM', DIST='UNIFORM')
main(V=10, E=10, G='CYCLE', DIST='UNIFORM')

# Cycle testing

