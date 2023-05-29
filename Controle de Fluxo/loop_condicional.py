# Condicionais
idade = 15

if idade >= 18:
    print("Adulto")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")
    
# Loops
i = 1
while i <= 5:
    print(i)
    i = i + 1
    
# Loop 2
total = 0
continuar = "s"
while continuar == "s":
    valor = float(input("Digite o valor da compra: "))
    total = total + valor
    
    continuar = input("Deseja continuar? (s/n)\n")
    if continuar != "s":
        break
    
print("O valor total da compra é: ", total)
print("Fim")