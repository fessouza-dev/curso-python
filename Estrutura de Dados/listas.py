# Listas - estrutura de dados ordenada
notas = [8, 10, 8.5]
print(notas[0])

notas.append(9)
print(notas)

i = 0
total = 0
qtd = len(notas) # quantidade de elementos dentro da lista
while i < qtd:
    total = total + notas[i]
    i += 1

print("O total das notas é:", total)

notas.sort() # ordena os valores em ordem crescente
print(notas)

notas.sort(reverse=True) # ordena os valores em ordem decrecente
print(notas)

notas.pop() # exclui o ultimo elemento da lista
print(notas)

notas.insert(0, 8) # insere o valor 8 na posição 0 da lista
print(notas)

notas.pop(0) # exclui o elemento indicado na pos. 0
print(notas)

# Listas podem armazenar valores de diferentes tipos
pessoa = ["João", 19, "123123"]
print("O nome é: ", pessoa[0])
print("A idade é: ", pessoa[1])

# Lista dentro de lista
pessoas = [
    ["João", 19],
    ["Bruno", 20]
]