import os
os.system("cls || clear ")

print("CONTAGEM DE NÚMEROS ÍMPARES")

media_par = 0
soma = 0
impar = 0
par = 0
quantidade = 0
while True:
    numero = float(input("Digite o número: "))
    if numero % 2 !=0 :
        impar += 1
        soma += 1   
    if numero % 2 == 0:
        par += numero
        soma += 1
    if numero == 0:
        break

    quantidade += numero
    media_par = par / soma 
    media = quantidade / numero


print(f"Media: {media: .1f}")
print(f"Média par: {media_par: .1f}")