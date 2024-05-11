""" A função input é nativa do Python, e recebe comandos de entrada diretamente do teclado. Seu valor é então retornado
a uma variável """

nota1 = float(input("Insira sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota: "))

media = (nota1 + nota2)/2

if media >= 7:
    print("Congratulations! You have passed!")

else:
    print("You're reproved")

