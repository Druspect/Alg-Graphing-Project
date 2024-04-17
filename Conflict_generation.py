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

def generate_cycle_graph(graph):
    # Generates a cycle graph
    for i in range(graph.V):
        if (i == graph.V - 1):  # this is the last node, wrap around to start
            graph.add_edge(i, 0)
        else:  # This is a non-terminal node, so just connect to adjacent node
            graph.add_edge(i, i + 1)

def generate_complete_graph(graph):
    # Generates a complete graph
    for i in range(graph.V):
        for j in range(i + 1, graph.V):
            graph.add_edge(i, j)

def save_graph_to_file(graph, filename):
    with open(filename, 'w') as file:
        for u in range(graph.V):
            file.write(f"{u}: {' '.join(map(str, graph.graph[u]))}\n")

def main(V, G, filename, DIST='UNIFORM'):
    graph = Graph(V)
    if G == 'RANDOM':
        if DIST == 'UNIFORM':
            generate_uniform(graph, int(V*(V-1)/4))  # Example for medium density
        elif DIST == 'SKEWED':
            generate_skewed(graph, int(V*(V-1)/4))  # Example for medium density
    elif G == 'CYCLE':
        generate_cycle_graph(graph)
    elif G == 'COMPLETE':
        generate_complete_graph(graph)
    
    graph.print_graph()
    save_graph_to_file(graph, filename)

# Example Usage
main(V=10, G='RANDOM', filename="output_random_uniform.txt")
main(V=10, G='CYCLE', filename="output_cycle_graph.txt")
main(V=10, G='COMPLETE', filename="output_complete_graph.txt")

