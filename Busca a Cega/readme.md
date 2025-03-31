# Uniform Cost Search (UCS) - Análise de Desempenho

## Descrição
Este projeto implementa o algoritmo **Uniform Cost Search (UCS)** para encontrar o caminho de menor custo entre dois pontos em um grafo ponderado. O código também executa vários experimentos para avaliar a eficiência do UCS em termos de iterações necessárias para encontrar a solução.

## Funcionalidades
- **Implementação do UCS** para encontrar o menor caminho baseado no custo acumulado.
- **Conversão de distância em tempo de viagem**, assumindo uma velocidade média de 30 km/h e um tempo adicional de 4 minutos para cada parada.
- **Execução de experimentos** com diferentes números de execuções (100, 1.000 e 10.000 vezes) para analisar o desempenho do UCS.
- **Cálculo de estatísticas** sobre as iterações necessárias para encontrar a solução, incluindo média, mínimo e máximo.

## Como Executar
1. Certifique-se de ter o Python instalado (versão 3.6 ou superior).
2. Instale a biblioteca `statistics` (caso não esteja instalada):
   ```sh
   pip install statistics
   ```
3. Execute o script Python:
   ```sh
   python nome_do_arquivo.py
   ```

## Estrutura do Código
- **`ucs(graph, start, goal)`**: Implementa o algoritmo UCS para encontrar o menor caminho.
- **`run_experiments(graph, start, goal, num_trials)`**: Executa múltiplas execuções do UCS para medir desempenho.
- **`graph`**: Representação do grafo com distâncias entre os pontos.
- **Execução de experimentos**:
  - 100 execuções
  - 1.000 execuções
  - 10.000 execuções
- **Impressão de estatísticas**: Média, mínimo e máximo de iterações, melhor caminho encontrado, distância e tempo total estimado.

## Exemplo de Saída
```
1000_execucoes:
Média de iterações: 7.85
Mínimo de iterações: 5
Máximo de iterações: 12
Melhor caminho encontrado: E7 → E5 → E4 → E3 → E9 → E11
Distância total: 33.50 km
Tempo total: 78.20 minutos
```

## Autor
Desenvolvido por [Seu Nome].

## Licença
Este projeto é de uso livre sob a licença MIT.

