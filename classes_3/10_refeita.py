import os 
from dataclasses import dataclass
os.system("cls || clear")

def limpar():
    os.system("cls || clear")

@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor :Autor

    def exibir_detalhes(self):
        print(f"\nTítulo: {self.titulo}\nAno: {self.ano}\n Autor:{self.autor.nome}")

lista_livros = []


print(f"\t= Solicitando Dados =")
livro = Livro(
            titulo = input(f"\nInsira o título do livro: "),
            ano = int(input("Insira o ano do livro: ")),
            autor = Autor(
                nome = input("Digite o nome do autor: "),
                biografia = input("Digite sobre a biografia do autor: ")
            )
        )   
limpar()

lista_livros.append(livro)

nome_arquivo = "olé.txt"
with open(nome_arquivo, "a", encoding="utf-8") as arquivo_livro:
    for livro  in lista_livros:
        arquivo_livro.write(f"\nTítulo do Livro: {livro.titulo}\nAno da publicação: {livro.ano}\nNome do autor: {livro.autor.nome}\nBiografia do autor: {livro.autor.biografia}")
print(f"\t\nSalvando . .  .")
try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"{linha.strip()}")
except FileNotFoundError:
    print("Arquivo não encontrado")


print(f"\n*Dados salvos com sucesso*")


