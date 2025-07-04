# Variaveis armazenam valores. Servem para guardar dados para serem manipulados ao longo do código.

# Exercícios de variaveis.

nome = "Bruno"
sobrenome = "Silva" 
idade = 29
altura = 1.70
maior_idade = idade >= 18
ano_nascimento = 1995

print("Nome: ", nome)
print("Sobrenome: ", sobrenome)
print("idade: ", idade)
print("altura: ", altura)
print("é maior de idade?: ", maior_idade)
print("nascimento: ", ano_nascimento)

# Pedir ao usuário dois numeros e realizar a soma.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um segundo numero: "))
soma = n1 + n2

print("A soma é: ", soma)

# Converter idade, pedir em ano e mostrar em meses, dias e semanas.

idade_anos = int(input("Digite o ano de nascimento: "))

idade_m = 2025 - idade_anos
idade_s = idade_m * 52
idade_d = idade_s * 365

print("A sua idade é: ", idade_m, "anos,", idade_s, "semanas, e", idade_d, "dias")

# Calculadora de salário, peça o nome do funcionário, salário, e porcentagem de aumento.
# Mostre o valor atualizado.

nome = input("Insira o nome do funcionário: ")
salario = int(input("Valor do ultimo salário; "))

atual = salario + 5

print("Salário atual: ", atual)

# Media de notas. Peça 3 notas de um aluno e calcule a média. Exiba o resultado.

aluno = input("Nome do aluno: ")
n1 = int(input("Insira a primeira nota: "))
n2 = int(input("Insira a segunda nota: "))

resultado = n1 + n2 / 2

print("A sua média é: ", resultado)