# No lugar do casting, podemos utilizar o método format() para unir tipos de dados diferentes em um mesmo contexto:

cidade = "Rio de Janeiro"
dia = 30
mes = "Julho"
ano = 2002
data = "{}, {} de {} de {}"

print(data.format(cidade, dia, mes, ano))

# Com isso, é possível inserir o valor das variáveis nos placeholders correspondentes, muito parecido com o processo de inserir valores em um array.

num1 = 1
num2 = 3
num3 = 5
array1 = []
array1 = num1, num2, num3
print(array1)