"""
string = '012345678901234567890123456789012345678901234567890123456789'
tenho que gerar algo assim:
lista = ['0123456789', '0123456789', '0123456789']
e depois fazer isso:
retorno = '0123456789.0123456789.0123456789.0123456789.0123456789'
"""

string = '012345678901234567890123456789012345678901234567890123456789'

teste = string.split(string[0:10:10])

# del teste[0]


print(teste)

teste = '.'.join(teste)
# print(teste)
