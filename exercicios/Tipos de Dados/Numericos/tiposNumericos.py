# Tipos Numéricos:

# Int: Representa um número inteiro positivo ou negativo, de largura ilimitada. Ex:

x = 1
y = 348275982758927582
z = -3142343124

# Float: Representa um número com parte decimal, positiva ou negativa, contendo um ou mais casas decimais. Ex:

x = 1.12
y = 1.0
z = -533.431

# Floats também podem representar números científicos com "e" para indicar potências de 10. Ex:

x = 35e3
y = 2E7
z = -92.7e100

# Complexos: Podem ser escritos com "j", representando sua parte imaginária. Ex:

x = 3+5j
y = 5j 
z = -32j


# Para converter esses tipos entre si, basta utilizar os métodos de casting, possuindo os nomes de seus tipos. Ex:

x = 1.5
y = 20
z = 23j

a = complex(x)
b = float(y)

# Obs: números complexos não podem ser convertidos.

print(type(a))
print(type(b))

# Extra: Para gerar números aleatórios em Python, podemos importar o módulo random. Ex:

import random

print(random.randrange(1, 20))