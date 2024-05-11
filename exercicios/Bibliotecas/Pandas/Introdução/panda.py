import pandas as pd

""" Pandas é uma das bibliotecas mais úteis para ciência de dados em Python. Ela pode ser instalada através do
gerenciador de dependências pip, através de 'pip install pandas' no terminal. Pandas lida com dados tabulares, que são 
armazenados em planilhas ou bancos de dados.

Em Pandas, um dado de tabela é chamado de DataFrame.

O comando abaixo criar a variável df, que receberá a tabela fornecida na pasta.
A função 'read_csv()' lerá o documento e então o retornará para a variável:"""

pokeDf = pd.read_csv("../Pokemon.csv")


print(pokeDf)
print(pokeDf.head(2))  # Retorna as primeiras duas linhas da tabela

""" Para a leitura de arquivos excel, podemos utilizar o método 'read_excel()':

OBS: Pandas dependia da biblioteca 'xlrd' para leitura de dados e formatos Excel. Em iterações recentes, essa biblioteca 
limitou-se a ler apenas arquivos.xls. Atualmente, o Pandas conta com a biblioteca "openpyxl" como alternativa para 
leitura e manipulação de arquivos Excel, incluindo arquivos .xlsx, que correspondem aos arquivos das versões mais 
recentes do Excel. 

Para utilizar o openpyxl no lugar do xlrd, precisaremos instalar a biblioteca através de "pip install openpyxl" e depois
adicionar um argumento à função read.excel(), seu conteúdo sendo "engine = 'openpyxl'":
"""

employeesDf = pd.read_excel("Employees.xlsx", engine="openpyxl")
print(employeesDf)
