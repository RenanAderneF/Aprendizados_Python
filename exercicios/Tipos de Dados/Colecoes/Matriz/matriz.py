""" Matrizes são arrayLists, ou seja, uma lista de arrays"""

carros = [["Modelo", "HRV"],  # Matriz 3x3
          ["Fabricante", "Honda"],
          ["Ano", "2016"]]

# Imprimindo todos os itens da lista:

i = 0
while i < len(carros):
    print(carros[i])
    i += 1

# Imprimindo apenas os items da primeira coluna:
i = 0
j = 0

while i < (len(carros) - 1):
    while j < (len(carros) - 1):
        print(carros[i][j])
        i += 1

