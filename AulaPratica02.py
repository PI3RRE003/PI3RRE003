nome = input("Qual seu Nome?: ")  # Coleta o nome do usuário

print('Bem vindo(a) {} Loja de açai do Vitor Pierre'.format(nome))  #Exibe a mensagem de boas vindas com o nome

tabelaDePreços= '''
            Cardapio
Tamanho |  Cupuaçu(CP) | Açai(AC) |
   P    |   R$ 9,00    | R$ 11,00 |
   M    |   R$ 14,00   | R$ 16,00 |
   G    |   R$ 18,00   | R$ 20,00 |
'''
print(tabelaDePreços)

# Preços dos produtos
precos = {'CP': {'P': 9, 'M': 14, 'G': 18},
          'AC': {'P': 11, 'M': 16, 'G': 20}}

total = 0 # Inicializa o acumulador

while True: # Loop principal
    sabor = input("Por favor, insira o sabor (CP/AC): ")# Solicita o sabor ao usuário
    if sabor not in ['CP', 'AC']:
        print("Sabor inválido. Tente novamente.")
        continue

    tamanho = input("Por favor, insira o tamanho (P/M/G): ")# Solicita o tamanho ao usuário
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente.")
        continue


    total += precos[sabor][tamanho] # Adiciona o preço ao total

    mais = input("Deseja pedir mais alguma coisa? (S/N): ")# Pergunta se o usuário deseja continuar
    if mais.lower() != 's':
        break

# Imprime o total
print("O total do seu pedido é: R$ {:.2f}". format(total))
