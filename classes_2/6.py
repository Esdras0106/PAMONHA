import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Paciente:
    nome: str
    idade: int
    
    def exibir(self):
        print(f"\nNome: {self.nome}\nIdade: {self.idade}\n")
    
print(f"\t= EXIBINDO DADOS =")
paciente = Paciente(nome="Marta", idade=45)
paciente.exibir()
