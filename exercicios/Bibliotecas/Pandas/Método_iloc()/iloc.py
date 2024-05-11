""" O método iloc() pode retornar:
    - Um intervalo de linhas ou colunas na tabela
    Ex: df.iloc(linha inicial : linha final, coluna inicial : coluna final).

    - Um item específico, indicando seus índices de linha e coluna.
    Ex: df.iloc(linha, coluna). """


print(df.iloc[0:5, 0:3])  # Exibe da linha 0 a 5.° linha, e de 0 a 3.° coluna.
print("\n")
print(df.iloc[0, 1])  # Exibe item da linha 0, coluna 1 (Nome Produto)
