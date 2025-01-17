import numpy as np

#utilizar np.array pois é uma função da biblioteca Numpy para criar um array (vetor)
p = np.array([8, 9, 7, 8, 6])
r = np.array([6, 7, 8, 9, 5])
j = np.array([10, 4, 2, 7, 6])

#calcular o produto escalar para calcular a similaridade entre cossenos
produto_escalar_p_r = np.dot(p, r)
produto_escalar_p_j = np.dot(p, j)
produto_escalar_r_j = np.dot(r, j)

#calcular o módulo de cada vetor para calcular a similaridade entre cossenos
modulo_p = np.linalg.norm(p)
modulo_r = np.linalg.norm(r)
modulo_j = np.linalg.norm(j)

#calcular similaridade entre cossenos para constatar se está mais próxima de 1 (vetores perfeitamente alinhados), se é igual a 0 (vetores sem relação) ou próxima de -1 (vetores opostos)
similaridade_p_r = produto_escalar_p_r / (modulo_p * modulo_r)
similaridade_p_j = produto_escalar_p_j / (modulo_p * modulo_j)
similaridade_r_j = produto_escalar_r_j / (modulo_r * modulo_j)

#resultado
print(f'A similaridade entre Paulo e Judite é {similaridade_p_j:.3f}, entre Paulo e Rosa é {similaridade_p_r:.3f} e entre Rosa e Judite é {similaridade_r_j:.3f}.')

similaridade = {
    'Paulo e Judite' : similaridade_p_j,
    'Paulo e Rosa' : similaridade_p_r,
    'Rosa e Judite' : similaridade_r_j
}

maior_similaridade = max(similaridade, key=similaridade.get)
menor_similaridade = min(similaridade, key=similaridade.get)

print(f'{maior_similaridade} possuem desempenho muito semelhante com relação às três combinações.')
print(f'{menor_similaridade} possuem a menor similaridade entre as três combinações, ou seja, seus desempenhos são menos alinhados.')