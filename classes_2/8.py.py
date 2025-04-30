import os
os.system("cls || clear")
from dataclasses import dataclass


def limpar():
    os.system("cls || clear")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float
    
    def exibir(self):
        print(f"\nNome: {self.nome}\nAutor: {self.autor}\nCategoria: {self.categoria}\nPreço: {self.preco}")
        

lista = []
QUANTIDADE = 3

for i in range (QUANTIDADE):
    livro = Livro(
                    nome = input("Digite o nome do Livro: "),
                    autor = input("Digite o nome do autor(a): "),
                    categoria =input("informe qual a categoria do livro: "),
                    preco = input("Digite o preço do livro: ")
                )
    limpar()  
    lista.append(livro)

nome_arquivo = "catalogo_livros.txt"
with open(nome_arquivo, "a") as arquivo_livros:
    for  livro in lista:
        arquivo_livros.write(f"{livro.nome}, {livro.autor}\n{livro.categoria}\n{livro.preco}")

print("*Dados salvos com sucesso*")

print(f"\n\t= EXIBINDO DADOS =")
for livro in lista:
    livro.exibir()
