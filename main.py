import heapq
import networkx as nx

# Criando o grafo do metrô de Paris
metro_graph = nx.Graph()

# Adicionando arestas com base na Tabela 2 (distâncias reais)
edges = [
    ("E1", "E2", 10), ("E2", "E3", 8.5), ("E3", "E4", 6.3), ("E4", "E5", 13),
    ("E5", "E6", 3), ("E6", "E7", 3.4), ("E7", "E8", 9.6), ("E8", "E12", 6.4),
    ("E9", "E10", 12.2), ("E10", "E11", 17.6), ("E11", "E12", 14.2),
    ("E12", "E13", 28.8), ("E13", "E14", 5.1), ("E3", "E13", 18.7),
    ("E4", "E13", 12.8)
]

for edge in edges:
    metro_graph.add_edge(edge[0], edge[1], weight=edge[2])

# Dicionário com heurísticas baseadas na Tabela 1 (distâncias diretas)
heuristic = {
    "E1": 29.8, "E2": 21.8, "E3": 16.6, "E4": 15.4, "E5": 17.9, "E6": 18.2,
    "E7": 15.5, "E8": 27.2, "E9": 26.6, "E10": 21.5, "E11": 35.5, "E12": 33.6,
    "E13": 5.1, "E14": 0 
}
# Heurísticas baseando na tabela 2
heuristic1 = {
    "E1": 10, "E2": 8.5, "E3": 6.3, "E4": 13, "E5": 3, "E6": 3.4, "E7": 9.6,
    "E8": 6.4, "E9": 12.2, "E10": 17.6, "E11": 14.2, "E12": 28.8, "E13": 18.7,
    "E14": 5.1
}

def greedy_best_first_search(graph, start, goal, heuristic):
    """Implementação da busca gulosa pelo melhor primeiro."""
    frontier = [(heuristic1[start], start)]  # Fila de prioridade (heurística, estação)
    came_from = {start: None}  # Dicionário para reconstruir o caminho

    while frontier:
        _, current = heapq.heappop(frontier)  # Pega o nó com menor heurística

        if current == goal:
            # Reconstruindo o caminho
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Retorna o caminho da origem ao destino

        for neighbor in graph.neighbors(current):
            if neighbor not in came_from:  # Evita ciclos
                came_from[neighbor] = current
                heapq.heappush(frontier, (heuristic[neighbor], neighbor))

    return None  # Se não encontrar caminho

# Executando a busca gulosa de E1 até E14
path_greedy = greedy_best_first_search(metro_graph, "E11", "E7", heuristic)
print("Melhor caminho encontrado:", path_greedy)