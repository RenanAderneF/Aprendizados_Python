import pandas as pd

"""O método head() exibe os registros de uma tabela do início da tabela ao número inserido como parâmetro."""

janDf = pd.read_excel("janeiro_export.xlsx", engine="openpyxl")

print(janDf.head(5))
print(janDf["Nome Produto"][0:5])
