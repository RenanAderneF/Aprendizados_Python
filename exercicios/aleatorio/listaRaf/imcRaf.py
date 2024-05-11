altura = float(input("Digite sua altura: "))
peso = float(input ("Digite seu peso: "))
idade = int(input ("Digite sua idade: "))
sexo = input("Digite 'M' para masculino e 'F' para feminino: ")

if idade > 10:

    imc = peso / altura**2
    print(imc)

    if 10 <= idade < 20 and sexo == "M":
        
        if idade == 10:
            if 14.42 < peso <= 19.60:
                print("Você está na categoria adequada para sua idade.")
            
            elif peso < 14.42:
                print("Você está abaixo do peso ideal para sua idade.")

            else:
                print("Você está acima do peso para sua idade.")

        elif idade == 11:
            if 14.83 < peso <= 20.35:
                print("Você está na categoria adequada para sua idade.")
            
            elif peso <= 14.83:
                print("Você está abaixo do peso ideal para sua idade.")

            else:
                print("Você está acima do peso para sua idade.")

        
        elif idade == 12:
            if 15.24 < peso < 21.12:
                print("Você está na categoria adequada para sua idade.")
            
            elif peso <= 14.83:
                print("Você está abaixo do peso ideal para sua idade.")

            else:
                print("Você está acima do peso para sua idade.")

        

    else:
        print("kill yourself")





