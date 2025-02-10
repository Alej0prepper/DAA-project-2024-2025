import numpy as np

def is_isomorphism(G, P, M):
    """Checks if M represents a valid subgraph isomorphism between graphs G and P."""
    A = np.array(G)  # Adjacency matrix of the larger graph G
    B = np.array(P)  # Adjacency matrix of the smaller graph P

    # Get the exact indices where nodes from P are mapped in G
    indices = np.argmax(M, axis=1)  # Extract mapped node indices

    # Create the induced subgraph from G
    induced_G = A[np.ix_(indices, indices)]

    # Strict check: Ensure both the adjacency matrix and degree sequence match
    return np.array_equal(induced_G, B) and np.sum(induced_G, axis=1).tolist() == np.sum(B, axis=1).tolist()

def prune(M, G, P):
    """Strictly removes impossible node correspondences based on structure."""
    valid = np.zeros_like(M)

    for i in range(M.shape[0]):  # Iterate over rows (nodes in P)
        for j in range(M.shape[1]):  # Iterate over columns (nodes in G)
            if M[i, j] == 1:
                # Get neighbors of P[i] and G[j]
                neighbors_P = np.where(P[i] == 1)[0]
                neighbors_G = np.where(G[j] == 1)[0]

                # Ensure that EVERY neighbor of P[i] has at least one corresponding mapped node in G[j]
                valid_mapping = all(
                    any(M[x, y] == 1 for y in neighbors_G) for x in neighbors_P
                )

                if valid_mapping and len(neighbors_P) <= len(neighbors_G):
                    valid[i, j] = 1  # This is a valid mapping
                else:
                    valid[i, j] = 0  # Remove invalid mapping immediately
            else:
                valid[i, j] = 0  # Remove non-valid mappings

    return valid

def ullman_recursive(used_columns, cur_row, G, P, M):
    """Recursive function for Ullman's algorithm."""
    if cur_row == M.shape[0]:  # Base case: all rows assigned
        if is_isomorphism(G, P, M):
            return True
        return False

    found_isomorphism = False

    for c in range(M.shape[1]):  # Iterate over possible columns
        if c not in used_columns:
            M_new = M.copy()
            M_new[cur_row, :] = 0  # Clear current row
            M_new[cur_row, c] = 1  # Assign column
            used_columns.add(c)

            pruned_M = prune(M_new.copy(), G, P)  # Apply strict pruning
            if ullman_recursive(used_columns, cur_row + 1, G, P, pruned_M):
                found_isomorphism = True

            used_columns.remove(c)  # Backtrack

    return found_isomorphism

def ullman_algorithm(G, P):
    """Main function to run Ullman's algorithm."""
    pa, pb = len(P), len(G)
    M0 = np.zeros((pa, pb), dtype=int)

    # Initialize M0 using degree constraints
    degrees_G = np.sum(G, axis=1)
    degrees_P = np.sum(P, axis=1)

    for i in range(pa):
        for j in range(pb):
            if degrees_P[i] <= degrees_G[j]:  # Only allow possible mappings
                M0[i, j] = 1

    pruned_M = prune(M0.copy(), G, P)  # Apply strict pruning before recursion
    
    found = ullman_recursive(set(), 0, G, P, pruned_M)
    return found
