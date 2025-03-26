import heapq

def a_star_search(graph, start, goal):
    open_set = []  # Fila de prioridade
    heapq.heappush(open_set, (0, start))
    came_from = {}  # Para reconstruir o caminho
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], g_score[goal]
        
        for neighbor, distance in graph[current].items():
            tentative_g_score = g_score[current] + distance
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                heapq.heappush(open_set, (tentative_g_score, neighbor))
    
    return None, float('inf')  # Caminho não encontrado

def calculate_travel_time(path, graph, line_info):
    total_time = 0  # Tempo em minutos
    total_distance = 0
    
    for i in range(len(path) - 1):
        station1, station2 = path[i], path[i + 1]
        distance = graph[station1][station2]
        total_distance += distance
        total_time += (distance / 30) * 60  # Convertendo velocidade para minutos
        
        # Verifica troca de linha
        if line_info.get(station1) != line_info.get(station2):
            total_time += 4  # Adiciona tempo de baldeação
    
    return total_time, total_distance

# Definição do grafo corrigido (baseado na Tabela 2)
graph = {
    "E1": {"E2": 10},
    "E2": {"E1": 10, "E3": 8.5, "E9": 10, "E10": 3.5},
    "E3": {"E2": 8.5, "E4": 6.3, "E9": 9.4, "E13": 18.7},
    "E4": {"E3": 6.3, "E5": 13, "E8": 15.3, "E13": 12.8},
    "E5": {"E4": 13, "E6": 3, "E7": 2.4, "E8": 30},
    "E6": {"E5": 3},
    "E7": {"E5": 2.4},
    "E8": {"E4": 15.3, "E5": 30, "E9": 9.6, "E12": 6.4},
    "E9": {"E2": 10, "E3": 9.4, "E8": 9.6, "E11": 12.2},
    "E10": {"E2": 3.5},
    "E11": {"E9": 12.2},
    "E12": {"E8": 6.4},
    "E13": {"E3": 18.7, "E4": 12.8, "E14": 5.1},
    "E14": {"E13": 5.1}   
}

# Definição das linhas do metrô
line_info = {
    "E1": 1, "E2": 2, "E3": 2, "E4": 2, "E5": 2, "E6": 1, "E7": 1,
    "E8": 2, "E9": 2, "E10": 1, "E11": 1, "E12": 1, "E13": 2, "E14": 1
}

# Teste do algoritmo
start_node = "E2"
goal_node = "E14"
path, cost = a_star_search(graph, start_node, goal_node)
total_time, total_distance = calculate_travel_time(path, graph, line_info)
print(f"Caminho encontrado: {path} com tempo total de {total_time:.2f} minutos e distância total de {total_distance:.2f} km")