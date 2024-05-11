# Listas são coleções modificáveis em tamanho e valores. Elas são escritas delimitadas por parênteses. Seus itens podem ser acessados por seus índices, podendo ser manipulados à vontade:

carros = ["HRV", "Golf", "Argo", "Focus"]
print(carros)

carros[3] = "Virtus"
print(carros)

# O método append() adiciona novos itens à lista, sendo estes adicionados no final dela:

carros.append("Citroen")
print(carros)


# Já para remover itens, utilizamos o método remove(), que recebe o valor do item a ser removido:

carros.remove("Virtus")
print(carros)

# Caso não se tenha maneira clara de capturar o valor do item a ser removido, e sua metodologia de remoção seja sempre de tirar o último item da lista, podemos utilizar o método pop(), que justamente o faz:

carros.pop()
print(carros)

# Podemos também inserir os valores de uma lista em outra:

carros2 = carros
print(carros2)

# Para limpar o conteúdo de uma lista, pode-se utilizar o método clear():

carros.clear()
print(carros)

