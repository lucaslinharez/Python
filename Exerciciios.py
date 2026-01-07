
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