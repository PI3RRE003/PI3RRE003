nome = input("Qual seu Nome?: ")  # Coleta o nome do usuário

print('Bem vindo(a) {} Loja do Vitor Pierre'.format(nome))  #Exibe a mensagem de boas vindas com o nome

valorProduto = float(input('Digite o valor unitario do produto: '))  # Variável que solicita o valor do produto
quantidadeProduto = int(input('Insira a quantidade: '))  # Variável que solicita o quantidade do produto

d1 = 0.04  #Desconto de 4%
d2 = 0.07  #Desconto de 7%
d3 = 0.11  #Desconto de 11%

valorFinal = valorProduto * quantidadeProduto

if valorFinal < 2500:
    print('Valor não atingido para desconto')
elif valorFinal < 500:  # Limita e compara com o valor total para obter a resposta ou prosseguir
    print('O valor total e de: {}' .format(valorFinal))# Limita e compara com o valor total para obter a resposta ou prosseguir
elif valorFinal >= 2500 and valorFinal < 6000:
    print('O valor total sem desconto é de: {:.2f}\n'
          'O valor total com desconto de 4% e de: {:.2f}' .format(valorFinal, valorFinal *(1 - d1)))# Calcula e subtrai o valor do desconto
elif valorFinal >= 6000 and valorFinal < 10000:
    print('O valor total sem desconto é de: {:.2f}\n'
          'O valor total com desconto de 7% e de: {:.2f}' .format(valorFinal, valorFinal *(1 - d2)))# Calcula e subtrai o valor do desconto
elif valorFinal >= 10000 :
    print('O valor total sem desconto é de: {:.2f}\n'
          'O valor total com desconto de 11% e de: {:.2f}'.format(valorFinal, valorFinal * (1 - d3)))  # Calcula e subtrai o valor do desconto
else:
    print('Ocorreu uma situação inesperada. por favor, tente novamente')