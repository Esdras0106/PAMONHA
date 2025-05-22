from dataclasses import dataclass
import os

def limpar():
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
        limpar()
        print("\t= Exibindo Dados =")
        print(f"Nome: {self.nome}\nIdade: {self.email}\nLogradouro: {self.endereco.logradouro}\nNúmero: {self.endereco.cidade}")        
       


nome = input("Digite seu nome: ")
email = input("Digite seu E-mail: ")

logradouro = input("Digite seu endereço: ")
numero = input("Digite o número da sua casa: ")
cidade = input("Informe qual a sua cidade: ")
endereco = Endereco(logradouro, numero, cidade)

enderecol = Endereco(logradouro, numero, cidade)
pessoal = Pessoa(nome, email, enderecol)

print("\n= Dado Pessoal =")
pessoal.exibr()