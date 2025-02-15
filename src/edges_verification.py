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
