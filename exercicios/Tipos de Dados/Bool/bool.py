# Expressões comparativas podem ser escritas diretamente, fora de uma estrutura
# condicional. Elas retornam true e false:

print(10 < 9)

# A função bool() permite que qualquer valor seja avaliado, retornando true ou false

print(bool(0))
print(bool("Hi"))
print(bool([]))

# Valores falsos em booleano são False, None, 0, "", (""),(()),([]),({})

# Funções podem retornar booleano.


def eh_de_verdade():
    return True


if eh_de_verdade():
    print("É de verdade!")


# Existe uma função nativa bool que checa se uma variável é do tipo de dado fornecido, chamado
# isinstance():

num1 = 200
print(isinstance(num1, int))
