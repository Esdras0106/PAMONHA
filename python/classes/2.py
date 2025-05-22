from dataclasses import dataclass
import os
os.system("cls || clear")

# Definindo classe.
@dataclass
class Pessoa ():
    nome: str
    email: str
    telefone: int
    endereco: str

# Definindo Valores.
# pessoa = Pesssoa("Marta" , 33 , 55, 333, 1.69)
print(f"\t= Solicitando Dados =")
nome = input("Digite seu nome: ")
email = str(input("Digite sua email: "))
telefone = int(input("Digite seu telefone: "))
endereco = str(input("Digite seu endereço: "))

pessoa = Pessoa(nome=nome, email=email, telefone=telefone, endereco=endereco)


print("\n\t Exibindo Dados")
print(f"Nome: {pessoa.nome}\nE-mail: {pessoa.email}\nTelefone: {pessoa.telefone}\nEndereço: {pessoa.endereco}\n")
