import pandas as pd

df = pd.read_csv("../Pokemon.csv")

# Lendo cabeçalhos da tabela:

print(df.columns)
print("\n")

# Lendo os registros de uma coluna específica (Por nome):

print(df['Name'])
print("\n")

# Retornando um intervalo de registros a serem lidos em uma coluna:

print(df['Type 1'][0:5])
print("\n")

# Lendo registros de várias colunas:

print(df[['Name', 'HP', 'Attack', 'Defense']])
print("\n")




