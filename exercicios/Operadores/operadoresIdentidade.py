#Operadores de Identidade ("is" e "is not") são utilizados para comparar objetos, verificando não se possuem o mesmo conteúdo, mas se de fato são o mesmo objeto, contendo a mesma locação de memória.


class Pessoa:

    nome = ""
    nascimento = 0
    cpf  = 0
    

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome= nome

    def getNasc(self):
        return self.nascimento
    
    def setNasc(self, nasc):
        self.nascimento = nasc
    

p1 = Pessoa()
p2 = Pessoa()

p1.setNome("Renan")
p1.setNasc(30072002)
p2.setNome("Renan")
p2.setNasc(30072002)

print(f"Endereço na memória: {id(p1)}")
print(f"Endereço na memória: {id(p2)}")

print(p1 is p2)

