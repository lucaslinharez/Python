
'''

Exercício

Peça ao usuário para digitar seu nome
Peça ao usuário para digitiar sua idade
Se nome e idade forem digitados
    Exiba: 
    Seu nome é {nome}
    Sua idade é {idade}
    Seu nome invertido é {nome invertido}
    Seu nome contém ou não espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A ultima letra do seu nome {letra}
Se nada for digitado em nome ou idade, exibir
    "Desculpe, você deixou campos vazios"


'''

nome = input('Digite seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertidos é: {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
        print(f'Seu nome tem: {len(nome)} letras')
        print(f'A primeira letra do seu nome é {nome[0]}')
        print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')

    
# Crie uma variável chamada nome que receba seu nome e imprima uma mensagem de boas-vindas.

nome = input('Insira seu nome: ')
print(f'Bem vindo: {nome} ')

# Crie duas variáveis numéricas e imprima a soma delas.

n1 = int(input('Insira um numero: '))
n2 = int(input('Insira o segundo numero: '))
resultado = n1 + n2
print('O resultado é: ', resultado)

# Faça um programa, que ao inserir um numero, diga se é maior que 10

numero = int(input("Insira um numero: "))

if numero >= 10 :
    print(f'O numero {numero} é maior que 10')
else: 
    print(f'O numero {numero} não é maior que 10')


"""
Um programa que peça ao usuário um numero inteiro, informe se é par ou impar
Caso o usuário não digite um numero inteiro, informe que não é. 

"""

numero = int(input('Insira um numero inteiro: '))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O numero é impar")

"""
Um programa que responde de acordo com o horario recebido. Ex; Bom dia.

"""

entrada = input("Insira o horário: ")

try: 
    hora = int(entrada)
    
    if  hora >= 0 and hora <= 11:
        print("Bom dia")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde")
    elif hora >= 18 and hora <= 23:
        print("Boa noite")
    else:
        print('Não conheço essa hora')
except:
    print('Somente numeros inteiros, tente novamente.')

"""
Um programa que solicita o nome do usuário, e caso tenha 4 letras ou menos
retorna "seu nome é curto"; se tiver entre 5 e 6 letras, retorna outra msg,
maior que 6 letras, "Seu nome é muito grande".

"""

nome = input("Digite seu nome")
contagem_nome = len(nome)

if contagem_nome > 1:
    if contagem_nome <= 4:
        print('Seu nome é curto')
    elif contagem_nome >= 5 and contagem_nome <= 6:
        print("Seu nome é tamanho médio")
    else:
        print('Seu nome é grande')
else:
    print('Por favor, digite ao menos uma letra')