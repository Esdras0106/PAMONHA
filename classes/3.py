from dataclasses import dataclass
import os
os.system("cls || clear")

# Definindo classe.
@dataclass
class Endereco: 
    logradouro: str
    numero: str

@dataclass
class Pessoa ():
    # Atributos da classe (variáveis que pertencem a uma classe).
    nome: str
    idade: int
    endereco: Endereco

    def exibr(self):
        print("\n\t= Exibindo Dados =")
        print(f"\nNome: {self.nome}\nIdade: {self.idade}\nLogradouro: {self.endereco.logradouro}\nNúmero: {self.endereco.numero}")        
        
endereco = Endereco("Rua A", "33" )
pessoa = Pessoa("Marta", 22, endereco)

print("\t= Dado da Pessoa =")
pessoa.exibr()
