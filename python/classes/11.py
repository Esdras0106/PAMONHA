import os
os.system("cls || clear")
from dataclasses import dataclass


def limpar():
    os.system("cls || clear")

@dataclass
class Usuario:
    nome: str
    data_nascimento: float
    rg: float
    cpf: float
    
    def exibir(self):
        print(f"\nNome: {self.nome}\nData de nascimento: {self.data_nascimento}\nRG: {self.rg}\nCPF: {self.cpf}")
        
QUANTIDADE =  5
lista = []

for i in range(QUANTIDADE):
    usuario = Usuario(
    nome = input("Digite o nome do usuário: "),
    data_nascimento = input("Digite sua data de nascimento: "),
    rg =input("Informe seu RG: "),
    cpf = input("informe seu CPF: ")
    )
    limpar()  
   

lista.append(usuario)

nome_arquivo = "Funcionarios.txt"
with open(nome_arquivo, "a", encoding="utf-8") as arquivo_usuario:
    for livro in lista:
        arquivo_usuario.write(f"Nome: {usuario.nome}\nData de nascimento: {usuario.data_nascimento}\nRG do usuário: {usuario.rg}\nCPF do usuário: {usuario.cpf}")

print("*Dados salvos com sucesso*")

nome_arquivo = "Funcionarios.txt"
with open(nome_arquivo, "a", encoding="utf-8") as arquivo_usuario:
    for usuario in lista:
        arquivo_usuario.write(f"\nNome do Usuário: {usuario.nome}\nData de nascimento do usuário: {usuario.data_nascimento}\nRG do usuario: {usuario.rg}\nCPF do usuário: {usuario.cpf}")
print(f"\t\nSalvando . .  .")

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"{linha.strip()}")
except FileNotFoundError:
    print("Arquivo não encontrado")
