from edges import comparar_subgrafos
from ullman_algorithm import ullman_algorithm
import numpy as np
g_a = np.array([[0, 0,1 ],
                [0, 0,0 ],
                [1, 0,0 ]])
  # Graph A adjacency matrix
g_b = np.array([[0, 1], [1, 0]])  # Graph B adjacency matrix

# print(ullman_algorithm(g_b, g_a))
# print(comparar_subgrafos(g_b,g_a))