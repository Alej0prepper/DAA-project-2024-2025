<<<<<<< HEAD
import numpy as np
from itertools import combinations, permutations

def node_degree_sequence(adj_matrix):
    """
    Returns a sorted list of node degrees from an adjacency matrix.
    """
    return sorted(np.sum(adj_matrix, axis=1))  # Sum of each row gives the degree

def find_isomorphic_subgraph(G1, G2):
    """
    Checks if G1 is isomorphic to a subgraph of G2 using adjacency matrices.
    """
    k = G1.shape[0]  # Number of nodes in G1
    target_degree_seq = node_degree_sequence(G1)
    n = G2.shape[0]  # Number of nodes in G2

    for nodes_subset in combinations(range(n), k):
        subgraph = G2[np.ix_(nodes_subset, nodes_subset)]  # Extract submatrix

        # Compare degree sequences
        sub_degree_seq = node_degree_sequence(subgraph)
        if sub_degree_seq != target_degree_seq:
            continue  # Skip if degree sequences don't match

        # Check for isomorphism by trying all possible label permutations
        for perm in permutations(range(k)):
            permuted_subgraph = subgraph[np.ix_(perm, perm)]
            if np.array_equal(permuted_subgraph, G1):
                return True  # Found an isomorphic subgraph

    return False  # No isomorphic subgraph found

# Example usage:
if __name__ == '__main__':
    G1 = np.array([[0, 1, 1],
                   [1, 0, 0],
                   [1, 0, 0]])

    G2 = np.array([[0, 1, 1, 0],
                   [1, 0, 0, 1],
                   [1, 0, 0, 1],
                   [0, 1, 1, 0]])

    result = find_isomorphic_subgraph(G1, G2)
    print("Isomorphic subgraph found!" if result else "No subgraph isomorphism.")
=======
import itertools
import networkx as nx

def find_subgraphs(G1, G2):
    """Find all subgraphs of size equal to G1 in G2."""
    n = len(G2.nodes)
    k = len(G1.nodes)
    subgraphs = []
    
    # Generate all combinations of k nodes in G2
    for nodes in itertools.combinations(G2.nodes, k):
        # Create the subgraph induced by these nodes in G2
        subgraph = G2.subgraph(nodes)
        subgraphs.append(subgraph)
    
    return subgraphs

def calculate_degrees(graph):
    """Calculate the degree of each node in the graph."""
    degrees = {node: degree for node, degree in graph.degree()}
    return degrees

def get_edges(graph, node_degrees):
    """Return the edges with the lower degree node first."""
    edges = []
    for u, v in graph.edges():
        # Get degrees of nodes u and v
        deg_u = node_degrees[u]
        deg_v = node_degrees[v]
        # Add edge with the node of lower degree first
        if deg_u < deg_v:
            edges.append((u, v))
        else:
            edges.append((v, u))
    return edges

def check_isomorphism(G1, G2):
    """Check if there is an isomorphism between G1 and G2."""
    # Find all subgraphs of G2 of size equal to G1
    subgraphs = find_subgraphs(G1, G2)
    
    # Calculate degrees for G1
    degree_G1 = calculate_degrees(G1)
    
    for subgraph in subgraphs:
        # Calculate degrees for the subgraph
        degree_subgraph = calculate_degrees(subgraph)
        
        # Get edges sorted by the node degrees in the subgraph
        edges_G1 = get_edges(G1, degree_G1)
        edges_subgraph = get_edges(subgraph, degree_subgraph)
        
        # Compare the sorted edges
        if edges_G1 == edges_subgraph:
            return True  # Isomorphism found
    
    return False  # No isomorphism found
>>>>>>> ee2797e193454cb4d77b916775fc6dd70774a004
