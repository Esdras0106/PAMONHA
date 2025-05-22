import os
os.system("cls || clear")
from dataclasses import dataclass


def limpar():
    os.system("cls || clear")

@dataclass
class Paciente:
    nome: str
    idade: int
    
    def exibir(self):
        print(f"\nNome: {self.nome}\nIdade: {self.idade}\n")
        

lista = []
QUANTIDADE = 2

for i in range (QUANTIDADE):
    paciente = Paciente(
                    nome = input("Digite seu nome: "),
                    idade = input("Digite sua idade: ")
                )
    limpar()  
    lista.append(paciente)

# Salvando em um arquivo com .txt
nome_arquivo = "Dados_paciente.txt"
with open(nome_arquivo, "a") as arquivo_pacientes:
    for  paciente in lista:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade}\n")

print("*Dados salvos com sucesso*")

print(f"\t= EXIBINDO DADOS =")
for paciente in lista:
    paciente.exibir()
