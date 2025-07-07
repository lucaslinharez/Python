"""Strings são textos exibidos. Sempre utilizar aspas simples ou duplas"""

"""Aspas simples: """
print('Olá mundo!')

"""Aspas duplas:"""
print("Olá mundo!")

"""Nesses formatos, o texto será exibido sem as aspas: Olá mundo!"""
"""Para inserir aspas que apareçam ao usuário, usamos # Escape"""

# Escape
print("\"Olá mundo!\"")

"""Podemos melhorar o código, usando aspas simples. Exemplo:"""
print('"Olá, mundo!"')

"""O processo pode ser feito ao contrário e não terá problemas"""

# Para formatação de f-strings: 

nome = 'Bruno Silva'
altura = 1.80
peso = 90
cidade = 'São Paulo'

linha1 = f'As informções de cadastro do {nome} são: {altura:.2f}, {peso}kg, e é da cidade de {cidade}'

print(linha1)

