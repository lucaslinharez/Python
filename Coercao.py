# Coerção Implícita, é feita automaticamente pelo interpretador do Python
# Quando dois types compativeis são usados na mesma operação.

a = 5
b = 2.0
c = a + b
print(c)
print(type(c))

# Coerção Explícita (casting) é feita manualmente pelo programador
# utilizando funções como int(), float(), str(), entre outras

x = "10"
y = 5
z = int(x) + y  # Faz a conversão explícita de string para inteiro
print(type(z))  # Saída mostrando o type convertido

# Importante: 
# Coerção implícita só ocorre entre tipos compatíveis (por exemplo: int e float).
# Python é fortemente tipado, então não força coerções arriscadas ou incoerentes automaticamente (como somar int com str, o que dá erro).
# A coerção explícita te dá mais controle, mas você deve garantir que o valor seja realmente compatível. 
# Exemplo:

int("abc")  # Vai gerar ValueError

# Mais exemplos de conversão

print(str(10) + 'a')
print(type(float('10') + 10))
print(type(bool(' ')))