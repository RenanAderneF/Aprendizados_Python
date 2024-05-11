""" A estrutura padrão do for consister em uma variável a ser incrementada/decrementada, a regra que ela deve seguir, e o
 que ocorrerá com ela após um loop. A forma mais próxima de C de expressar essa condicional seria: """

numLista = [0, 35, 76, 423, 12, 8, 7]

for i in range(0, len(numLista), 1):
    if numLista[i] % 2 == 0:
        print(numLista[i])

""" Nesse caso, a função range(), que retorna uma sequência, com valor inicial, limite e valor da incrementação/
decrementação, muito parecido com o for em C. Porém, para uma sintaxe facilitada, quando o objetivo é apenas percorrer 
itens do primeiro ao último item, utilizamos o operador de associação 'in':"""

carros = ['HRV', 'Golf', 'Argo', 'Focus']

for x in carros:
    print(x)

