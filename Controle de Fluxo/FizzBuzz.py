# FizzBuzz
print("FizzBuzz!\nCaso queira parar algum momento apenas digite 'n'")
while True:
    num = input("Digite um valor: ")
    if num == 'n':
        break
    try:
        num = int(num)
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print("...")
    except ValueError:
        print("Entrada inválida. Digite um número válido ou 'n' para parar.")
