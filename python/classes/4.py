from dataclasses import dataclass
import os
os.system("cls || clear")

# Definindo classe.
@dataclass
class Endereco: 
    logradouro: str
    numero: str
    cidade: str
@dataclass
class Pessoa:
    # Atributos da classe (variáveis que pertencem a uma classe).
    nome: str
    email: str
    endereco: Endereco
    
    def exibr(self):
        print("\t= Exibindo Dados =")
        print(f"Nome: {self.nome}\nIdade: {self.email}\nLogradouro: {self.endereco.logradouro}\nNúmero: {self.endereco.cidade}")        
        
endereco = Endereco("Rua A", 33, "Salvador")
nome = Pessoa("Marta", "marta@gmail.com", endereco)

print("= Dado da Pessoa =")
nome.exibr()