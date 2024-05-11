import math as m 

def real_para_bin(real):
    '''Recebe um número real, e transforma-o em binário, analisando sua parte 
    inteira e sua parte decimal e aplicando os métodos necessários.'''

    valor = real  # Armazena valor de entrada do usuário na variável "valor". Ex: 5,625

    lista_inteiros = []  # Lista que receberá a parte inteira das iterações.

    lista_decimal = [] # Essa lista armazenará os decimais para checar se há repetição dos termos e assim saber se o número pode ser representado ou não.


    # Separa a parte inteira da fracionária para identificar o método utilizado para a conversão.

    int_e_dec = valor.split(".")  # retorna o valor inteiro e decimal separadamente.

    num_inteiro = int(int_e_dec[0])
    num_decimal = float("0." + int_e_dec[1])
    
    print(num_inteiro)
    print(num_decimal)

    # Na condição abaixo, caso a parte inteira do número seja diferente de 0, serão executadas as instruções nela contidas, configurando uma etapa adicional ao método.

    if num_inteiro != 0:  # 5,625 possui parte inteira diferente de 0, logo:

        print("if acessado")

        lista_resto = []  # Nela serão armazenados os restos das divisões de inteiros, que serão utilizados para o resultado da parte inteira em binário.

        while int(num_inteiro / 2) != 1 :  # a divisão inteira de 5/2 é 2, logo:

            print("while acessado")

            resto = num_inteiro % 2  # resto = 1
            print(resto)

            lista_resto += str(resto)
            num_inteiro = int(num_inteiro / 2)  # num_inteiro = 2

        if(num_inteiro % 2 == 0):
            lista_resto.append("0")  # Adiciona-se o coeficiente 0 no final da lista
            lista_resto.append("1")  # Adiciona-se o coeficiente 1 no final da lista
        
        else:
            lista_resto.append("1")  # Adiciona-se o coeficiente 0 no final da lista
            lista_resto.append("1")  # Adiciona-se o coeficiente 1 no final da lista

        lista_resto.reverse()  # Inverte a lista

        parte_inteira = "".join(lista_resto)  # parte inteira = 101

        print("Parte inteira: " + parte_inteira)

        
    while num_decimal != 0:

        num_decimal, num_inteiro = m.modf(float(valor))
        num_inteiro = int(num_inteiro)

        valor = float(num_decimal) * 2 # Parte decimal multiplicada e armazenada em valor.

        num_decimal, num_inteiro = m.modf(valor)
        num_inteiro = int(num_inteiro)

        lista_inteiros += str(num_inteiro)  # Adiciona parte inteira à lista.

        print("Número atual: " + str(valor))
        print("Parte inteira: " + str(num_inteiro))
        print("Parte decimal: " + str(num_decimal))

        

    
    print("Parte inteira das iterações: " + str(lista_inteiros))

    if parte_inteira == 0:
        lista_inteiros.insert(0, "0.")  # Adiciona um zero no fim da lista.

    result_decimal = "".join(lista_inteiros)

    print("Resultado: " + str(real) + "(base 10) = " + parte_inteira + "."+ result_decimal + "(base 2).")

    continuar = input("Tentar outro número? y [Sim] / n [Não]  ")

    if continuar == "y":
        real = input("Insira um número decimal: ")
        real_para_bin(real)


num = input("Insira um número decimal: ")
real_para_bin(num)
