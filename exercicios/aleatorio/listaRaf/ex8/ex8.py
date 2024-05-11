from random import randint

eleitores = 0
votosBranco = 0
votosJoaoSilva = 0
votosJoseRamalho = 0
votosMariaMattos = 0
votosPedroAmerico = 0
votosNulo = 0

while eleitores <= 20000:

    voto = randint(0, 5)

    if voto == 0:
        votosBranco += 1

    elif voto == 1:
        votosJoaoSilva += 1

    elif voto == 2:
        votosJoseRamalho += 2

    elif voto == 3:
        votosMariaMattos += 3

    elif voto == 4:
        votosPedroAmerico += 4

    else:
        votosNulo += 1

    eleitores += 1

print(f"Votos em branco: {votosBranco}")
print(f"Votos de Joao Silva: {votosJoaoSilva}")
print(f"Votos de Jose Ramalho: {votosJoseRamalho}")
print(f"Votos de Maria Mattos: {votosMariaMattos}")
print(f"Votos de Pedro Americo: {votosPedroAmerico}")
print(f"Votos nulos: {votosNulo}")
