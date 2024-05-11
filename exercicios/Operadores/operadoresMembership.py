# Operadores de Associação checam se um item de determinada sequência (lista, tupla, dicionário):

tupla1 = (2,4,6,8,10)

lista1 = [1,3,5,7,9]

dict1 = {"nome": "Renan", "nascimento": 30072002}

print(1 in tupla1)
print(5 in lista1)

print("Renan" in dict1.values())
print("nascimento" in dict1.keys())