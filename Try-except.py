
"""
Introdução básica Try-except
Serve para validar alguma excessão no script, porém, a sintaxe precisa estar 
correta. 


No exemplo abaixo, o programa com try/except indica a mensagem de erro
quando o usuário insere string em um campo para int

"""

numero_str = input('Vou dobrar o numero que você digitar')

try:
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:}')
except:
    print('Isso não é um numero')

# No resultado, aparece a mensagem de erro quando digitado uma string