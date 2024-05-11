# Strings podem ser escritas com aspas simples ou duplas. Ex:

print("Hello World")
print('Hello World')

# Strings multilinha são possíveis utilizando três aspas duplas ou simples. Ex:

a = """I may not be able to make you smile but,
I will never make you cry, 
even once,
never!"""

print(a)

# Strings como Arrays: Strings em Python são arrays de bytes representando caracteres unicode. Em Python,
# um caractere, por exemplo, representa uma String de largura 1.Ex:

a = "Olá!"
print(a[0] + a[1])

# Fazendo um loop em uma String: Visto que Strings são arrays, é possível realizar um loop em seus caracteres. Ex:

for x in "banana":
    print(x)

#  Largura de uma String: É possível capturar esse valor utilizando a função len(). Ex:

a = "paralelepípedo"

print(len(a))

# Checar String: Para encontrar um conteúdo específico em uma string, é possível utilizar a palavra-chave "in".
# Também é possível checar se algo não existe com "not in" Ex:

a = "Passa dor de cabeça, pelo amor de Deus"
print("Deus" in a)
print("!" in a)


# Cortando Strings: É possível retornar um range de caracteres usando a sintasse slice, especificando o índice de
# início e fim da string, separados por dois pontos. Ex:

a = "Eu não vou conseguir!"

print(a[7:])  # Utilizando dessa maneira, à partir do índice 7, todo o resto da string é capturado. O contrário ocorre
# ao apenas especificar o fim da string.




