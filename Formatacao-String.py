
# Formatação básica de String

""" 

 s - string 
 d - int
 f - float
 > - esquerda
 > - direita
 ^- centro
 

 """

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')

""" 

Função len conta a quantidade de caracteres usadas nas strings, incluindo campos vazios
Funciona além de strings

"""

# Exemplo:

variavel = 'Olá mundo'
print(len(variavel))

#Resultado: 9 caracteres incluindo espaço