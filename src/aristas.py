def comparar_subgrafos(grafo1, grafo2):
    """
    Compara subgrafos de dos grafos dados.

    Args:
        grafo1: Matriz de adyacencia del primer grafo.
        grafo2: Matriz de adyacencia del segundo grafo.
    """

    nodos_grafo1 = len(grafo1)
    nodos_grafo2 = len(grafo2)
    if nodos_grafo1 > nodos_grafo2:
        return False
    
    grafo_mayor = grafo2
    grafo_menor = grafo1
    tamano_menor = nodos_grafo1

    # Encontrar todos los subgrafos del grafo mayor del tamaño del grafo menor
    subgrafos = encontrar_subgrafos(grafo_mayor, tamano_menor)

    # Iterar a través de cada subgrafo y compararlo con el grafo menor
    for subgrafo in subgrafos:
        if(comparar_aristas(subgrafo, grafo_menor)): return True

def encontrar_subgrafos(grafo_mayor, tamano_menor):
    """
    Encuentra todos los subgrafos de un tamaño dado dentro de un grafo mayor.

    Args:
        grafo_mayor: Matriz de adyacencia del grafo mayor.
        tamano_menor: El número de nodos que debe tener cada subgrafo.

    Returns:
        Una lista de matrices de adyacencia, donde cada matriz representa un subgrafo.
    """
    import itertools

    nodos_grafo_mayor = len(grafo_mayor)
    subgrafos = []

    # Generar todas las combinaciones posibles de nodos para el subgrafo
    for combinacion in itertools.combinations(range(nodos_grafo_mayor), tamano_menor):
        # Crear la matriz de adyacencia para el subgrafo
        subgrafo = [[0] * tamano_menor for _ in range(tamano_menor)]
        
        # Mapear los nodos del grafo original a los nodos del subgrafo
        mapeo_nodos = {nodo_original: i for i, nodo_original in enumerate(combinacion)}

        # Llenar la matriz de adyacencia del subgrafo basándose en las aristas del grafo mayor
        for i in range(tamano_menor):
            for j in range(tamano_menor):
                nodo_i_original = combinacion[i]
                nodo_j_original = combinacion[j]
                subgrafo[i][j] = grafo_mayor[nodo_i_original][nodo_j_original]

        subgrafos.append(subgrafo)

    return subgrafos

def calcular_grado_nodo(grafo, nodo):
    """
    Calcula el grado de un nodo en un grafo representado por una matriz de adyacencia.

    Args:
        grafo: Matriz de adyacencia del grafo.
        nodo: El índice del nodo cuyo grado se va a calcular.

    Returns:
        El grado del nodo.
    """
    grado = 0
    for i in range(len(grafo)):
        grado += grafo[nodo][i]  # Suma las conexiones en la fila del nodo
    return grado

def obtener_aristas_ordenadas(grafo):
    """
    Obtiene una lista ordenada de aristas del grafo, donde cada arista se representa como una tupla (nodo_menor_grado, nodo_mayor_grado).

    Args:
        grafo: Matriz de adyacencia del grafo.

    Returns:
        Una lista de aristas ordenadas por el grado del nodo de menor grado.
    """
    aristas = []
    for i in range(len(grafo)):
        for j in range(i + 1, len(grafo)):  # Evita duplicados y auto-conexiones
            if grafo[i][j] == 1:
                grado_i = calcular_grado_nodo(grafo, i)
                grado_j = calcular_grado_nodo(grafo, j)
                if grado_i <= grado_j:
                    aristas.append((i, j))
                else:
                    aristas.append((j, i))
    
    # Ordenar las aristas por el grado del primer nodo (nodo de menor grado)
    aristas_ordenadas = sorted(aristas, key=lambda arista: calcular_grado_nodo(grafo, arista[0]))
    
    return aristas_ordenadas

def comparar_aristas(subgrafo, grafo_menor):
    """
    Compara las aristas de un subgrafo con las aristas de un grafo menor,
    verificando si las listas de grados de nodos correspondientes son iguales.

    Args:
        subgrafo: Matriz de adyacencia del subgrafo.
        grafo_menor: Matriz de adyacencia del grafo menor.
    """
    aristas_subgrafo = obtener_aristas_ordenadas(subgrafo)
    aristas_grafo_menor = obtener_aristas_ordenadas(grafo_menor)

    # Comprobar si las listas de aristas tienen la misma longitud
    if len(aristas_subgrafo) != len(aristas_grafo_menor):
        # print("Las listas de aristas tienen longitudes diferentes, no son iguales.")
        return

    # Comparar las aristas basándose en los grados de los nodos
    son_iguales = True
    for i in range(len(aristas_subgrafo)):
        grado_subgrafo_nodo_i = calcular_grado_nodo(subgrafo, aristas_subgrafo[i][0])
        grado_grafo_menor_nodo_i = calcular_grado_nodo(grafo_menor, aristas_grafo_menor[i][0])

        if grado_subgrafo_nodo_i != grado_grafo_menor_nodo_i:
            son_iguales = False
            break

    if son_iguales:
        # print("Los subgrafos son iguales en términos de grados de nodos en sus aristas.")
        return True
    else:
        # print("Los subgrafos no son iguales en términos de grados de nodos en sus aristas.")
        return False
