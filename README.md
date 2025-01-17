# Similaridade de Desempenho - Cálculo de Similaridade entre Vetores

Este projeto compara como três pessoas se saem em aspectos como pontualidade, qualidade de trabalho e outros critérios importantes, para revelar quais pares têm mais sintonia em termos de performance! Ideal para otimizar equipes e fortalecer colaborações.

Dessa forma, contém um código em Python que utiliza a biblioteca NumPy para calcular a similaridade entre vetores representando o desempenho de diferentes pessoas com base em critérios pré-definidos. O cálculo é realizado utilizando a **similaridade entre cossenos**.

---

## 📋 Descrição do Código

O código foi desenvolvido para comparar o desempenho de três indivíduos fictícios: **Paulo**, **Rosa** e **Judite**, com base em cinco dimensões de avaliação:  
1. **Pontualidade**  
2. **Qualidade do Trabalho**  
3. **Trabalho em Equipe**  
4. **Proatividade**  
5. **Resolução de Problemas**

Os valores atribuídos a cada dimensão para cada pessoa são representados como vetores. O código calcula a similaridade entre cossenos para determinar o quão alinhado está o desempenho entre eles.

---

## ⚙️ Como Funciona

1. **Criação dos Vetores**  
   Utiliza-se `np.array()` para criar vetores que representam as dimensões de avaliação de cada indivíduo:
   ```python
   p = np.array([8, 9, 7, 8, 6])  # Desempenho de Paulo
   r = np.array([6, 7, 8, 9, 5])  # Desempenho de Rosa
   j = np.array([10, 4, 2, 7, 6]) # Desempenho de Judite

2. **Cálculo do Produto Escalar**  
  O produto escalar entre os vetores é calculado com `np.dot()`, o que ajuda na determinação da similaridade entre cossenos.

3. **Cálculo dos Módulos dos Vetores**  
  O módulo de cada vetor é calculado com `np.linalg.norm()`.

4. **Similaridade entre Cossenos**  
  A similaridade entre dois vetores \(A\) e \(B\) é dada por:

  Sim(A, B) = cos(θ) = (A ⋅ B) / (||A|| ||B||)

  Resultados:
  - **1**: Vetores perfeitamente alinhados
  - **0**: Vetores sem relação
  - **-1**: Vetores opostos

5. **Resultados e Interpretação**  
  O código exibe:
  - A similaridade entre os pares (Paulo-Judite, Paulo-Rosa, Rosa-Judite).
  - Qual par possui maior e menor similaridade.


---

## 📊 Interpretação

- A **similaridade entre cossenos** é uma métrica útil para analisar o alinhamento entre dois conjuntos de dados.
- No contexto deste código, a análise ajuda a identificar indivíduos com desempenhos mais alinhados ou divergentes com base nas dimensões avaliadas.
