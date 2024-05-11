# Operadores Lógicos:

"""
'and': Retorna verdadeiro se ambas as declarações foram verdadeiras. 
'or': Retorna verdadeiro se uma ou ambas as declarações forem verdadeiras. 
'not': Retorna falso se o valor for verdadeiro e vice e versa. 
"""

num1 = 11
num2 = 5

print(num1 < 10 and num2 < 10)  # Falso e Verdadeiro, logo Falso
print((num1 or num2) > 10)  # Falso ou Verdadeiro, logo Verdadeiro
print(not (num1 < 10 and num2 < 10))  # NOT Falso, logo Verdadeiro


