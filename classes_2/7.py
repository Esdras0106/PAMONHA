import os
os.system("cls || clear")
from dataclasses import dataclass

def limpar() :
    os.system("cls || clear")

@dataclass
class Pessoa ():
    nome: str
    idade: int
    peso: float
    altura: float
    
    # Método: uma função que pertence a uma classe.
    def exibr(self):
        print("\n\t= Exibindo Dados =")
        print(f"\nNome: {self.nome}\nIdade: {self.idade}\nIdade: {self.peso}\nAltura: {self.altura}\n")        
       

lista = []
QUANTIDADE_PESSOAS = 4

for i in range (QUANTIDADE_PESSOAS):
    print(f"\t= SOLICITANDO DADOS =")
    pessoa = Pessoa( 
                nome = str(input(f"\nDigite seu nome: ")),
                idade = int(input("Digite sua idade: ")),
                peso = float(input("Digite seu peso: ")),
                altura = float(input("Digite seu altura: "))
             )    
 
    limpar()
    lista.append(pessoa)

for pessoa in lista:
    pessoa.exibr()
