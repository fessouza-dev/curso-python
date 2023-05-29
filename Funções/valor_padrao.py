# caso não sejam passados valores para a função, 
# será utilizado como parametro os valores padrões da mesma
def calcular_conta(consumo, taxa_servico=0.1, desconto_fidelidade=0):
    if taxa_servico == 0 and desconto_fidelidade == 0:
        return consumo # early return
    servico = consumo * taxa_servico
    desconto = consumo * desconto_fidelidade
    valor = consumo + servico
    valor = valor - desconto
    return valor
  
valor = calcular_conta(consumo=100, taxa_servico=0.1, desconto_fidelidade=0.05)
print("O valor é:", valor)
