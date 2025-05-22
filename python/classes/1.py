from dataclasses import dataclass
import os
os.system("cls || clear")

# Definindo classe.
@dataclass
class Pessoa ():
    nome: str
    idade: int
    peso: float
    altura: float

print("= Solicitando Dados =")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

pessoa1 = Pessoa(nome=nome, idade=idade, peso=peso, altura=altura)
pessoa2 = Pessoa(nome, idade, peso, altura)

print("\n Exibindo Dados")
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nPeso: {pessoa1.peso}\nAltura: {pessoa1.altura}")
print(f"Nome: {pessoa2.nome}\nIdade: {pessoa2.idade}\nPeso: {pessoa2.peso}\nAltura: {pessoa2.altura}")