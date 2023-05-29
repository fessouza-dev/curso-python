"""
 Tuplas - são mais utilizadas para armazenar valores diferentes, representando um obj.
 Imutabilidade das tuplas - não podem ter seus valores sobrescritos 
 após terem sido criados, nem criar ou excluir valores
"""
x = (5, 10)
print(x)
print(type(x))

pessoa = ("João", 19, True)
# Unpacking
""""
Unpacking - Desempacotamento
Forma de atribuição de valores para Tuplas
obs: unpacking também funciona em listas, porém não é utilizada na mesma,
já que em listas se espera um grupo de valores para serem tratados em ordem
ou todas de uma vez só, já em Tuplas geralmente se esperar a representação de um Obj,
com elementos diferentes entre si (heterogenios) -> iterando em seus índices
"""
nome, idade, admin = pessoa
print(nome, idade, admin)

turma = (
    ("Nono ano", 3),
    [8, 9, 7]
)
print(turma)
