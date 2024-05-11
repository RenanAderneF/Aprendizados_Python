# Um dicionário é uma coleção de dados chave-valor:

dictCarros = {
    'Fabricante': 'Honda',
    'Modello': "HRV",
    'Ano': '2016',
    'Cor': 'Preta'
}

print(dictCarros.items())
print(dictCarros.keys())
print(dictCarros.values())

for chave, valor in dictCarros.items():
    print(chave + " : " + valor)


# Editando um valor em uma chave:

for chave, valor in dictCarros.items():

    if chave == "Fabricante":
        dictCarros["Fabricante"] = "Tesla"

print(dictCarros)


# Alterando a chave de um dicionário

# 1 Cria-se uma nova chave que recebe a chave antiga:

dictCarros["Modelo"] = dictCarros["Modello"]

# A nova chave é adicionada no final do dicionário, possuindo o mesmo valor:

print(dictCarros)

# Com isso, retira-se a chave anterior, utilizando a função pop():

dictCarros.pop("Modello")
print(dictCarros)


# Dicionários podem ter dicionários dentro dele:

dictCarros = {

    "Carro1": {

        "Fabricante": "Honda",
        "Modelo": "HRV"
    },

    "Carro2": {

        "Fabricante": "Volkswagem",
        "Modelo": "Golf"

    }
}

print(dictCarros)
print(dictCarros["Carro1"]["Modelo"])


""" É possível simplificar essa ideia criando esses dicionários fora do dicionário conjunto e depois
referenciá-los no dicionário conjunto: """

Carro1 = {

    "Fabricante": "Honda",
    "Modelo": "HRV"
}

Carro2 = {

    "Fabricante": "Volkswagem",
    "Modelo": "Golf"
}

dictCarros = {

    "C1": Carro1,
    "C2": Carro2
}

print(dictCarros)