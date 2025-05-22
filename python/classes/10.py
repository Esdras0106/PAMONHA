import os 
from dataclasses import dataclass
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

    def exibir(self):
        print(f"\nTítulo: {self.titulo}\nAno: {self.ano}\nAutor:{self.autor.nome}\nBiografia: {self.autor.biografia}")

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
 
print("\n= Exibindo dados =")
for livro in lista_livros:
    livro.exibir()