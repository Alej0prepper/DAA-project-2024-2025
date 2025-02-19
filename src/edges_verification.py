import numpy as np
from itertools import combinations

def node_degree_sequence(adj_matrix):
    """Returns a sorted list of node degrees from an adjacency matrix."""
    return sorted(np.sum(adj_matrix, axis=1))

def canonical_form(adj_matrix):
    """Returns the canonical form of the adjacency matrix by sorting nodes based on degree and index."""
    n = adj_matrix.shape[0]
    degrees = np.sum(adj_matrix, axis=1)
    # Sort nodes by degree (ascending), then by original index (ascending)
    sorted_nodes = sorted(range(n), key=lambda x: (degrees[x], x))
    return adj_matrix[np.ix_(sorted_nodes, sorted_nodes)]

def find_isomorphic_subgraph(G1, G2):
    """Checks if G1 is isomorphic to a subgraph of G2 using canonical forms."""
    k = G1.shape[0]
    target_degree_seq = node_degree_sequence(G1)
    G1_canonical = canonical_form(G1)
    n = G2.shape[0]

    for nodes_subset in combinations(range(n), k):
        subgraph = G2[np.ix_(nodes_subset, nodes_subset)]
        sub_degree_seq = node_degree_sequence(subgraph)
        if sub_degree_seq != target_degree_seq:
            continue  # Degree sequences don't match

        sub_canonical = canonical_form(subgraph)
        if np.array_equal(sub_canonical, G1_canonical):
            return True  # Found an isomorphic subgraph

    return False  # No isomorphic subgraph found
