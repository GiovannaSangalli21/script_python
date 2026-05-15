# Dada a lista L = [5, 7, 2, 9, 4, 1, 3] Escreva um programa que imprima as seguintes informações: a) tamanho da lista. b) maior valor da lista. c) menor valor da lista. d) soma de todos os elementos da lista. e) lista em ordem crescente. f) lista em ordem decrescente.

# 8
L = [5, 7, 2, 9, 4, 1, 3]
tamanho = len(L)
print(f"a) Tamanho da lista: {tamanho}")
maior = max(L)
print(f"b) Maior valor: {maior}")
menor = min(L)
soma= sum(L)
print(f"c) Ordem crescente: {soma}")
crescente = sorted(L, reverse=True)
print(f"e) Ordem crescente: {crescente}")
