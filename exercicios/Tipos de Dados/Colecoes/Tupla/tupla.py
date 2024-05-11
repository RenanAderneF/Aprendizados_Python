# Tuplas são listas, porém não são modificáveis:

tupla_carros = ("HRV", "Golf", "Argo")

for carro in tupla_carros:
    print(carro)

"""É possível realizar casting de uma tupla para uma lista, a fim de se modificar 
essa lista em um momento desejado:"""

lista_carros = list(tupla_carros)
lista_carros.append("Virtus")
print(lista_carros)

tupla_carros = tuple(lista_carros)
print(tupla_carros)