# Python permite você associar valores para múltiplas variáveis em uma linha. Ex:

nome, sexo, altura, idade = "Renan", "Homem", 1.72, 21

print(nome)
print(sexo)
print(altura)
print(idade)

# Também é possível associar um valor para diversas variáveis. Ex:

corCabelo = corBarba = corSobrancelha = "castanho"

print(corCabelo)
print(corBarba)
print(corSobrancelha)

# Caso se tenha uma coleção em uma lista ou tupla, é possível extrair seus valores em variáveis. Esse processo é
# conhecido como unpacking. Ex:

alunosTurma1 = ["Renan", "Rian", "Jefferson"]
primeiroAluno, segundoAluno, ultimoAluno = alunosTurma1

print(primeiroAluno)
print(segundoAluno)
print(ultimoAluno)

