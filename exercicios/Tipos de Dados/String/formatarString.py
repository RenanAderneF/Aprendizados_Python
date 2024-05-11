# Para concatenar strings, utilizamos "+":

str1 = "Eu tenho"
num1 = 9

print(str1 + " " + str(num1) + " biscoitos")

# Porém, existe uma formatação para strings em Python, conhecida como F-String, que muitas vezes é a forma preferível de
# se escrever strings concatenadas:

print(f"{str1} {num1} biscoitos")

# Os placeholders (as chaves com as variáveis dentro) podem conter um modificador para formatar o valor. Ele é utilizado
# colocando ":" após o nome da variável, e a formatação a ser feita, especificando o tipo de dado, e quantas casas
# decimais esse número pode ter, por exemplo:

str2 = "A sua média é:"
num2 = 5.45
num3 = 8.7
media = (num2 + num3)/2
print(f"Média sem formatação: {media}")

print(f"Média formatada: {str2} {media: .2f}")

# Placeholders também podem conter operações:

print(f"{str2} {((num2 + num3)/2): .2f}")

