import networkx as nx
from itertools import combinations

def node_degree_sequence(graph):
    """
    Returns a sorted list of node degrees for accurate element-wise comparison.
    """
    return sorted(dict(graph.degree()).values())

def find_isomorphic_subgraph(G1, G2):
    """
    Finds a subgraph in G2 that is isomorphic to G1 using node degrees and edge structure.
    """
    k = G1.number_of_nodes()
    target_degree_seq = node_degree_sequence(G1)

    for nodes_subset in combinations(G2.nodes(), k):
        subgraph = G2.subgraph(nodes_subset)

        # Step 1: Compare degree sequences element-wise
        sub_degree_seq = node_degree_sequence(subgraph)
        if any(sub_degree_seq[i] != target_degree_seq[i] for i in range(len(target_degree_seq))):
            continue  # Skip if node degrees don't match

        # Step 2: Check structural isomorphism
        if nx.is_isomorphic(subgraph, G1):
            return True  # Found an isomorphic subgraph

    return False  # No match found

# Example usage:
if __name__ == '__main__':
    G1 = nx.Graph()
    G1.add_edges_from([(0, 1), (1,2)])

    G2 = nx.Graph()
    G2.add_edges_from([
    (0, 1),
    (2, 3),
    (3, 5)
])

    # Check if there is an isomorphic subgraph
    print(find_isomorphic_subgraph(G1, G2))