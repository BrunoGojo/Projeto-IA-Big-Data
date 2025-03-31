import heapq
import random

def a_star_search(graph, start, goal, max_iterations=1000):
    open_set = []  # Fila de prioridade
    heapq.heappush(open_set, (0, start))
    came_from = {}  # Para reconstruir o caminho
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    iterations = 0
    while open_set and iterations < max_iterations:
        iterations += 1
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], g_score[goal], iterations
        
        for neighbor, distance in graph[current].items():
            tentative_g_score = g_score[current] + distance
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                heapq.heappush(open_set, (tentative_g_score, neighbor))
    
    return None, float('inf'), iterations  # Caminho não encontrado

def calculate_travel_time(path, graph, line_info):
    total_time = 0  # Tempo em minutos
    total_distance = 0
    
    for i in range(len(path) - 1):
        station1, station2 = path[i], path[i + 1]
        distance = graph[station1][station2]
        total_distance += distance
        total_time += (distance / 30) * 60  # Convertendo velocidade para minutos
        
        # Verifica troca de linha, exceto na última estação
        if i < len(path) - 2 and line_info.get(station1) != line_info.get(station2):
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
    "E1": 1, "E2": 2, "E3": 3, "E4": 4, "E5": 5, "E6": 6, "E7": 7,
    "E8": 8, "E9": 9, "E10": 10, "E11": 11, "E12": 12, "E13": 13, "E14": 14
}

# Teste com múltiplas iterações
start_node = "E7"
goal_node = "E11"
num_tests = 1
max_iterations = 100
results = []

for _ in range(num_tests):
    path, cost, iterations = a_star_search(graph, start_node, goal_node, max_iterations)
    if path:
        total_time, total_distance = calculate_travel_time(path, graph, line_info)
        results.append((path, cost, total_time, total_distance, iterations))

# Exibindo os caminhos encontrados
for i, r in enumerate(results):
    remaining_iterations = max_iterations - r[4]
    print(f"Progresso: Caminho {r[0]} | Tempo: {r[2]:.2f} min | Distância: {r[3]:.2f} km | Iterações: {r[4]}/{max_iterations} (restantes: {remaining_iterations})")
