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
        print(f"\nNome: {self.nome}\nAutor: {self.data_nascimento}\nCategoria: {self.rg}\nPreço: {self.cpf}")
        

lista = []

while True:
    usuario = Usuario(
    nome = input("Digite o nome do usuário: "),
    data_nascimento = input("Digite sua data de nascimento: "),
    rg =input("Informe seu RG: "),
    cpf = input("informe seu CPF: ")
    )
    limpar()  
    break

lista.append(usuario)

nome_arquivo = "Funcionarios.txt"
with open(nome_arquivo, "a") as arquivo_livros:
    for livro in lista:
        arquivo_livros.write(f"Nome: {usuario.nome}\nData de nascimento: {usuario.data_nascimento}\nRG do usuário: {usuario.rg}\nCPF do usuário: {usuario.cpf}")

print("*Dados salvos com sucesso*")

print(f"\t= EXIBINDO DADOS =")
for usuario in lista:
    usuario.exibir()
