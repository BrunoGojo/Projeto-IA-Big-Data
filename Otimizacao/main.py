import numpy as np
import random
import matplotlib.pyplot as plt
import cv2

# Imagem será carregado
image_path = ".\Otimizacao\dados.png"
image = cv2.imread(image_path)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_red1 = np.array([0, 120, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 100])
upper_red2 = np.array([180, 255, 255])
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)
contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cities = np.array([cv2.boundingRect(cnt)[:2] for cnt in contours])

# Calcula a distância total de um caminho
def total_distance(cities, path):
    return sum(np.linalg.norm(cities[path[i]] - cities[path[i-1]]) for i in range(len(path)))

# Subida de Encosta
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

# Têmpera Simulada
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

# Plotar caminho
def plot_path(cities, path, title):
    plt.figure(figsize=(8, 6))
    plt.scatter(cities[:, 0], -cities[:, 1], c='red')
    ordered_cities = cities[path + [path[0]]]
    plt.plot(ordered_cities[:, 0], -ordered_cities[:, 1], 'b-')
    plt.title(title)
    plt.show()

# Testando Subida de Encosta
hc_path, hc_dist = hill_climbing(cities)
plot_path(cities, hc_path, f"Subida de Encosta (Teste) - Distância: {hc_dist:.2f}")

# Testando Têmpera Simulada
sa_path, sa_dist = simulated_annealing(cities)
plot_path(cities, sa_path, f"Têmpera Simulada (Teste) - Distância: {sa_dist:.2f}")
