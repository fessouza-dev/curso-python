# 1
n1 = input("Digite um valor: ")
try:
    n1 = int(n1)
    i = 1
    soma = 0
    while i <= n1:
        soma = soma + i
        i = i + 1
except ValueError:
    print("Entrada inválida.")

print(soma)

# 2
n2 = input("Digite um valor: ")
try:
    n2 = int(n2)
    i = 2
    while i <= n2:
        print(i)
        i = i + 2
except ValueError:
    print("Entrada inválida.")
    
# Primo ou Não
n3 = input("Digite um valor: ")
try:
    n3 = int(n3)
    if n3 < 2:
        print("Não é primo")
    else:
        is_primo = True
        i = 2
        while i < n3:
            if n3 % i == 0:
                is_primo = False
                break
            i = i + 1
        if is_primo:
            print("É primo")
        else:
            print("Não é primo")
except ValueError:
    print("Entrada inválida.")

