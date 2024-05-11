soma = 0
num = 1
numPar = 0

while numPar < 20:

    num += 1

    if num % 2 == 0:
        print(f"Número par: {num}")
        soma += num
        print(soma)
        numPar += 1


print(f"Soma: {soma}")
