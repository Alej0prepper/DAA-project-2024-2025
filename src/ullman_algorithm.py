import numpy as np

def initialize_m0(G_a, G_b):
    """
    Initializes the candidate matrix M0 for Ullmann's algorithm.
    
    Parameters:
    G_a (ndarray): Adjacency matrix of graph A.
    G_b (ndarray): Adjacency matrix of graph B.
    
    Returns:
    ndarray: Initial candidate matrix M0.
    """
    pa = len(G_a)
    pb = len(G_b)
    M0 = np.zeros((pa, pb), dtype=int)
    
    for i in range(pa):
        for j in range(pb):
            if degree(G_b, j) >= degree(G_a, i):
                M0[i][j] = 1
    return M0

def degree(graph, vertex):
    """
    Computes the degree of a given vertex in a graph.
    
    Parameters:
    graph (ndarray): Adjacency matrix of the graph.
    vertex (int): Index of the vertex.
    
    Returns:
    int: Degree of the vertex.
    """
    return sum(graph[vertex])
def prune(M, G_a, G_b):
    changed = True
    while changed:
        changed = False
        for i in range(M.shape[0]):  # Para cada fila
            for j in range(M.shape[1]):  # Para cada columna
                if M[i, j] == 1:
                    for neighbor_x in neighbors(G_a, i):
                        found_neighbor = False
                        for neighbor_y in neighbors(G_b, j):
                            if M[neighbor_x, neighbor_y] == 1:
                                found_neighbor = True
                                break
                        if not found_neighbor:
                            M[i, j] = 0
                            changed = True
                            break  # Salir del bucle interno si se cambia el valor
    return M

def neighbors(graph, vertex):
    neighbors_list = []
    for i in range(len(graph)):
        if graph[vertex][i] == 1:
            neighbors_list.append(i)
    return neighbors_list

def is_isomorphism(M_prime, G_a, G_b):
    """
    Checks if a given mapping matrix M_prime represents an isomorphism between G_a and G_b.
    
    Parameters:
    M_prime (ndarray): Current mapping matrix.
    G_a (ndarray): Adjacency matrix of graph A.
    G_b (ndarray): Adjacency matrix of graph B.
    
    Returns:
    bool: True if M_prime represents an isomorphism, False otherwise.
    """
    C = np.dot(M_prime, np.transpose(np.dot(M_prime, G_b)))
    pa = len(G_a)
    
    for i in range(pa):
        for j in range(pa):
            if G_a[i][j] == 1 and C[i][j] != 1:
                return False
    return True

# def prune(M):
#     """
#     Prunes the candidate matrix M to improve efficiency.
    
#     Parameters:
#     M (ndarray): Candidate matrix to be pruned.
    
#     Returns:
#     None
#     """
#     pass  # Implement pruning logic here

def recurse(used_columns, cur_row, G_a, G_b, M_prime):
    """
    Recursively explores possible mappings to find an isomorphism.
    
    Parameters:
    used_columns (set): Set of used columns in M_prime.
    cur_row (int): Current row index being processed.
    G_a (ndarray): Adjacency matrix of graph A.
    G_b (ndarray): Adjacency matrix of graph B.
    M_prime (ndarray): Current state of the mapping matrix.
    
    Returns:
    bool: True if an isomorphism is found, False otherwise.
    """
    if cur_row == len(M_prime):  # If all rows are filled
        return is_isomorphism(M_prime, G_a, G_b)
    # M_prime = prune(M_prime,G_a,G_b)
    for c in range(len(G_b)):
        if c not in used_columns:  # If column is not used
            M_prime[cur_row] = 0  # Reset row
            M_prime[cur_row][c] = 1  # Mark current column
            
            used_columns.add(c)
             # Clonar M_prime antes de la poda
            M_prime_cloned = M_prime.copy()
            
            # Aplicar poda
            prune(M_prime_cloned, G_a, G_b)
            if recurse(used_columns, cur_row + 1, G_a, G_b, M_prime):
                return True
            used_columns.remove(c)  # Unmark column
    
    return False

def ullman_algorithm(G_a, G_b):
    """
    Implements Ullmann's subgraph isomorphism algorithm.
    
    Parameters:
    G_a (ndarray): Adjacency matrix of the pattern graph A.
    G_b (ndarray): Adjacency matrix of the target graph B.
    
    Returns:
    None
    """
    M0 = initialize_m0(G_a, G_b)
    pa = len(G_a)
    M_prime = np.zeros_like(M0)
    
    if recurse(set(), 0, G_a, G_b, M_prime):
        return True
    else:
        return False

# # Example usage
# g_a = np.array([[0, 0,1 ],
#                 [0, 0,0 ],
#                 [1, 0,0 ]])
#   # Graph A adjacency matrix
# g_b = np.array([[0, 1], [1, 0]])  # Graph B adjacency matrix

# print(ullman_algorithm(g_b, g_a))