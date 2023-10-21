import networkx as nx
import matplotlib.pyplot as plt

class WeightedLeavittPathAlgebra:
    def __init__(self):
        self.graph = nx.DiGraph()  # A directed graph to represent the Weighted Leavitt Path Algebra
        self.path_weights = {}
    
    def add_edge(self, source, target, weight):
        """
        Add an edge to the Weighted Leavitt Path Algebra.

        Args:
            source (str): The source vertex.
            target (str): The target vertex.
            weight (float): The weight of the edge.
        """
        self.graph.add_edge(source, target, weight=weight)
    
    def add_vertex(self, vertex, weight=0):
        """
        Add a vertex to the Weighted Leavitt Path Algebra.

        Args:
            vertex (str): The vertex to add.
            weight (float, optional): The initial weight for the vertex. Default is 0.
        """
        self.path_weights[vertex] = weight

    def calculate_weighted_leavitt_path_algebra(self):
        """
        Calculate the Weighted Leavitt Path Algebra for all vertices in the graph.
        """
        for node in self.graph.nodes():
            self.path_weights[node] = self.calculate_path_weight(node)
    
    def calculate_path_weight(self, vertex):
        """
        Calculate the path weight for a vertex recursively.

        Args:
            vertex (str): The vertex to calculate the path weight for.

        Returns:
            float: The path weight of the vertex.
        """
        if not list(self.graph.predecessors(vertex)):
            return self.path_weights[vertex]
        return max(self.path_weights[pred] + self.graph[pred][vertex]['weight'] for pred in self.graph.predecessors(vertex))
    
    def multiply(self, element1, element2):
        """
        Perform multiplication in the Weighted Leavitt Path Algebra.

        Args:
            element1 (str): The first element.
            element2 (str): The second element.

        Returns:
            float: The result of the multiplication.
        """
        return self.path_weights[element1] * self.path_weights[element2]
    
    def visualize(self):
        """
        Visualize the Weighted Leavitt Path Algebra as a directed graph with weights.
        """
        pos = nx.spring_layout(self.graph, seed=42)  # You can choose different layouts
        labels = {node: f"{node}\n{self.path_weights[node]:.2f}" for node in self.graph.nodes()}
        nx.draw(self.graph, pos, with_labels=True, labels=labels, node_size=5000, node_color='lightblue')
        edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in self.graph.edges(data=True)}
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.show()

# Example usage
wlp = WeightedLeavittPathAlgebra()

# Add edges and vertices
wlp.add_edge("v1", "v2", 2.5)
wlp.add_edge("v2", "v3", 1.5)
wlp.add_vertex("v1", weight=0)

# Calculate the Weighted Leavitt Path Algebra
wlp.calculate_weighted_leavitt_path_algebra()

# Perform multiplication
result = wlp.multiply("v1", "v2")
print("v1 * v2 =", result)

# Visualize the algebra
wlp.visualize()
