# Recebendo valores input
idade = input("Digite a idade: ")

# Inputs no python sempre retornam em forma de String dentro da variavel
print(type(idade))

# Conversão do tipo de variavel de String para Int
idade = int(idade)
print(type(idade))

print("É maior de idade?", idade >= 18)
print(idade)