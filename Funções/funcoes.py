def dar_boas_vindas(nome, sobrenome, nome_do_curso):
    print("Olá,", nome, sobrenome)
    print("Bem vindo ao curso de", nome_do_curso)
    
dar_boas_vindas("João", "Souza", "JavaScript"); # Argumentos posicionais -> faz diferença a posição em que são passados

def calcular_conta(consumo, taxa_servico, desconto_fidelidade):
    if taxa_servico == 0 and desconto_fidelidade == 0:
        return consumo # early return
    servico = consumo * taxa_servico
    desconto = consumo * desconto_fidelidade
    valor = consumo + servico
    valor = valor - desconto
    return valor
  
valor = calcular_conta(consumo=100, taxa_servico=0.1, desconto_fidelidade=0.05)
print("O valor é:", valor)
