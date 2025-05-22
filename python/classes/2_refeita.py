from dataclasses import dataclass
import os

def limpar():
    os.system("cls || clear")

# Definindo classe.
@dataclass
class Pessoa ():
    nome: str
    email: str
    telefone: int
    endereco: str
    def exibr(self):
        print("\n\t= Exibindo Dados =")
        print(f"\nNome: {self.nome}\nE-mail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}\n")        
        limpar()

limpar()
print(f"\t= Solicitando Dados =")
nome = input("Digite seu nome: ")
email = str(input("Digite sua email: "))
telefone = int(input("Digite seu telefone: "))
endereco = str(input("Digite seu endereço: "))

pessoa = Pessoa(nome=nome, email=email, telefone=telefone, endereco=endereco)

pessoa.exibr()

