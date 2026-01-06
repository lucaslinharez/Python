# Operadores de comparação (relacionais)

maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 3
igual = 'a' == 'a' 
diferente = 'a' != 'b'

# Exemplo usando If/else como bloco de código.

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
