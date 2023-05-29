# Percorrendo estrutura de Dados
notas = [8, 9, 10]

# i = 0
# while i < len(notas):
#    nota = notas[i]
#    i += 1
#    print(nota)

for nota in notas:
    print(nota)
    
# Dicionários, conjuntos, listas e tuplas são iteráveis

notas = {
    "alice": 10,
    "bob": 8,
    "carlos": 9
}

for nota in notas:
    print(nota)
    print(notas[nota])
    
"""
dict.keys() -> retorna um iterável (estrutura percorrível) apenas com as chaves daquele dicionário
dict.values() -> retorna um iterável apenas com os valores daquele dicionário
dict.items() -> retorna um iterável com cada elemento completo daquele dicionário
"""

print("\nKeys:")
for nota in notas.keys():
    print(nota)
 
print("\nValues:")   
for nota in notas.values():
    print(nota)

print("\nItems:")
for nota in notas.items():
    print(nota)

for v, k in notas.items():
    print(v, k)