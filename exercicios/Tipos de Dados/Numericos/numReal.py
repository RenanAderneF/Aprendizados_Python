"""No exercicício abaixo, é mostrado como o computador, por interpretar números na base binária,
é incapaz de representar determinados números reais com exatidão. Em certos casos, ao tentar
converter um número real para binário, seriam supostamente necessários infinitos números para
representá-lo, o que faz com que o computador represente o número desejado de forma aproximada

No caso abaixo, o número é devidamente representado, visto que, a partir
do Método da Divisão Sucessiva, é possível zerar sua parte decimal. """

print(0.125 * 5)

"""Diferente do primeiro caso, ao tentar usar o método descrito, nos
encontramos em um loop, impossibilitados de zerar a parte decimal, sendo impossível
representar fielmente esse número em binário.
"""

print(3 * 0.1)
