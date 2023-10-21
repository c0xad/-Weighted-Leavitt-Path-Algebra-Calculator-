import networkx as nx  # You'll need to install the networkx library for visualization

class WeightedLeavittPathAlgebra:
    def __init__(self):
        self.graph = nx.DiGraph()  # A directed graph to represent the Weighted Leavitt Path Algebra
        self.path_weights = {}
    
    def add_edge(self, source, target, weight):
        self.graph.add_edge(source, target, weight=weight)
    
    def add_vertex(self, vertex, weight=0):
        self.path_weights[vertex] = weight

    def calculate_weighted_leavitt_path_algebra(self):
        for node in self.graph.nodes():
            self.path_weights[node] = self.calculate_path_weight(node)
    
    def calculate_path_weight(self, vertex):
        if not list(self.graph.predecessors(vertex)):
            return self.path_weights[vertex]
        return max(self.path_weights[pred] + self.graph[pred][vertex]['weight'] for pred in self.graph.predecessors(vertex))
    
    def multiply(self, element1, element2):
        return self.path_weights[element1] * self.path_weights[element2]
    
    def visualize(self):
        # Visualize the directed graph with weights using networkx
        pos = nx.spring_layout(self.graph, seed=42)  # You can choose different layouts
        labels = {node: f"{node}\n{self.path_weights[node]:.2f}" for node in self.graph.nodes()}
        nx.draw(self.graph, pos, with_labels=True, labels=labels, node_size=5000, node_color='lightblue')
        edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in self.graph.edges(data=True)}
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.show()

# Example usage
wlp = WeightedLeavittPathAlgebra()

wlp.add_edge("v1", "v2", 2.5)
wlp.add_edge("v2", "v3", 1.5)

wlp.add_vertex("v1", weight=0)  # Initial weight for v1

wlp.calculate_weighted_leavitt_path_algebra()

result = wlp.multiply("v1", "v2")
print("v1 * v2 =", result)

wlp.visualize()
