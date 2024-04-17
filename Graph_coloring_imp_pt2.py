import random
import time

class GraphColoring:
    def __init__(self, filename):
        self.graph = self.read_graph(filename)
        self.V = len(self.graph)
        self.colors = [-1] * self.V
        self.degrees = [len(adj) for adj in self.graph]

    def read_graph(self, filename):
        graph = []
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    _, edges = parts
                    graph.append(list(map(int, edges.split())))
                else:
                    graph.append([])
        return graph

    def smallest_last_ordering(self):
        ordering = []
        degrees = self.degrees.copy()
        for _ in range(self.V):
            min_degree_vertex = degrees.index(min(degrees))
            ordering.append(min_degree_vertex)
            degrees[min_degree_vertex] = self.V + 1
            for neighbor in self.graph[min_degree_vertex]:
                degrees[neighbor] -= 1
        return ordering[::-1]

    def smallest_original_degree_last(self):
        return sorted(range(self.V), key=lambda x: self.degrees[x])

    def uniform_random_ordering(self):
        ordering = list(range(self.V))
        random.shuffle(ordering)
        return ordering

    def largest_degree_first_ordering(self):
        return sorted(range(self.V), key=lambda x: -self.degrees[x])

    def degree_of_saturation_ordering(self):
        saturation = [0] * self.V
        ordering = []
        while len(ordering) < self.V:
            max_sat = -1
            for i in range(self.V):
                if i not in ordering and (saturation[i] > max_sat or (saturation[i] == max_sat and self.degrees[i] > self.degrees[vertex])):
                    max_sat = saturation[i]
                    vertex = i
            ordering.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in ordering:
                    saturation[neighbor] += 1
        return ordering

    def color_graph(self, ordering):
        for vertex in ordering:
            forbidden = [False] * self.V
            for neighbor in self.graph[vertex]:
                if self.colors[neighbor] != -1:
                    forbidden[self.colors[neighbor]] = True
            self.colors[vertex] = next(color for color, used in enumerate(forbidden) if not used)

    def print_coloring_results(self):
        for i, color in enumerate(self.colors):
            print(f"Vertex {i}: Color {color}")

    def process_graph(self, filename):
        print(f"\nProcessing file: {filename}")
        orderings = [
            (self.smallest_last_ordering, "Smallest Last Ordering"),
            (self.smallest_original_degree_last, "Smallest Original Degree Last"),
            (self.uniform_random_ordering, "Uniform Random Ordering"),
            (self.largest_degree_first_ordering, "Largest Degree First Ordering"),
            (self.degree_of_saturation_ordering, "Degree of Saturation Ordering"),
        ]
        for method, name in orderings:
            start_time = time.perf_counter()
            print(f"\n{name}:")
            self.color_graph(method())
            self.print_coloring_results()
            elapsed_time = time.perf_counter() - start_time
            elapsed_time_microseconds = elapsed_time * 1_000_000
            print(f"Elapsed Time: {elapsed_time_microseconds:.2f} microseconds")
            print(f"Total Colors Used: {max(self.colors) + 1}")
            self.colors = [-1] * self.V

def main():
    filenames = ["output_complete_graph.txt", "output_random_uniform.txt", "output_cycle_graph.txt"]
    for filename in filenames:
        graph_coloring = GraphColoring(filename)
        graph_coloring.process_graph(filename)

if __name__ == "__main__":
    main()
