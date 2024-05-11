# Toda variável criada fora de uma função é uma variável global. Elas podem ser usadas em qualquer escopo. Ex:

adjetivo = "incrível"


def descreve_python(complemento):
    print("python é " + complemento)


descreve_python(adjetivo)

# Criando uma variável local com o mesmo nome de uma global em uma função, caso o nome dessas variáveis seja
# utilizada dentro da mesma, será usado o valor armazenado na variável local, sem nenhuma chamada ou alteração do
# valor da variável global. Ex:

nome = "Renan"


def saudacao(nome):
    nome = "Guilherme"
    print("Olá! Meu nome é " + nome)


saudacao(nome)

print(nome)


# Também é possível criar uma variável global dentro de uma função utilizando a palavra-chave global. Ex:

def descrevePython2():
    global complemento
    complemento = "confuso"


descrevePython2()

print("Python é " + complemento)
