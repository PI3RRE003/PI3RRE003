# Imprime uma mensagem de boas-vindas ao usuário
nome = input('Informe o seu nome: ') # Pergunta o nome do Usuario
print('Bem-vindo Sr(a) {} ao nosso sistema de Fotocopiadora!'. format(nome))

servCopiadora = '''
Escolha o serviço desejado
DIG - Digitalização
ICO - Impressão Colorida
IPB - Impressão Preto e Branco
FOT - Fotocópia
'''

servExtras = '''
Serviços Adicionais
1 - Encadernação simples
2 - Encadernação de capa dura
0 - Sem serviço extra
'''

print(servCopiadora)  # Demonstra os serviços disponiveis

precos_servicos = {
'DIG': 1.10, # Preço do serviço de Digitalização por página
'ICO': 1.00, # Preço do serviço de Impressão Colorida por página
'IPB': 0.40, # Preço do serviço de Impressão Preto e Branco por página
'FOT': 0.20 # Preço do serviço de Fotocópia por página
}

# Define um dicionário com os preços dos serviços adicionais

precos_extras = {
1: 15.00, # Preço da encadernação simples
2: 40.00, # Preço da encadernação de capa dura
0: 0.00 # Sem serviço adicional
}

def escolha_servico():
    while True: # Loop infinito até que o usuário insira uma opção válida
        servico = input("Por favor, insira o serviço desejado (DIG/ICO/IPB/FOT): ")
        if servico in precos_servicos: # Verifica se a opção inserida é válida
            return servico # Retorna a opção escolhida pelo usuário
        else:
            print("Serviço inválido. Tente novamente.") # Imprime uma mensagem de erro se a opção não for válida

# Função para perguntar ao usuário quantas páginas eles querem e aplicar o desconto correspondente
def num_pagina():
    while True: # Loop infinito até que o usuário insira uma opção válida
        try:
            num_pagina = int(input("Por favor, insira o número de páginas: ")) # Pergunta ao usuário o número de páginas
            if num_pagina < 20: # Se o número de páginas for menor que 20, não há desconto
                return num_pagina
            elif num_pagina > 20 and num_pagina <=200: # Se o número de páginas for entre 20 e 200, o desconto é de 15%
                return num_pagina * 0.30
            elif  num_pagina > 200 and num_pagina <= 2000: # Se o número de páginas for entre 20 e 2000, o desconto é de 20%
                 return num_pagina * 0.8
            elif num_pagina > 2000 and num_pagina <= 20000: # Se o número de páginas for maior que 2000 ou igual a 20000, o desconto é de 25%
                 return num_pagina * 0.75
            else:
                print("Não aceitamos pedidos com essa quantidade de páginas.")
        except ValueError:
                print("Número inválido. Tente novamente.")

# Função para perguntar ao usuário quais serviços adicionais eles querem e calcular o custo total desses serviços
def servico_extra():
    total_extra = 0 # Inicializa o total de custos extras
# Loop que continua até que o usuário não queira mais nenhum serviço adicional
    while True:
        print(servExtras) # Imprime os serviços adicionais disponíveis
# Tenta converter a entrada do usuário para um inteiro
        try:
            extra = int(input("Por favor, insira o serviço adicional (1/2/0): "))
# Verifica se a entrada do usuário é um serviço adicional válido
            if extra in precos_extras:
                total_extra += precos_extras[extra] # Adiciona o custo do serviço adicional ao total
# Se o usuário inserir 0, isso significa que ele não quer mais nenhum serviço adicional
                if extra == 0:
                    return total_extra # Retorna o total de custos extras
            else:
                print("Serviço adicional inválido. Tente novamente.") # Imprime uma mensagem de erro se a entrada não for válida
        except ValueError:
                print("Entrada inválida. Tente novamente.")# Imprime uma mensagem de erro se a entrada não puder ser convertida para um inteiro

# Calcula o total a pagar com base no serviço escolhido, no número de páginas e nos serviços adicionais escolhidos pelo usuário
servico = escolha_servico()
num_pagina = num_pagina()
extra = servico_extra()
total = precos_servicos[servico] * num_pagina + extra
# Imprime o total a pagar pelo usuário
print("O total do seu pedido é: R$ {:.2f}".format(total))