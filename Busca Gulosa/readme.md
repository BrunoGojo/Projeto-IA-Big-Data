# A* Search para Rede de Metrô

## Descrição
Este projeto implementa o algoritmo de busca A* para encontrar o caminho mais curto entre duas estações de metrô em um grafo ponderado. O objetivo é determinar a rota mais eficiente com base na distância entre as estações e calcular o tempo total de viagem.

## Funcionalidades
- Utiliza o algoritmo A* para encontrar o caminho mais curto.
- Calcula a distância total do percurso.
- Estima o tempo total de viagem com base na velocidade do metrô e tempo de baldeação.
- Permite configurar um número máximo de iterações para controle de desempenho.

## Estrutura do Código
O código é composto pelas seguintes funções:

- `a_star_search(graph, start, goal, max_iterations)`: Implementa o algoritmo A* para encontrar o caminho mais curto entre duas estações.
- `calculate_travel_time(path, graph, line_info)`: Calcula o tempo de viagem e a distância total com base no caminho encontrado.

## Representação do Grafo
As estações de metrô são representadas por um grafo, onde:
- Os nós são as estações.
- As arestas representam a distância (em km) entre as estações.
- Um dicionário `line_info` identifica a linha de metrô associada a cada estação.

## Como Usar
1. Defina os nós de origem (`start_node`) e destino (`goal_node`).
2. Especifique o número máximo de iterações (`max_iterations`).
3. Execute o código para encontrar o melhor caminho, tempo de viagem e distância total.

## Exemplo de Saída
```
Progresso: Caminho ['E7', 'E5', 'E6', 'E5', 'E4', 'E3', 'E9', 'E11'] | Tempo: 46.80 min | Distância: 23.40 km | Iterações: 24/100 (restantes: 76)
```

## Dependências
O código usa apenas bibliotecas padrão do Python:
- `heapq`
- `random`

## Melhorias Futuras
- Implementar uma heurística mais eficiente para otimizar a busca.
- Adicionar visualização do grafo.
- Introduzir diferentes velocidades de trens por linha.

## Autor
Desenvolvido por [Seu Nome].

