import numpy as np
import random
import matplotlib.pyplot as plt
import cv2

# Carregar imagem
image_path = "./Otimizacao/dados.png"
image = cv2.imread(image_path)

# Verificar se a imagem foi carregada corretamente
if image is None:
    raise FileNotFoundError(f"Erro: Não foi possível carregar a imagem em {image_path}")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Definir intervalo para vermelho
lower_red1 = np.array([0, 120, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 100])
upper_red2 = np.array([180, 255, 255])

# Criar máscara para vermelho
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)

# Detectar contornos (cidades)
contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cities = np.array([cv2.boundingRect(cnt)[:2] for cnt in contours])

# Verificar se cidades foram detectadas
if len(cities) == 0:
    raise ValueError("Nenhuma cidade detectada na imagem. Verifique se há pontos vermelhos.")

# Função para calcular a distância total do caminho
def total_distance(cities, path):
    return sum(np.linalg.norm(cities[path[i]] - cities[path[i-1]]) for i in range(len(path)))

# Algoritmo de Subida de Encosta
def hill_climbing(cities, max_iters=1000):
    n = len(cities)
    best_path = list(range(n))
    random.shuffle(best_path)
    best_dist = total_distance(cities, best_path)
    
    for _ in range(max_iters):
        i, j = sorted(random.sample(range(n), 2))
        new_path = best_path[:i] + best_path[i:j+1][::-1] + best_path[j+1:]
        new_dist = total_distance(cities, new_path)
        
        if new_dist < best_dist:
            best_path, best_dist = new_path, new_dist
    
    return best_path, best_dist

# Algoritmo de Têmpera Simulada
def simulated_annealing(cities, initial_temp=100, cooling_rate=0.995, max_iters=10000):
    n = len(cities)
    path = list(range(n))
    random.shuffle(path)
    dist = total_distance(cities, path)
    temp = initial_temp
    
    for _ in range(max_iters):
        i, j = sorted(random.sample(range(n), 2))
        new_path = path[:i] + path[i:j+1][::-1] + path[j+1:]
        new_dist = total_distance(cities, new_path)
        
        if new_dist < dist or random.random() < np.exp((dist - new_dist) / temp):
            path, dist = new_path, new_dist
        
        temp *= cooling_rate
        if temp < 1e-8:
            break
    
    return path, dist

# Função para plotar e salvar imagem
def plot_and_save(cities, path, title, filename):
    plt.figure(figsize=(8, 6))
    plt.scatter(cities[:, 0], -cities[:, 1], c='red')
    
    # Corrigir erro de índice fora do intervalo
    ordered_cities = cities[np.append(path, path[0])]
    
    plt.plot(ordered_cities[:, 0], -ordered_cities[:, 1], 'b-')
    plt.title(title)
    plt.savefig(filename)
    plt.close()

# Executar e salvar resultados da Subida de Encosta
for i in range(10):
    hc_path, hc_dist = hill_climbing(cities)
    plot_and_save(cities, hc_path, f"Subida de Encosta - Distância: {hc_dist:.2f}", f"hc_result_{i}.png")

# Executar e salvar resultados da Têmpera Simulada
for i in range(10):
    sa_path, sa_dist = simulated_annealing(cities)
    plot_and_save(cities, sa_path, f"Têmpera Simulada - Distância: {sa_dist:.2f}", f"sa_result_{i}.png")
