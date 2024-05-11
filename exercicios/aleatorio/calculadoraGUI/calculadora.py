resultado = 0
continuar = ""

while True:

    
    print("Digite a operação/sinal antecedente ao número.")
    print("Opções:(+, -, *, /), 'r' para mostrar o resultado e 'p' para encerrar o loop. ")
    operacao = input()

    if operacao == 'p':
        break
         
    elif operacao == 'r':
        print(resultado)
        resultado = 0
        continuar = input("Calculadora zerada. Deseja calcular novamente? (S/N)")
        if continuar == "N" or continuar == "n":
            break

        else:
            continue
            
    elif operacao not in ("+", "-", "*", "/"):
        print("Operador inválido.")
        break

    print("Digite um número. OBS: Números reais são permitidos.")    
    num = float(input(""))

    if operacao == '+':
        resultado += num

    elif operacao == '-':
        resultado -= num

    elif operacao == '*':
        resultado *= num

    elif operacao == '/':
        if num == 0:
            print("Não é possível dividir por zero.")

        else:
            resultado /= num


