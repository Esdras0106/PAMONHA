import os

# Função sem retorno
def logo_senai():
    os.system("cls || clear")   
    print(f"\t== SENAI ==")

logo_senai()    # Chamando a função
nome = input(f"\nDigite seu nome: ")

logo_senai()    # Chamando a função
idade = input(f"\nDigite sua idade: ")

logo_senai()    # Chamando a função
print(f"\nNome: {nome}")
print(f"Idade: {idade}")
