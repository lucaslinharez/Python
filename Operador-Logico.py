# Operador AND funciona para chegar mais de uma condição. Exemplo;

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')


senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')

else:
    print('Sair')

# Avaliação de curto circuito AND. Irá avaliar até encontrar False, 0, None e string vazia ' '.
# Serve para economizar recursos, visto que a condição termina no primeiro False

# Exemplo:

print(True and True and False and True)

# Ao rodar esse código, ele avalia toda a operação como False

# Exemplo 2

print(True and 0 and True)

# Operador OR avalia a expressão inteira como verdadeiro

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')


senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e' )and senha_digitada == senha_permitida:
    print('Entrar')

else:
    print('Sair')

# Avaliação de curto circuito OR - no código abaixo, a operação avalia até o primeiro
# verdadeiro, ou seja, nesse caso seria o 'abc', pois está antes do True

print(True or False or 0 or 'abc' or True)

# Exemplo 2

senha = input('Senha: ') or 'Sem senha'

# Operador NOT inverte as expressões

# Exemplo

print(not True)  # False 
print(not False) # True

# Operador IN e NOT IN - serve para chegar strings e suas letras
# IN - checa se possui
# NOT IN - checa se não possui

# Exemplo

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')