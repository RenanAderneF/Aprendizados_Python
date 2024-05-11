import random  # Importando biblioteca

def jogaDado():
    d20 = random.randrange(1,20)
    print(f"resultado: {d20}")
    return d20

def turnoAtaque():

    attackTotal = 0

    if(jogaDado() >= 12):
        
        print("Você acertou o oponente! Você desfere...")
        
        listAttacks = [

            random.randrange(1,5), # Primeiro ataque
            random.randrange(1,5) # Segundo ataque
        ]

        for attackDmg in listAttacks:
            
            attackTotal += attackDmg
        
        print(f"{attackTotal} de dano.")
        
    else: 
        print("Você não acertou o oponente =(")
turnoAtaque()