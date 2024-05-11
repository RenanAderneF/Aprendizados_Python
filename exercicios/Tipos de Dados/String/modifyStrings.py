# Os métodos upper() e lower() alteram a capitalização das letras de uma string.

frase1 = "Hoje é quinta-feira"
frase2 = "EU QUERO SER MELHOR"

print(frase1.upper())
print(frase2.lower())

# Também é possível realizar uma verificação booleana a fim de checar se a string em questão está capitalizada
# ou não:

print(frase1.isupper())
print(frase2.isupper())


# Com o método strip(), todo espaço em branco é removido de uma string:

print(frase1.strip())

# Esse método também possui um argumento opcional que recebe uma combinação de caracteres a serem excluídos:

frase3 = "www.fulano@yahoo.com.br"
print(frase3.strip("w."))

# O método split() divide uma string utilizando um caractere como divisor:

print(frase3.split("."))

