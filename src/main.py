import networkx as nx
import random
import itertools
import numpy as np
from ullman import ullman_algorithm  # Assuming ullman.py is in the same folder
from edges_verification import check_isomorphism  # Assuming edges_verification.py is in the same folder

# Graph generation and saving functions
def generate_random_graph(n, m):
    """Generate a random graph with n nodes and m edges."""
    if m > n * (n - 1) // 2:
        raise ValueError("The number of edges m is too large for the number of nodes n.")
    
    G = nx.Graph()
    G.add_nodes_from(range(n))

    # Generate m random edges
    edges = set()
    while len(edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:  # Prevent self-loops
            edges.add(tuple(sorted([u, v])))

    G.add_edges_from(edges)
    return G

def save_graph_to_file(graph, filename):
    """Save the graph to a file."""
    with open(filename, 'w') as f:
        for edge in graph.edges():
            f.write(f"{edge[0]} {edge[1]}\n")

def generate_and_save_random_graphs(num_graphs, max_nodes, max_edges, filename_prefix):
    """Generate and save random graphs."""
    for i in range(num_graphs):
        n = random.randint(1, max_nodes)
        
        # Handle the case where n = 1 separately to avoid the empty range issue
        if n == 1:
            m = 0  # No edges for a single node
        else:
            max_possible_edges = n * (n - 1) // 2
            m = random.randint(1, min(max_possible_edges, max_edges))
        
        # Ensure that the number of edges m is valid
        if m == 0 and n > 1:
            m = 1  # Ensure at least one edge for n > 1
        
        G = generate_random_graph(n, m)
        
        # Save graph to file
        filename = f"{filename_prefix}_graph_{i+1}.txt"
        save_graph_to_file(G, filename)
        print(f"Graph {i+1} with {n} nodes and {m} edges saved to {filename}")

# Graph loading and comparison functions
def load_graph_from_file(filename):
    """Load a graph from a file where each line represents an edge."""
    G = nx.Graph()
    with open(filename, 'r') as f:
        for line in f:
            u, v = map(int, line.split())
            G.add_edge(u, v)
    return G

def compare_isomorphisms(G1, G2):
    """Compare isomorphism results from Ullman and edge verification methods."""
    # Convert NetworkX graphs to adjacency matrices
    G1_adj = nx.to_numpy_array(G1)
    G2_adj = nx.to_numpy_array(G2)
    
    # Check isomorphism using Ullman's algorithm
    ullman_result = ullman_algorithm(G1_adj, G2_adj)
    
    # Check isomorphism using the edge verification method
    edge_verification_result = check_isomorphism(G1, G2)
    
    print(f"Ullman Algorithm Result: {ullman_result}")
    print(f"Edge Verification Result: {edge_verification_result}")
    
    if ullman_result == edge_verification_result:
        print("Both algorithms agree: Isomorphism:", ullman_result)
    else:
        print("The algorithms disagree.")

def main():
    # Generate and save random graphs
    num_graphs = 10
    max_nodes = 10
    max_edges = 15
    filename_prefix = "random_graph"
    generate_and_save_random_graphs(num_graphs, max_nodes, max_edges, filename_prefix)
    
    # Load all generated graphs
    graphs = []
    for i in range(num_graphs):
        filename = f"{filename_prefix}_graph_{i+1}.txt"
        G = load_graph_from_file(filename)
        graphs.append(G)
    
    # Compare all pairs of graphs
    for i in range(num_graphs):
        for j in range(i + 1, num_graphs):
            print(f"\nComparing Graph {i+1} and Graph {j+1}:")
            compare_isomorphisms(graphs[i], graphs[j])

if __name__ == "__main__":
    main()