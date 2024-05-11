import openpyxl as op

caminho_arquivo = 
planilha_nome =
coluna_links =


workbook = op.load_workbook(caminho_arquivo)
sheet = workbook[planilha_nome]

links = []

for cell in sheet[coluna_links]:
    link = cell.value
    if link:
        link.append(link)

print(links)