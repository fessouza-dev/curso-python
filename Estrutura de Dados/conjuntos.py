"""
Conjuntos
Não admitem elementos repitidos e não garantem a ordenação de inserção de elementos
conseguem evitar duplicatas
"""

usuarios = {"alice", "bob"}
usuarios_2 = set(["bob", "lucas"])

usuarios.add("bob")
print(usuarios)

usuarios.add("carlos")
print(usuarios)

# União
print(usuarios.union(usuarios_2)) # também é possivel usar | (pipe)
e_igual = usuarios.union(usuarios_2) == usuarios | usuarios_2
print(e_igual)

# Intersecção
print(usuarios.intersection(usuarios_2)) # também é possivel usar &
# usuarios & usuario_2

# Diferença
print(usuarios.difference(usuarios_2)) # também é possivel usar -
# usuarios - usuarios_2


